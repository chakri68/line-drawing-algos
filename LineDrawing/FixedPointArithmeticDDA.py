from typing import Tuple, List
from LineDrawing.LineDrawingStrategy import LineDrawingStrategy


class FixedPointArithmeticDDA(LineDrawingStrategy):
    @staticmethod
    def draw(startPoint: Tuple[int, int], endPoint: Tuple[int, int]) -> List[Tuple[int, int]]:
        q_factor = 2
        x1, y1 = (point << q_factor for point in startPoint)
        x2, y2 = (point << q_factor for point in endPoint)
        points = []

        if x1 == x2:
            # Vertical Line
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1 >> q_factor, (y2 >> q_factor) + 1):
                points.append((x1 >> q_factor, y >> q_factor))
            return points
        else:
            slope = int(((y2 - y1) << q_factor) / (x2 - x1))
            if slope > (1 << q_factor) or slope < -(1 << q_factor):
                # y increases faster than x
                if y1 > y2:
                    y1, y2 = y2, y1
                    x1, x2 = x2, x1
                x = x1
                for y in range(y1, y2 + 1, 1 << q_factor):
                    points.append((x >> q_factor, y >> q_factor))
                    x += int((1 << q_factor * 2) / slope)
            else:
                # x increases faster than y
                if x1 > x2:
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
                y = y1
                for x in range(x1, x2 + 1, 1 << q_factor):
                    points.append((x >> q_factor, y >> q_factor))
                    y += slope
        return points
