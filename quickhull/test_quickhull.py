import pytest
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

