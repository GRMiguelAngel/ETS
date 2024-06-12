class Triangle:
    def __init__(self, side: float | int):
        self.side = side

    def calc_area(self) -> float | int:
        return ((3)**0.5 / 4) * self.side
    
    def calc_perimeter(self) -> float | int:
        return self.side * 3