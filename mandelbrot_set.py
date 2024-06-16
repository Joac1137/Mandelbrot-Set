from dataclasses import dataclass

@dataclass
class MandelbrotSet:
    max_iterations: int 


    def __contains__(self, c: complex) -> bool:
        return self.stability(c) == 1

    def stability(self, c: complex) -> float:
        return self.escape_count(c) / self.max_iterations
    
    def escape_count(self, c: complex) -> int:
        z = 0
        for iterations in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) > 2:
                return iterations
        return self.max_iterations