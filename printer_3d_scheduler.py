from typing import List, Dict
from dataclasses import dataclass


@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    jobs = [PrintJob(**job) for job in print_jobs]
    limits = PrinterConstraints(**constraints)

    def sort_key(job: PrintJob):
        return (job.priority, -job.print_time)

    jobs.sort(key=sort_key)

    total_time = 0
    print_order = []
    current_group = []
    current_volume = 0

    for job in jobs:
        if (current_volume + job.volume > limits.max_volume or
            len(current_group) + 1 > limits.max_items):
            if current_group:
                total_time += max(j.print_time for j in current_group)
                print_order.extend([j.id for j in current_group])
                current_group = []
                current_volume = 0
        current_group.append(job)
        current_volume += job.volume

    if current_group:
        total_time += max(j.print_time for j in current_group)
        print_order.extend([j.id for j in current_group])

    return {
        "print_order": print_order,
        "total_time": total_time
    }

def test_printing_optimization():
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
    ]

    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("# Тест 1: Моделі однакового пріоритету :")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Порядок друку: {result1['print_order']}")
    print(f"Загальний час: {result1['total_time']} хвилин\n")

    print("# Тест 2: Моделі різних пріоритетів :")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Порядок друку: {result2['print_order']}")
    print(f"Загальний час: {result2['total_time']} хвилин\n")

    print("# Тест 3: Перевищення обмежень об'єму :")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Порядок друку: {result3['print_order']}")
    print(f"Загальний час: {result3['total_time']} хвилин")