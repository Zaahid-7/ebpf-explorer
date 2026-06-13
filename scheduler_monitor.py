from bcc import BPF

program = """
TRACEPOINT_PROBE(sched, sched_switch)
{
    bpf_trace_printk("Sched switch: prev=%s next=%s\\n", args->prev_comm, args->next_comm);
    return 0;
}
"""

b = BPF(text=program)

print("Listening for scheduler switch events...")

b.trace_print()
