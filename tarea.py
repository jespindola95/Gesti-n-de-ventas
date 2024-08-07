class Tarea:
    def __init__(self, descripcion, fecha_vencimiento, estado):
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado

    def __str__(self):
        return f"Tarea(descripcion={self.descripcion}, fecha_vencimiento={self.fecha_vencimiento}, estado={self.estado})"

class TareaSimple(Tarea):
    def __init__(self, descripcion, fecha_vencimiento, estado):
        super().__init__(descripcion, fecha_vencimiento, estado)

class TareaRecurrente(Tarea):
    def __init__(self, descripcion, fecha_vencimiento, estado, intervalo):
        super().__init__(descripcion, fecha_vencimiento, estado)
        self.intervalo = intervalo

    def __str__(self):
        return f"TareaRecurrente(descripcion={self.descripcion}, fecha_vencimiento={self.fecha_vencimiento}, estado={self.estado}, intervalo={self.intervalo})"