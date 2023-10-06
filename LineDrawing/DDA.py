from typing import Tuple, List
from LineDrawing.LineDrawingStrategy import LineDrawingStrategy


class DDALineDrawing(LineDrawingStrategy):
    @staticmethod
    def draw(startPoint: Tuple[int, int], endPoint: Tuple[int, int]) -> List[Tuple[int, int]]:
        x1, y1 = startPoint
        x2, y2 = endPoint
        points = []

        if x1 == x2:
            # Vertical Line
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                points.append((x1, y))
            return points
        else:
            slope = (y2 - y1) / (x2 - x1)
            if slope > 1 or slope < -1:
                # y increases faster than x
                if y1 > y2:
                    y1, y2 = y2, y1
                    x1, x2 = x2, x1
                x = x1
                for y in range(y1, y2 + 1):
                    points.append((x, round(y)))
                    x += (1 / slope)
            else:
                # x increases faster than y
                if x1 > x2:
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
                y = y1
                for x in range(x1, x2 + 1):
                    points.append((x, round(y)))
                    y += slope
        return points
