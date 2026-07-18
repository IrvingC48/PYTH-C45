#Caso: Recorre una lista de tareas con for y, 
# para cada tarea usa while para reintentos con backoff exponencial, 
# manejo de excepciones y estadísticas de ejecución.

import time
import random

tasks = [
    {"id" : 1, "name" : "Enviar correo", "success_rate": 0.7, "is_active" : True},
    {"id" : 2, "name" : "Generar reporte", "success_rate": 0.5, "is_active" : True},
    {"id" : 3, "name" : "Subir archivo", "success_rate": 0.3, "is_active" : False},
    {"id" : 4, "name" : "Leer archivo", "success_rate": 0.1, "is_active" : True},
]

max_retries = 4
summary = {"processed" : 0, "failed" : 0, "attempts" : []}

for task in tasks:
    attempt = 0
    backoff = 1.0 #Tiempo inicial de espera en segundos
    success = False

    if not task["is_active"]:
        print(f'Tarea {task["id"]} {task["name"]} esta inactiva, omitiendo...')
        continue

    #Reintentos controlados por while
    while attempt <= max_retries:
        attempt += 1
        try:
            #Simular procesamiento con probabilidad de éxito
            if random.random() < task["success_rate"]:
                success = True
                print(f'Tarea {task["id"]} {task["name"]} completada en intento {attempt}.')
                break
            else:
                print(f'Tarea {task["id"]} {task["name"]} fallo en intento {attempt}, reintentando...')
                if attempt <= max_retries:
                    time.sleep(backoff)
                    backoff *= 2 #Incremento exponencial del tiempo de espera
        except Exception as e:
            print(f'Error inesperado en tarea {task["id"]} : {e}')
            if attempt <= max_retries:
                time.sleep(backoff)
                backoff *= 2 #Incremento exponencial del tiempo de espera

    summary['attempts'].append({"task_id" : task["id"], "attempts" : attempt, "success" : success})
    if success:
        summary["processed"] += 1
    else:
        summary["failed"] += 1

print(f'Resumen: {summary}')