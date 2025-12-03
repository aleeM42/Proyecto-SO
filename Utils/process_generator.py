"""
Generador de procesos para pruebas
"""
import random
from Core.process import Process

class ProcessGenerator:
    """Genera procesos para pruebas del simulador"""
    
    @staticmethod
    def generate_random_processes(count=5, max_arrival=10, max_burst=15, max_priority=5):
        """Genera procesos aleatorios"""
        processes = []
        
        for i in range(count):
            pid = f"P{i+1}"
            arrival = random.randint(0, max_arrival)
            burst = random.randint(1, max_burst)
            priority = random.randint(1, max_priority)
            
            processes.append(Process(pid, arrival, burst, priority))
        
        return processes
    
    @staticmethod
    def generate_test_case_1():
        """Genera el Conjunto 1 de prueba obligatorio"""
        return [
            Process("P1", 0, 8, 3),
            Process("P2", 1, 4, 1),
            Process("P3", 2, 9, 4),
            Process("P4", 3, 5, 2)
        ]
    
    @staticmethod
    def generate_test_case_2():
        """Genera el Conjunto 2 de prueba obligatorio"""
        return [
            Process("P1", 0, 10, 2),
            Process("P2", 2, 3, 1),
            Process("P3", 4, 6, 3),
            Process("P4", 6, 1, 1),
            Process("P5", 8, 4, 2)
        ]
    
    @staticmethod
    def generate_io_bound_processes(count=4):
        """Genera procesos con características I/O bound"""
        processes = []
        
        for i in range(count):
            pid = f"IO{i+1}"
            arrival = i * 2  # Llegan escalonados
            burst = random.randint(1, 5)  # Cortos (I/O bound)
            priority = random.randint(1, 3)
            
            processes.append(Process(pid, arrival, burst, priority))
        
        return processes
    
    @staticmethod
    def generate_cpu_bound_processes(count=3):
        """Genera procesos con características CPU bound"""
        processes = []
        
        for i in range(count):
            pid = f"CPU{i+1}"
            arrival = i  # Llegan casi simultáneos
            burst = random.randint(10, 20)  # Largos (CPU bound)
            priority = random.randint(1, 5)
            
            processes.append(Process(pid, arrival, burst, priority))
        
        return processes