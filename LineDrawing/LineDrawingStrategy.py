from typing import List, Tuple
from abc import ABC, abstractmethod


class LineDrawingStrategy(ABC):
    @staticmethod
    @abstractmethod
    def draw(startPoint: Tuple[int, int], endPoint: Tuple[int, int]) -> List[Tuple[int, int]]:
        pass
