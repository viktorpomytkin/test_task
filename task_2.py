import sys
from decimal import Decimal, getcontext

getcontext().prec = 38


def point_position(cx, cy, a, b, x, y):
    value = ((x - cx) ** 2) / (a ** 2) + ((y - cy) ** 2) / (b ** 2)
    if value == 1:
        return 0
    elif value < 1:
        return 1
    else:
        return 2


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python task_2.py ellipse.txt points.txt")
        sys.exit(1)

    ellipse_file, points_file = sys.argv[1], sys.argv[2]

    with open(ellipse_file, "r") as f:
        cx, cy = map(Decimal, f.readline().split())
        a, b = map(Decimal, f.readline().split())

    with open(points_file, "r") as f:
        points = [tuple(map(Decimal, line.split())) for line in f]

    for px, py in points:
        print(point_position(cx, cy, a, b, px, py))
