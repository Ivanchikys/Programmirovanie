import math


def isPointInRegion(x, y, N=None, R=None, center = (0, 0)):
    if N:
        return abs(x) <= N / 2 and abs(y) <= N / 2                         #квадрату со стороной N с «центром» в начале координат 
    elif R:
        cx, cy = center
        distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)                #кругу радиусом R и центром в начале координат
        return distance <= R
    else:
        return False


points = [
    {'x': 2, 'y': 0, 'inRegion': 'unknown'},
    {'x': -3, 'y': 4, 'inRegion': 'unknown'},
    {'x': 5, 'y': 3, 'inRegion': 'unknown'},
    {'x': 0, 'y': 7, 'inRegion': 'unknown'},
    {'x': -6, 'y': 0, 'inRegion': 'unknown'}
]

for point in points:
    x = point['x']
    y = point['y']
    point['inRegion'] = isPointInRegion(x, y)
    print(point)