### DEFINICIÓN DE LA CLASE ANIMAL ###

class Animal:
    def __init__(self, nombre_animal: str, pelo: float, plumas: float, tomaLeche: float, esqueleto: float, acuático: float,
                 predador: float, dientes: float, columnaVertebral: float, respira: float, venenoso: float,
                  piernas: float, cola: float, domestico: float, tamañoMedio: float, clase: int) -> None:
        self.nombre = nombre_animal
        self.pelo = pelo
        self.plumas = plumas
        self.tomaLeche = tomaLeche
        self.esqueleto = esqueleto
        self.acuatico = acuático
        self.predador = predador
        self.dientes = dientes
        self.columnaVertebral = columnaVertebral
        self.respira = respira
        self.venenoso = venenoso
        self.piernas = piernas
        self.cola = cola
        self.domestico = domestico
        self.tamañoMedio = tamañoMedio
        self.Class = clase
    
    def __repr__(self):
        # Crear un string con todos los atributos y sus valores
        atributos = ', '.join(f"{key}={value!r}" for key, value in self.__dict__.items())
        return f"Animal({atributos})\n"

### FIN DEL PROGRAMA ###