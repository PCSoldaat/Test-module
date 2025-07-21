from dataclasses import dataclass
from functools import cached_property

@dataclass
class dims:
    width: int
    height: int
    
    @cached_property
    def area(self):
        return self.width * self.height
    
    @cached_property
    def perimeter(self):
        return (self.width + self.height) * 2
    
    @cached_property
    def section_modulus(self):
        return 1/6 * self.width * self.height ** 2
    
@dataclass
class stress:
    force: float 
    area: float 
    moment: float 
    section_modulus: float 
    
    @cached_property
    def normal(self):
        return self.force / self.area
    
    @cached_property
    def bending(self):
        return self.moment / self.section_modulus
