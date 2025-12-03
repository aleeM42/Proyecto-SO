"""
Motor principal de planificación de CPU
Clase base para todos los algoritmos de planificación
"""
from Core.process import Process
from Core.metrics import MetricsCalculator

class Scheduler:
    """Clase base abstracta para planificadores de CPU"""
    
    def __init__(self, name: str = "Scheduler"):
        self.name = name
        self.processes = []
        self.completed_processes = []
        self.current_time = 0
        self.gantt_chart = []
        self.metrics_calculator = MetricsCalculator()
    
    def add_process(self, process: Process):
        """Agrega un proceso al planificador"""
        self.processes.append(process)
    
    def add_processes(self, processes):
        """Agrega múltiples procesos al planificador"""
        self.processes.extend(processes)
    
    def sort_by_arrival_time(self):
        """Ordena procesos por tiempo de llegada"""
        self.processes.sort(key=lambda p: p.arrival_time)
    
    def run(self):
        """Método abstracto para ejecutar la planificación"""
        raise NotImplementedError("Subclases deben implementar run()")
    
    def calculate_metrics(self):
        """Calcula métricas después de la simulación"""
        return self.metrics_calculator.calculate_all(self.completed_processes)
    
    def reset(self):
        """Reinicia el estado del planificador"""
        self.processes = []
        self.completed_processes = []
        self.current_time = 0
        self.gantt_chart = []
    
    def get_gantt_chart(self):
        """Retorna el diagrama de Gantt de la simulación"""
        return self.gantt_chart
    
    def update_gantt(self, process_id, start_time, end_time):
        """Actualiza el diagrama de Gantt"""
        self.gantt_chart.append({
            "process_id": process_id,
            "start": start_time,
            "end": end_time,
            "duration": end_time - start_time
        })