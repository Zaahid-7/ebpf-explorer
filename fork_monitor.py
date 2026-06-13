from bcc import BPF

program = """
#include <uapi/linux/ptrace.h>

TRACEPOINT_PROBE(sched, sched_process_fork)
{
    bpf_trace_printk("Fork: parent=%d child=%d\\n", args->parent_pid, args->child_pid);
    return 0;
}
"""

b = BPF(text=program)

print("Listening for fork events with PID info...")

b.trace_print()
