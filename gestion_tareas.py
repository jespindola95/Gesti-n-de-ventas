import json
from tarea import Tarea, TareaSimple, TareaRecurrente

class GestionTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def obtener_tarea(self, descripcion):
        for tarea in self.tareas:
            if tarea.descripcion == descripcion:
                return tarea
        return None

    def actualizar_tarea(self, descripcion, fecha_vencimiento=None, estado=None):
        tarea = self.obtener_tarea(descripcion)
        if tarea:
            if fecha_vencimiento is not None:
                tarea.fecha_vencimiento = fecha_vencimiento
            if estado is not None:
                tarea.estado = estado

    def eliminar_tarea(self, descripcion):
        tarea = self.obtener_tarea(descripcion)
        if tarea:
            self.tareas.remove(tarea)

    def listar_tareas(self):
        for tarea in self.tareas:
            print(tarea)

    def guardar_datos(self, filename):
        with open(filename, 'w') as file:
            json.dump([tarea.__dict__ for tarea in self.tareas], file)

    def cargar_datos(self, filename):
        try:
            with open(filename, 'r') as file:
                tareas_data = json.load(file)
                for tarea_data in tareas_data:
                    if 'intervalo' in tarea_data:
                        tarea = TareaRecurrente(**tarea_data)
                    else:
                        tarea = TareaSimple(**tarea_data)
                    self.tareas.append(tarea)
        except FileNotFoundError:
            print("Archivo no encontrado.")