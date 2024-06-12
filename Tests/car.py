class Coche:
    def __init__(self, marca: str, modelo: str, color: str, cilindrada: float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cilindrada = cilindrada
        self.car_status = False
        self.speeding_up = False

    def acelerar(self) -> bool:
        if not self.speeding_up:
            self.speeding_up = True
        return self.speeding_up
    
    def frenar(self) -> bool:
        if self.speeding_up:
            self.speeding_up = False
        return self.speeding_up