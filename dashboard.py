from bcc import BPF

program = """
#include <uapi/linux/ptrace.h>

TRACEPOINT_PROBE(sched, sched_process_fork)
{
    bpf_trace_printk("FORK parent=%d child=%d\\n", args->parent_pid, args->child_pid);
    return 0;
}

TRACEPOINT_PROBE(sched, sched_process_exec)
{
    bpf_trace_printk("EXEC pid=%d\\n", bpf_get_current_pid_tgid() >> 32);
    return 0;
}

TRACEPOINT_PROBE(syscalls, sys_enter_openat)
{
    char fname[64];
    bpf_probe_read_user_str(&fname, sizeof(fname), (void *)args->filename);
    bpf_trace_printk("OPEN pid=%d file=%s\\n", bpf_get_current_pid_tgid() >> 32, fname);
    return 0;
}
"""

b = BPF(text=program)

print("=== eBPF Explorer Dashboard ===")
print("Monitoring: Fork | Exec | Open events")
print("Press Ctrl+C to stop\n")

b.trace_print()
