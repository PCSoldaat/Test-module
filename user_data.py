from dataclasses import dataclass

@dataclass
class dims:
    width: int = 500
    height: int = 1000

@dataclass
class forces:
    description: list
    normal: list        
    bending: list        