from bcc import BPF

program = """
#include <uapi/linux/ptrace.h>

TRACEPOINT_PROBE(syscalls, sys_enter_openat)
{
    char fname[64];
    bpf_probe_read_user_str(&fname, sizeof(fname), (void *)args->filename);
    bpf_trace_printk("Open: pid=%d file=%s\\n", bpf_get_current_pid_tgid() >> 32, fname);
    return 0;
}
"""

b = BPF(text=program)

print("Listening for file open events...")

b.trace_print()
