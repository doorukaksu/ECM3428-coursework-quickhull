import math
from flask import *
from quickhull.quickhull import *
MAX_POINTS = 50000
def App():
    app = Flask(__name__)
    
    @app.get("/")
    def home_page():
        return render_template("index.html")
    
    @app.post("/api/quickhull")
    def api_quickhull():
        data = request.get_json() or {}
        raw = data.get("points") # get this data from the browser via posting from js script
        
        if not isinstance(raw, list):
            return jsonify(error='whoops')
        if len(raw) > MAX_POINTS:
            return jsonify(error='too many points')
        
        try:
            pts = [(float(x), float(y)) for x,y in raw]
        except:
            return jsonify(error='non numerical')    
        
        hull = quickhull(pts)
        
        return jsonify(input_count = len(pts),
                       hull=[list(p) for p in hull],
                       vertex_count=len(hull),
                       area=polygon_area(hull),
                       perimeter=perimeter(hull))
        
        
    return app