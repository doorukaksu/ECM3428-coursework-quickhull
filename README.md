# ECM3428-coursework-quickhull
GEOSPATIAL BOUNDARY MAPPER TO AID CONTAINING FOREST FIRES
Chosen Algorithm: Quickhull

## Motivation and Usecases

The product is for use by emergency responders to be able to contain a forest fire quickly and effectively.

As it stands it is difficult to visualise the most effective way to contain a forest fire without sacrificing a portion of the forest, which with this algorithm is minimised significantly.

The algorithm uses fire sensors scattered throughout the forest to identify which 'chunks' of the forest is affected by the fire. These sensors report their coordinates, which are then used to find the minimum area required to contain all of the fire.

## Complexities

| Case                              | Time       | Space |
|-----------------------------------|------------|-------|
| Best / average (balanced splits)  | O(n log n) | O(n)  |
| Worst (unbalanced splits)         | O(n²)      | O(n²) |

## Live link
https://ecm3428-live.vercel.app/

## How to use
Click the live link above to be taken straight to the live domain where the app is deployed.

To use the forest fire board, simply click any multiple points on the forest to start a fire and observe the quickhull algorithm calculating the smallest containment area.

To see prepared scenarios, click on the desired scenario on the right or generate a number of random points using the random point generator.

## Local Installation

```bash
git clone https://github.com/doorukaksu/ECM3428-coursework-quickhull.git
cd ECM3428-coursework-quickhull
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Local Usage

```bash
python run.py
```

'run.py' creates the Flask app from the 'app' package and starts it. Open the address printed in the terminal, which is usually `http://127.0.0.1:5000`.

## Testing

test_quickhull.py is dedicated for testing the functions written in quickhull.py . A number of cases are tested for each function:

1. test_find_side_of_line() : Tests the find_side_of_line() function, which determines the position of a point relative to a directed line.

Three cases are tested:
- A point above the horizontal line, which should return a positive value (left side).
- A point below the line, which should return a negative value (right side).
- A point directly on the line, which should return zero.
This verifies that the function correctly identifies all three possible point positions.



2. test_distance_from_line() : Tests the distance_from_line() function, which calculates the perpendicular distance between a point and a line.

Three cases are tested:
- A point above the line with an expected distance of 4.
- A point below the line with an expected distance of 2.
- A point directly on the line with an expected distance of 0.
This checks that the function returns positive distances regardless of which side of the line the point occupies, and correctly handles points lying on the line.



3. test_polygon_area() : Tests the polygon_area() function using rectangles and triangles.

Four cases are tested:
- A rectangle with an area of 12.
- A triangle with an area of 6.
- An alternative rectangle with translated coordinates, also having an area of 12.
- An alternative triangle with translated coordinates, also having an area of 6.
The alternative shapes verify that translating a polygon does not affect its calculated area.



4. test_perimeter_of_polygon() : Tests the perimeter() function by calculating the total boundary length of rectangles and triangles.

Four cases are tested:
- A rectangle with an expected perimeter of 14.
- A triangle with an expected perimeter of 12.
- An alternative rectangle with an expected perimeter of 14.
- An alternative triangle with an expected perimeter of 12.
This verifies that the function correctly sums the distances between consecutive vertices, including the final edge connecting the last vertex back to the first.



5. test_find_hull() : Tests the recursive find_hull() function, which identifies the points forming part of the convex hull between two endpoints.

Three cases are tested:
- An empty list of points, which should return an empty list.
- A single point, which should be returned as the hull.
- A collection of four points, where the algorithm should identify the three outer points and exclude the interior point.
The empty-list case checks an important edge condition, while the final case verifies that the recursive algorithm correctly identifies the farthest points and excludes points that do not contribute to the hull.



6. test_quickhull() : Tests the main quickhull() function, which constructs the complete convex hull from a collection of input points.

Three cases are tested:
- A set containing only two points, verifying that small input sets are handled correctly.
- A collection of five points, where the algorithm should identify the four outer vertices and exclude the interior point.
- A similar collection containing a duplicate point, verifying that duplicate coordinates are removed without affecting the resulting convex hull.
The final case is particularly useful for checking how the algorithm handles duplicate input coordinates.


# Outcome Summary
All test functions passed successfully when executed using pytest, which indicates that the tested geometric helper functions, polygon calculations, recursive hull construction and the main Quickhull implementation produced the expected results across the selected test cases. The tests also covered several edge cases such as empty input, single-point input, duplicate coordinates and points lying directly on a line.

## Contributions

Backend - Doruk & Siddhant
FrontEnd - Doruk
API - Doruk
Testing - Siddhant
ReadME - Doruk & Siddhant

