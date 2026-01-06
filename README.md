# Mini Priority Scheduler – Group 8

**Operating System Capstone Project**  
**Option A: Mini Scheduler** – Priority-based scheduler for 5 simulated processes

### Group Members
- Member 1 STEPHANO EDWARD
- Member 2 NAJAAH GELEMA
- Member 3 JOFREY JONATHAN
- Member 4 ARAFA GOGOLA

### Overview
This project implements a **non-preemptive priority-based CPU scheduler** that simulates scheduling for 5 processes.  
Each process has:
- PID
- Arrival time
- Burst time
- Priority (lower number = higher priority)

The scheduler calculates waiting time, turnaround time, averages, and displays a text-based Gantt chart.

### Features
- Handles different arrival times
- Selects the highest-priority ready process
- Simulates CPU idle time when no process is ready
- Prints detailed results table
- Shows average waiting and turnaround times
- Visualizes execution order with Gantt chart

### Design Choices
- **Non-preemptive**: Once a process starts, it runs to completion (simpler implementation, highlights starvation risk)
- **Priority**: Lower number = higher priority (standard convention)
- Written in Python for easy execution and understanding

### How to Run
```bash
python scheduler.py
