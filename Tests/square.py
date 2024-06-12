class Square:
    def __init__(self, height: float):
        self.height = height

    def calc_area(self) -> float:
        return self.height ** 2
    
    def calc_perimeter(self) -> float:
        return self.height * 4