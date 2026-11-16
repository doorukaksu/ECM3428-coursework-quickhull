
import math
import random
import time

from quickhull.quickhull import quickhull

def cross(o, a, b):
   
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def monotone_chain(points):
    points = sorted(set(points))
    if len(points) < 3:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()   # remove points that do not make a left turn
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]
def time_ms(function, points):
   
    times = []
    for _ in range(5):
        start = time.perf_counter()
        function(points)
        times.append((time.perf_counter() - start) * 1000)
    return sorted(times)[2]


rng = random.Random(1)
print("| Points | Quickhull, random | Baseline, random | Quickhull, circle | Baseline, circle |")
print("|---|---|---|---|---|")

for n in [1000, 5000, 10000, 50000]:
    random_points = [(rng.uniform(0, 100), rng.uniform(0, 100)) for _ in range(n)]
    circle = [(math.cos(2 * math.pi * k / n), math.sin(2 * math.pi * k / n)) for k in range(n)]

    print(f"| {n:,} "
          f"| {time_ms(quickhull, random_points):.1f} ms "
          f"| {time_ms(monotone_chain, random_points):.1f} ms "
          f"| {time_ms(quickhull, circle):.1f} ms "
          f"| {time_ms(monotone_chain, circle):.1f} ms |")