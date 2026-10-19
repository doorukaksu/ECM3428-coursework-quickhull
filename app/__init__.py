import math
from flask import *


def App():
    app = Flask(__name__)
    
    @app.get("/")
    def home_page():
        return render_template("index.html")
    
    @app.post("/api/quickhull")
    def api_quickhull():
        data = request.get_json() or {}
        raw = data.get("points") # get this data from the browser via posting from js script