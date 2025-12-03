"""
Clase/estructura de proceso (PCB - Process Control Block)
"""
class Process:
    """Representa un proceso en el sistema"""
    
    def __init__(self, pid, arrival_time, burst_time, priority=1):
        # Atributos obligatorios del enunciado
        self.pid = pid                    # ID único del proceso
        self.arrival_time = arrival_time  # Tiempo de llegada
        self.burst_time = burst_time      # Tiempo de ráfaga de CPU
        self.priority = priority          # Prioridad (para algoritmos que la requieran)
        self.state = "NEW"                # Estado actual: NEW, READY, RUNNING, TERMINATED
        
        # Atributos para cálculo de métricas
        self.remaining_time = burst_time  # Para algoritmos apropiativos
        self.start_time = None           # Cuando comienza a ejecutar por primera vez
        self.completion_time = None      # Cuando termina completamente
        self.waiting_time = 0            # Tiempo total de espera
        self.response_time = None        # Tiempo hasta primera ejecución
        self.turnaround_time = None      # Tiempo de retorno total
        
        # Historial del proceso
        self.execution_history = []      # Registro de ejecuciones
        
    def __str__(self):
        return f"Process(PID={self.pid}, Arrival={self.arrival_time}, " \
               f"Burst={self.burst_time}, Priority={self.priority}, State={self.state})"
    
    def __repr__(self):
        return self.__str__()
    
    def execute(self, time_units, current_time):
        """Ejecuta el proceso por un número específico de unidades de tiempo"""
        if self.state == "NEW":
            self.state = "RUNNING"
            self.start_time = current_time
            self.response_time = current_time - self.arrival_time
        
        if self.remaining_time <= time_units:
            # Proceso termina en esta ejecución
            executed = self.remaining_time
            self.remaining_time = 0
            self.state = "TERMINATED"
            self.completion_time = current_time + executed
        else:
            # Proceso continúa
            executed = time_units
            self.remaining_time -= time_units
            self.state = "READY"
        
        # Registrar ejecución
        self.execution_history.append({
            "start": current_time,
            "end": current_time + executed,
            "units": executed
        })
        
        return executed
    
    def is_completed(self):
        """Verifica si el proceso ha terminado"""
        return self.remaining_time == 0
    
    def calculate_waiting_time(self):
        """Calcula el tiempo de espera del proceso"""
        if self.completion_time is not None:
            self.turnaround_time = self.completion_time - self.arrival_time
            self.waiting_time = self.turnaround_time - self.burst_time
        return self.waiting_time