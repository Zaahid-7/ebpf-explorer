from bcc import BPF

program = """
#include <uapi/linux/ptrace.h>

TRACEPOINT_PROBE(sched, sched_process_exec)
{
    bpf_trace_printk("Exec: pid=%d\\n", bpf_get_current_pid_tgid() >> 32);
    return 0;
}
"""

b = BPF(text=program)

print("Listening for exec events...")

b.trace_print()
