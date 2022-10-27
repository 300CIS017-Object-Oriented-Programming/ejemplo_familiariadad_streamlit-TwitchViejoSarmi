class DatosPersonales:

   def __init__(self, hobbies, nucleo_familiar,tiene_mascotas):
        self.hobbies = hobbies
        self.nucleo_familiar = nucleo_familiar
        self.tiene_mascotas = tiene_mascotas


   def __str__(self):
        return f"{self.hobbies} {self.nucleo_familiar} {self.tiene_mascotas}"