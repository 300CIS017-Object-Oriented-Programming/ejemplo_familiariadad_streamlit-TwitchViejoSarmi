class Aspirante:

    def __init__(self, nombre_completo, documento, fecha_entrevista, periodo, observaciones, datos_personales_obj):
        self.nombre_completo = nombre_completo
        self.documento = documento
        self.fecha_entrevista = fecha_entrevista
        self.periodo = periodo
        self.observaciones = observaciones
        self.datos_personales = datos_personales_obj

    def __str__(self) -> str:
        return f"*{self.nombre_completo}*: {self.documento} {self.fecha_entrevista}\n * periodo: {self.periodo}\n"

