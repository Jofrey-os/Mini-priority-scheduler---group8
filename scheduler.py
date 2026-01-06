from typing import List

class Process:
    def __init__(self, pid: int, arrival: int, burst: int, priority: int):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.priority = priority  # Lower number = higher priority
        self.start_time = -1
        self.completion_time = -1
        self.waiting_time = 0
        self.turnaround_time = 0

def priority_scheduling_non_preemptive(processes: List[Process]) -> None:
    processes.sort(key=lambda p: p.arrival)  # Initial sort by arrival
    
    time = 0
    completed = 0
    n = len(processes)
    gantt = []  # For visualization
    
    while completed < n:
        # Available processes at current time
        available = [p for p in processes if p.arrival <= time and p.completion_time == -1]
        
        if not available:
            gantt.append(("Idle", 1))
            time += 1
            continue
        
        # Select highest priority
        current = min(available, key=lambda p: p.priority)
        
        current.start_time = time
        time += current.burst
        current.completion_time = time
        current.turnaround_time = current.completion_time - current.arrival
        current.waiting_time = current.turnaround_time - current.burst
        gantt.append((f"P{current.pid}", current.burst))
        completed += 1
    
    # Output table
    print("\nPID | Arrival | Burst | Priority | Waiting | Turnaround")
    print("-" * 60)
    for p in sorted(processes, key=lambda p: p.pid):
        print(f"{p.pid:3d} | {p.arrival:7d} | {p.burst:5d} | {p.priority:8d} | {p.waiting_time:7d} | {p.turnaround_time:10d}")
    
    avg_wait = sum(p.waiting_time for p in processes) / n
    avg_tat = sum(p.turnaround_time for p in processes) / n
    print(f"\nAverage Waiting Time: {avg_wait:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    
    # Gantt Chart
    print("\nGantt Chart:")
    chart = " | ".join([f"{item} ({dur})" for item, dur in gantt])
    print(chart)
    total_time = time
    print("0" + "   " * (len(gantt) + 1) + f"{total_time}")

# 5 Simulated Processes
processes = [
    Process(1, 0, 8, 3),
    Process(2, 1, 4, 1),  # Highest priority
    Process(3, 2, 9, 4),
    Process(4, 3, 5, 2),
    Process(5, 4, 2, 5),  # Lowest priority
]

priority_scheduling_non_preemptive(processes)
