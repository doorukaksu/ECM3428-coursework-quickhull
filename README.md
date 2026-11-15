# ECM3428-coursework-quickhull
GEOSPATIAL BOUNDARY MAPPER TO AID CONTAINING FOREST FIRES
Chosen Algorithm: Quickhull


## How the algorithm works

Quickhull finds the convex hull, the smallest convex polygon that encloses every point. For the fire map, that polygon is the shortest closed containment line around all the sensors reporting fire.

The algorithm divides and conquers. The leftmost and rightmost points must be on the hull, so the line between them splits the points into an upper and a lower set. In each set, the point farthest from the line must also be on the hull. Any point inside the triangle formed by the line's two ends and that farthest point cannot be on the hull, so it is discarded. The same step then repeats on the two new edges of the triangle until no points remain outside.

## Motivation and Use cases

The product is for use by emergency responders to be able to contain a forest fire quickly and effectively.

As it stands it is difficult to visualise the most effective way to contain a forest fire without sacrificing a portion of the forest, which with this algorithm is minimised significantly.

The algorithm uses fire sensors scattered throughout the forest to identify which 'chunks' of the forest is affected by the fire. These sensors report their coordinates, which are then used to find the minimum area required to contain all of the fire.
## Limitations

1. **Concave and split fires.** A convex hull cannot bend inwards. For a crescent shaped fire, or two separate fires, the line closes the gaps and encloses forest that is not burning, so crews could clear more than they need to. The "Crescent shaped fire" and "Two separate fires" scenarios show this.
2. **Sensor coverage and reliability.** The line can only be as good as the sensor data. A failed or missing sensor pulls the line inwards and could leave part of the fire outside it; a false alarm pushes it outwards.
3. **Recursion depth.** `find_hull` is recursive. In the worst case the recursion goes n levels deep, so unusual inputs could reach Python's default limit of about 1,000 calls. Random and clustered data stay far below this.
4. **Map scale.** The map is a 100 by 100 grid with no real geographic coordinates. A real deployment would need GPS positions and a map projection.

## Dependencies and third party resources

1. **Python 3.12 or later**, with **Flask** for the web server and **pytest** for testing (see `requirements.txt`).
2. **Vercel** hosts the live deployment.
3. The browser frontend uses only standard HTML, CSS and JavaScript, with no external libraries.

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

| Area | Contributors |
|---|---|
| Core Algorithm | Doruk & Siddhant|
| API | Doruk |
| Frontend | Doruk |
| Testing | Siddhant & Doruk|
| ReadME | Doruk & Siddhant |
| Presentation | Doruk & Siddhant |

## Use of generative AI

We used Claude (Anthropic, Claude Opus 5.5 through the Claude app) during November 2026. We take full responsibility for all submitted work, and every team member can explain every part of the code.

### What it was used for

| Area | How AI contributed |
|---|---|
| Code review | Assessed the repository against the marking criteria and suggested a prioritised list of improvements |
| Tie break bug | Generated random tests that exposed tied farthest points being reported as hull corners, and proposed a fix |
| Frontend styling | Drafted `flame.svg` & `trees.svg` and small colour changes in `main.js` |
| Test scenario buttons | Generated relevant and interesting scenarios for use in the product |
| Deployment and setup | Suggested `pyproject.toml` for the Vercel entrypoint error|
| Presentation | Suggested layout and generated graphs & visuals |

The core algorithm in `quickhull.py`, the Flask API and the original frontend were written by the team before AI was used.

### Representative prompts

1. "Assess the source code against the marking criteria."
2. "Generate interesting test cases that can be activated using buttons in the frontend."
3. " [pasted build log error] identify what is causing this error with vercel deployment and suggest a viable fix"

### How we checked the output

1. We asked for the reasoning behind every change before applying it.
2. We ran the test suite with `python -m pytest` after each change to the algorithm.
3. We tested every scenario button in the browser and compared the results with values we could calculate by hand: 2 vertices and 0 ha for the collinear road, 72 vertices for the ring, and 4 vertices, 3,600 ha and 24 km for the square.
4. We checked the deployed site after each deployment.