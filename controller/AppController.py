from model.Aspirante import Aspirante
from model.DatosPersonales import DatosPersonales


class AppController:
    def __init__(self) -> None:
        super().__init__()
        self.dic_aspirantes = {}

    def agregar_aspirante(self, aspirante_obj):
        # Agrega aspirante al diccionario de aspirantes
        self.dic_aspirantes[aspirante_obj.documento] = aspirante_obj