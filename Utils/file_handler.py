"""
Manejo de archivos para cargar y guardar procesos
"""
import json
import csv
import os
from Core.process import Process

class FileHandler:
    """Maneja operaciones de archivo para el simulador"""
    
    @staticmethod
    def load_processes(filename):
        """Carga procesos desde archivo"""
        filepath = filename
        if not os.path.exists(filepath) and not os.path.isabs(filename):
            # Buscar en directorio data/
            filepath = os.path.join("data", filename)
        
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Archivo no encontrado: {filepath}")
        
        _, ext = os.path.splitext(filepath)
        ext = ext.lower()
        
        if ext == '.json':
            return FileHandler._load_json(filepath)
        elif ext in ['.csv', '.txt']:
            return FileHandler._load_csv(filepath)
        else:
            raise ValueError(f"Formato no soportado: {ext}")
    
    @staticmethod
    def _load_json(filepath):
        """Carga procesos desde archivo JSON"""
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        processes = []
        
        if isinstance(data, list):
            for item in data:
                pid = item.get('pid', f"P{len(processes)+1}")
                arrival = int(item.get('arrival_time', 0))
                burst = int(item.get('burst_time', 0))
                priority = int(item.get('priority', 1))
                
                processes.append(Process(pid, arrival, burst, priority))
        
        return processes
    
    @staticmethod
    def _load_csv(filepath):
        """Carga procesos desde archivo CSV/TXT"""
        processes = []
        
        with open(filepath, 'r') as f:
            # Intentar detectar delimitador
            sample = f.read(1024)
            f.seek(0)
            
            delimiter = ',' if ',' in sample else '\t' if '\t' in sample else ' '
            
            reader = csv.reader(f, delimiter=delimiter)
            
            for i, row in enumerate(reader):
                if not row or row[0].startswith('#'):
                    continue  # Saltar líneas vacías o comentarios
                
                try:
                    if len(row) >= 3:
                        pid = row[0].strip()
                        arrival = int(row[1].strip())
                        burst = int(row[2].strip())
                        priority = int(row[3].strip()) if len(row) >= 4 else 1
                        
                        processes.append(Process(pid, arrival, burst, priority))
                except (ValueError, IndexError):
                    print(f"Advertencia: Línea {i+1} ignorada - formato incorrecto")
        
        return processes
    
    @staticmethod
    def save_processes(processes, filename):
        """Guarda procesos en archivo"""
        filepath = filename
        if not os.path.isabs(filename):
            filepath = os.path.join("data", filename)
        
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        _, ext = os.path.splitext(filepath)
        ext = ext.lower()
        
        if ext == '.json':
            FileHandler._save_json(processes, filepath)
        elif ext in ['.csv', '.txt']:
            FileHandler._save_csv(processes, filepath)
        else:
            # Por defecto, usar JSON
            if '.' not in filename:
                filepath += '.json'
                FileHandler._save_json(processes, filepath)
    
    @staticmethod
    def _save_json(processes, filepath):
        """Guarda procesos en archivo JSON"""
        data = []
        for p in processes:
            data.append({
                'pid': p.pid,
                'arrival_time': p.arrival_time,
                'burst_time': p.burst_time,
                'priority': p.priority
            })
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    @staticmethod
    def _save_csv(processes, filepath):
        """Guarda procesos en archivo CSV"""
        with open(filepath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['PID', 'Arrival_Time', 'Burst_Time', 'Priority'])
            
            for p in processes:
                writer.writerow([p.pid, p.arrival_time, p.burst_time, p.priority])