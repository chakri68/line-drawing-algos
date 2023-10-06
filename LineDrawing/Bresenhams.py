from typing import Tuple, List
from LineDrawing.LineDrawingStrategy import LineDrawingStrategy


class BresenhamLineDrawing(LineDrawingStrategy):
    @staticmethod
    def draw(startPoint: Tuple[int, int], endPoint: Tuple[int, int]) -> List[Tuple[int, int]]:
        x1, y1 = startPoint
        x2, y2 = endPoint

        rise: int = y2 - y1
        run: int = x2 - x1

        slopeIsNegative: bool = (rise < 0) ^ (run < 0)
        points: List[Tuple[int, int]] = []

        if (abs(run) > abs(rise)):
            # x increases faster than y
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            y = y1
            pk: int = 2 * rise - run  # magic formula
            for x in range(x2, x2 + 1):
                if pk <= 0:
                    # Select yk since dl < du
                    points.append((x, y))
                    pk += 2 * rise
                else:
                    if slopeIsNegative:
                        y -= 1
                    else:
                        y += 1
                    points.append((x, y))
                    pk += (2 * rise) - (2 * run)
        else:
            # y increases faster than x
            if y1 > y2:
                y1, y2 = y2, y1
                x1, x2 = x2, x1

            x = x1
            pk: int = 2 * run - rise  # magic formula
            for y in range(y1, y2 + 1):
                if pk <= 0:
                    points.append((x, y))
                    pk += 2 * run
                else:
                    if slopeIsNegative:
                        x -= 1
                    else:
                        x += 1
                    points.append((x, y))
                    pk += (2 * run) - (2 * rise)

        return points
