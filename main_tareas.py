from gestion_tareas import GestionTareas
from tarea import TareaSimple, TareaRecurrente

def main():
    gestion_tareas = GestionTareas()

    while True:
        print("\n1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Actualizar tarea")
        print("4. Eliminar tarea")
        print("5. Guardar datos")
        print("6. Cargar datos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                tipo = input("Tipo de tarea (simple/recurrente): ")
                descripcion = input("Descripción: ")
                fecha_vencimiento = input("Fecha de vencimiento: ")
                estado = input("Estado (pendiente/en progreso/completada): ")

                if tipo == 'simple':
                    tarea = TareaSimple(descripcion, fecha_vencimiento, estado)
                elif tipo == 'recurrente':
                    intervalo = input("Intervalo de recurrencia: ")
                    tarea = TareaRecurrente(descripcion, fecha_vencimiento, estado, intervalo)
                else:
                    print("Tipo de tarea no válido.")
                    continue

                gestion_tareas.agregar_tarea(tarea)

            elif opcion == '2':
                gestion_tareas.listar_tareas()

            elif opcion == '3':
                descripcion = input("Descripción de la tarea a actualizar: ")
                fecha_vencimiento = input("Nueva fecha de vencimiento (presione enter para dejar igual): ")
                estado = input("Nuevo estado (presione enter para dejar igual): ")

                gestion_tareas.actualizar_tarea(
                    descripcion,
                    fecha_vencimiento=fecha_vencimiento if fecha_vencimiento else None,
                    estado=estado if estado else None
                )

            elif opcion == '4':
                descripcion = input("Descripción de la tarea a eliminar: ")
                gestion_tareas.eliminar_tarea(descripcion)

            elif opcion == '5':
                filename = input("Nombre del archivo para guardar: ")
                gestion_tareas.guardar_datos(filename)

            elif opcion == '6':
                filename = input("Nombre del archivo para cargar: ")
                gestion_tareas.cargar_datos(filename)

            elif opcion == '7':
                break

            else:
                print("Opción no válida. Por favor, intente de nuevo.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()