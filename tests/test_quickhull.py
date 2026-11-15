import pytest
import math
import random
import time
from quickhull import quickhull

def test_find_side_of_line(): 

    assert quickhull.find_side_of_line((2, 5), (9,5), (3, 9)) > 0 #left of the line
    
    assert quickhull.find_side_of_line((2, 5), (9,5), (4, 3)) < 0 # right of the line 

    assert quickhull.find_side_of_line((2, 5), (9,5), (3, 5)) == 0 # on the line
    

def test_distance_from_line():

    assert quickhull.distance_from_line((2, 5), (9, 5), (3, 9)) == 4 #above the line

    assert quickhull.distance_from_line((2, 5), (9, 5), (4, 3)) == 2 #below

    assert quickhull.distance_from_line((2, 5), (9, 5), (6, 5)) == 0 #on

def test_polygon_area():

    rectangle = [(0,0), (0,3), (4,3), (4,0)]

    triangle = [(0,0), (0,3), (4,3)]

    rectangle_alt = [(10, 10), (14, 10), (14, 13), (10, 13)]

    triangle_alt = [(10, 10), (14, 10), (14, 13)]

    assert quickhull.polygon_area(rectangle) == 12

    assert quickhull.polygon_area(triangle) == 6

    assert quickhull.polygon_area(rectangle_alt) == 12

    assert quickhull.polygon_area(triangle_alt) == 6


def test_perimeter_of_polygon():

  rectangle = [(0,0), (0,3), (4,3), (4,0)]
  
  triangle = [(0,0), (0,3), (4,3)]
  
  rectangle_alt = [(10, 10), (14, 10), (14, 13), (10, 13)]
  
  triangle_alt = [(10, 10), (14, 10), (14, 13)]
  
  assert quickhull.perimeter(rectangle) == 14
  
  assert quickhull.perimeter(triangle) == 12
  
  assert quickhull.perimeter(rectangle_alt) == 14

  assert quickhull.perimeter(triangle_alt) == 12


def test_find_hull():

    assert quickhull.find_hull([], (0, 0), (10, 0)) == []

    assert quickhull.find_hull([(5, -4)], (0, 0), (10, 0)) == [(5, -4)]

    assert quickhull.find_hull( [(2, -3), (5, -4), (8, -3), (5, -1)], (0, 0), (10, 0),) == [(2, -3), (5, -4), (8, -3)]

def test_quickhull():

    assert quickhull.quickhull([(2,4), (1, 3)]) == [(1,3), (2, 4)]

    assert quickhull.quickhull([(0, 0), (4, -1), (6, 0), (3, 2), (3, 0)]) == [(0, 0), (4, -1), (6, 0), (3, 2)]

    assert quickhull.quickhull([(0, 0), (0, 0), (4, -1), (6, 0), (3, 2)]) == [(0, 0), (4, -1), (6, 0), (3, 2)]

def test_tied_farthest_points():

    points = [(0, 0), (10, 0), (4, 5), (5, 5), (6, 5)]

    assert set(quickhull.quickhull(points)) == {(0, 0), (10, 0), (6, 5), (4, 5)}


def test_negative_coordinates_and_input_order():

    points = [(-5, -5), (5, -5), (5, 5), (-5, 5), (0, 0), (-1, 2)]

    shuffled = points[::-1]

    assert set(quickhull.quickhull(points)) == {(-5, -5), (5, -5), (5, 5), (-5, 5)}

    assert quickhull.quickhull(points) == quickhull.quickhull(shuffled) 

def test_empty_and_single_point():

    assert quickhull.quickhull([]) == []

    assert quickhull.quickhull([(3, 4)]) == [(3, 4)]

    assert quickhull.quickhull([(3, 4), (3, 4), (3, 4)]) == [(3, 4)] 


def test_collinear_points():

    horizontal = [(0, 0), (1, 0), (2, 0), (3, 0)]

    vertical = [(5, 0), (5, 7), (5, 2), (5, 9)]

    diagonal = [(k, 2 * k + 1) for k in range(10)]

    assert set(quickhull.quickhull(horizontal)) == {(0, 0), (3, 0)} 

    assert set(quickhull.quickhull(vertical)) == {(5, 0), (5, 9)}

    assert set(quickhull.quickhull(diagonal)) == {(0, 1), (9, 19)}

    assert quickhull.polygon_area(quickhull.quickhull(diagonal)) == 0


def test_points_on_edges_are_not_vertices():

    corners = [(0, 0), (10, 0), (10, 10), (0, 10)]
    on_edges = [(5, 0), (10, 5), (5, 10), (0, 5)]
    inside = [(5, 5), (1, 1), (9, 2)]
    hull = quickhull.quickhull(corners + on_edges + inside)

    assert set(hull) == set(corners)
    assert quickhull.polygon_area(hull) == 100
    assert quickhull.perimeter(hull) == 40



def test_large_dataset():

    rng = random.Random(42)
    points = [(rng.uniform(0, 100), rng.uniform(0, 100)) for _ in range(50000)]
    start = time.perf_counter()
    hull = quickhull.quickhull(points)
    elapsed = time.perf_counter() - start

    assert len(hull) >= 3 and set(hull) <= set(points)
    