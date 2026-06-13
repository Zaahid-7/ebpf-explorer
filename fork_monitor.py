from bcc import BPF

program = """
TRACEPOINT_PROBE(sched, sched_process_fork)
{
    bpf_trace_printk("Fork detected\\n");
    return 0;
}
"""

b = BPF(text=program)

print("Listening for fork events...")

b.trace_print()
