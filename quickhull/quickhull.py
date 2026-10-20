"""
Functions TO DO:
    - which side a line point p is on (returns >0 if point is to the left of line <0 if to the right of line and =0 if on the line)     >    USE VECTOR CROSS PRODUCT 
    - how far is point p from the line (returns absolute value of distance)    >    ^^^^^^^^^^^^^^^^^^^^^^^^
    
    - recursive find hull
    - main quickhull function to act as main entry point 
"""
import math

def find_side_of_line(p1, p2, p3):    
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - ((p2[1] - p1[1]) * (p3[0] - p1[0])) #to remember (can be removed later): area of the parallelogram formed

def distance_from_line(p1, p2, p3):

    side = find_side_of_line(p1, p2, p3)

    if side < 0:
        side = side * -1

     return side/math.dist(p1, p2)

def polygon_area(polygon):
    n = len(polygon)
    area = 0.0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def perimeter(polygon):
# Finds perimeter of polygon    
    total = 0
    for i in range(len(polygon)):
        next = (i +1) % len(polygon)
        total += math.dist(polygon[i], polygon[next])
    return total

def find_hull(points, p1, p2):
    return

def quickhull(points):
    return
