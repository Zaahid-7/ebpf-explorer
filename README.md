# eBPF Explorer

A simple Linux system call and process event monitor built using eBPF (BCC framework) on Kali Linux.

## Overview

This project demonstrates real-time kernel-level event tracing using eBPF tracepoints. It monitors process creation (fork), program execution (exec), and file open operations (openat), then combines them into a unified dashboard.

## Components

- **fork_monitor.py** — Detects process fork events with parent and child PIDs
- **exec_monitor.py** — Detects process exec (program execution) events
- **open_monitor.py** — Detects file open (openat syscall) events with file paths
- **scheduler_monitor.py** — Detects CPU scheduler context switches
- **dashboard.py** — Combined real-time monitor for fork, exec, and open events

## Requirements

- Linux kernel with eBPF/BCC support
- Python 3
- BCC (BPF Compiler Collection)

## How to Run

```bash
sudo python3 dashboard.py
```

In another terminal, run any command (e.g. `ls`, `cat file`) to generate events.

## Project Structure
ebpf-project/

├── fork_monitor.py

├── exec_monitor.py

├── open_monitor.py

├── scheduler_monitor.py

├── dashboard.py

├── notes.txt

├── report/

└── screenshots/


## Author

Zahid Hossain
Inkiyed Tanzir
Durjoy Dey
