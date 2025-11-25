#!/usr/bin/env python3
"""
Simulador de Algoritmos de Planificación de CPU
Materia: Sistemas Operativos
Profesor: Ing. Gustavo Lara Jr.
Universidad Católica Andrés Bello
"""
import os
import sys

# Agregar el directorio actual al path para imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Core.scheduler import Scheduler
from UI.interface import Interface

def main():
    """Función principal del simulador"""
    print("=" * 60)
    print("    SIMULADOR DE ALGORITMOS DE PLANIFICACIÓN DE CPU")
    print("=" * 60)
    print("Universidad Católica Andrés Bello - Sistemas Operativos")
    print("Profesor: Ing. Gustavo Lara Jr.")
    print()
    
    # Verificar que existan las carpetas necesarias
    required_dirs = ['casos_prueba']
    for dir_name in required_dirs:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print(f"✓ Creando carpeta '{dir_name}'")
    
    try:
        # Inicializar componentes
        scheduler = Scheduler()
        interface = Interface(scheduler)
        
        # Ejecutar interfaz principal
        interface.main_menu()
        
    except KeyboardInterrupt:
        print("\n\n¡Simulador terminado por el usuario!")
    except Exception as e:
        print(f"\n✗ Error inesperado: {e}")
        print("Por favor, verifique la configuración del proyecto.")

if __name__ == "__main__":
    main()