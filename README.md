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

## Installation

```bash
git clone https://github.com/doorukaksu/ECM3428-coursework-quickhull.git
cd ECM3428-coursework-quickhull
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python run.py
```

'run.py' creates the Flask app from the 'app' package and starts it. Open the address printed in the terminal, which is usually `http://127.0.0.1:5000`.

## Contributions

Backend - Doruk & Sidhant
FrontEnd - Doruk
API - Doruk
Testing - Sidhant