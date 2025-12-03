"""
Script para crear automáticamente los archivos de datos de prueba
"""
import os
import json
import csv

def crear_carpeta_data():
    """Crea la carpeta data si no existe"""
    if not os.path.exists("data"):
        os.makedirs("data")
        print("✅ Carpeta 'data' creada")
    else:
        print("📁 Carpeta 'data' ya existe")

def crear_archivos_json():
    """Crea los archivos JSON"""
    
    # Conjunto 1: Procesos Básicos
    conjunto1 = [
        {"pid": "P1", "arrival_time": 0, "burst_time": 8, "priority": 3},
        {"pid": "P2", "arrival_time": 1, "burst_time": 4, "priority": 1},
        {"pid": "P3", "arrival_time": 2, "burst_time": 9, "priority": 4},
        {"pid": "P4", "arrival_time": 3, "burst_time": 5, "priority": 2}
    ]
    
    # Conjunto 2: Procesos Variados
    conjunto2 = [
        {"pid": "P1", "arrival_time": 0, "burst_time": 10, "priority": 2},
        {"pid": "P2", "arrival_time": 2, "burst_time": 3, "priority": 1},
        {"pid": "P3", "arrival_time": 4, "burst_time": 6, "priority": 3},
        {"pid": "P4", "arrival_time": 6, "burst_time": 1, "priority": 1},
        {"pid": "P5", "arrival_time": 8, "burst_time": 4, "priority": 2}
    ]
    
    # Conjunto 3: Caso Personal
    conjunto3 = [
        {"pid": "P1", "arrival_time": 0, "burst_time": 7, "priority": 1},
        {"pid": "P2", "arrival_time": 2, "burst_time": 4, "priority": 3},
        {"pid": "P3", "arrival_time": 3, "burst_time": 9, "priority": 2},
        {"pid": "P4", "arrival_time": 5, "burst_time": 5, "priority": 1},
        {"pid": "P5", "arrival_time": 6, "burst_time": 3, "priority": 4},
        {"pid": "P6", "arrival_time": 8, "burst_time": 6, "priority": 2}
    ]
    
    # Procesos Mixtos
    procesos_mixtos = [
        {"pid": "A1", "arrival_time": 0, "burst_time": 5, "priority": 1},
        {"pid": "A2", "arrival_time": 1, "burst_time": 3, "priority": 2},
        {"pid": "A3", "arrival_time": 2, "burst_time": 8, "priority": 3},
        {"pid": "A4", "arrival_time": 3, "burst_time": 6, "priority": 1},
        {"pid": "A5", "arrival_time": 4, "burst_time": 4, "priority": 4},
        {"pid": "A6", "arrival_time": 5, "burst_time": 7, "priority": 2},
        {"pid": "A7", "arrival_time": 6, "burst_time": 2, "priority": 1},
        {"pid": "A8", "arrival_time": 7, "burst_time": 9, "priority": 3}
    ]
    
    # Procesos Cortos para RR
    procesos_cortos = [
        {"pid": "S1", "arrival_time": 0, "burst_time": 2, "priority": 1},
        {"pid": "S2", "arrival_time": 1, "burst_time": 1, "priority": 2},
        {"pid": "S3", "arrival_time": 2, "burst_time": 3, "priority": 1},
        {"pid": "S4", "arrival_time": 3, "burst_time": 2, "priority": 3},
        {"pid": "S5", "arrival_time": 4, "burst_time": 1, "priority": 2}
    ]
    
    archivos_json = {
        "conjunto1.json": conjunto1,
        "conjunto2.json": conjunto2,
        "conjunto3.json": conjunto3,
        "procesos_mixtos.json": procesos_mixtos,
        "procesos_cortos.json": procesos_cortos
    }
    
    for nombre, datos in archivos_json.items():
        ruta = os.path.join("data", nombre)
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        print(f"✅ {nombre} creado ({len(datos)} procesos)")

def crear_archivos_csv():
    """Crea los archivos CSV"""
    
    # Datos para CSV
    datos_csv = {
        "conjunto1.csv": [
            ["PID", "Arrival_Time", "Burst_Time", "Priority"],
            ["P1", 0, 8, 3],
            ["P2", 1, 4, 1],
            ["P3", 2, 9, 4],
            ["P4", 3, 5, 2]
        ],
        "conjunto2.csv": [
            ["PID", "Arrival_Time", "Burst_Time", "Priority"],
            ["P1", 0, 10, 2],
            ["P2", 2, 3, 1],
            ["P3", 4, 6, 3],
            ["P4", 6, 1, 1],
            ["P5", 8, 4, 2]
        ],
        "conjunto3.csv": [
            ["PID", "Arrival_Time", "Burst_Time", "Priority"],
            ["P1", 0, 7, 1],
            ["P2", 2, 4, 3],
            ["P3", 3, 9, 2],
            ["P4", 5, 5, 1],
            ["P5", 6, 3, 4],
            ["P6", 8, 6, 2]
        ]
    }
    
    for nombre, filas in datos_csv.items():
        ruta = os.path.join("data", nombre)
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(filas)
        print(f"✅ {nombre} creado ({len(filas)-1} procesos)")

def crear_archivos_txt():
    """Crea los archivos de texto plano"""
    
    conjunto1_txt = """# Conjunto 1: Procesos Básicos
# PID   Llegada   Ráfaga   Prioridad
P1      0         8        3
P2      1         4        1
P3      2         9        4
P4      3         5        2"""
    
    conjunto2_txt = """# Conjunto 2: Procesos Variados
# PID   Llegada   Ráfaga   Prioridad
P1      0         10       2
P2      2         3        1
P3      4         6        3
P4      6         1        1
P5      8         4        2"""
    
    archivos_txt = {
        "conjunto1.txt": conjunto1_txt,
        "conjunto2.txt": conjunto2_txt
    }
    
    for nombre, contenido in archivos_txt.items():
        ruta = os.path.join("data", nombre)
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"✅ {nombre} creado")

def main():
    """Función principal"""
    print("="*60)
    print("CREANDO ARCHIVOS DE DATOS PARA EL SIMULADOR")
    print("="*60)
    
    crear_carpeta_data()
    crear_archivos_json()
    crear_archivos_csv()
    crear_archivos_txt()
    
    print("\n" + "="*60)
    print("✅ TODOS LOS ARCHIVOS CREADOS EXITOSAMENTE")
    print("="*60)
    print("\n📁 Estructura creada en carpeta 'data/':")
    print("├── conjunto1.json/csv/txt")
    print("├── conjunto2.json/csv/txt")
    print("├── conjunto3.json/csv")
    print("├── procesos_mixtos.json")
    print("└── procesos_cortos.json")
    print("\n🚀 Ejecuta el simulador con: python run.py")

if __name__ == "__main__":
    main()