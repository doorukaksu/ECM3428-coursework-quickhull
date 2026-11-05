import pytest
import quickhull

#chosen base test points: (2, 5) and (9, 5)

def test_find_side_of_line(): 

    assert quickhull.find_side_of_line((2, 5), (9,5), (3, 9)) > 0 #left of the line
    
    assert quickhull.find_side_of_line((2, 5), (9,5), (4, 3)) < 0 # right of the line 

    assert quickhull.find_side_of_line((2, 5), (9,5), (3, 5)) == 0 # on the line
    

def test_distance_from_line():

    assert quickhull.distance_from_line((2, 5), (9, 5), (3, 9)) == 4 #above the line

    assert quickhull.distance_from_line((2, 5), (9, 5), (4, 3)) == 2 #below

    assert quickhull.distance_from_line((2, 5), (9, 5), (6, 5)) == 0 #on
