const SIZE = 600
const RANGE  = 100

const canvas = document.getElementById("canvas")
const ctx = canvas.getContext("2d")

let points = []
let hull = []

const flame = new Image();  
flame.src = "/static/flame.svg";

function toPixel([x, y]) {
  return [x / RANGE * SIZE, SIZE - y / RANGE * SIZE];
}

function toData(px, py) {
  return [px / SIZE * RANGE, (SIZE - py) / SIZE * RANGE];
}

function draw(){
  ctx.clearRect(0,0,SIZE,SIZE)
    
  const s = points.length > 500 ? 0.5 : 1; 
  for (const p of points) {
    const [x, y] = toPixel(p);
    ctx.drawImage(flame, x - 6 * s, y - 12 * s, 12 * s, 16 * s);
  }


  if (hull.length >= 2) {
    ctx.beginPath();
    hull.forEach((p, i) => {
      const [x, y] = toPixel(p);
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    });
    if (hull.length >= 3) {
      ctx.closePath();
      ctx.fillStyle = "#75757524";
      ctx.fill();
    }
    ctx.strokeStyle = "#c01515";
    ctx.lineWidth = 2;
    ctx.stroke();
  }
}

function showStats(data) {
  document.getElementById("points").textContent = data.input_count;
  document.getElementById("vertices").textContent = data.vertex_count;
  document.getElementById("area").textContent = data.area.toFixed(2);
  document.getElementById("perimeter").textContent = data.perimeter.toFixed(2);
}


async function update() {

  if (points.length === 0) {
    hull = [];
    showStats({ input_count: 0, vertex_count: 0, area: 0, perimeter: 0 });
    draw();
    return;
  }

  const res = await fetch("/api/quickhull", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ points }),
  });
  const data = await res.json();

  if (!res.ok) {
    return;
  }

  hull = data.hull;
  showStats(data);
  draw();
}

canvas.addEventListener("click", e => {
  const rect = canvas.getBoundingClientRect();
  const px = (e.clientX - rect.left) * (SIZE / rect.width);
  const py = (e.clientY - rect.top) * (SIZE / rect.height);
  points.push(toData(px, py));
  update();
});

document.getElementById("generate").addEventListener("click", () => {
  const n = Math.min(5000, Math.max(3, Number(document.getElementById("count").value) || 100));
  points = Array.from({ length: n }, () => [Math.random() * RANGE, Math.random() * RANGE]);
  update();
});

document.getElementById("clear").addEventListener("click", () => {
  points = [];
  update();
});

// Test scenarios


function addFire(cx, cy, width, height, n) {
  for (let i = 0; i < n; i++) {
    const angle = Math.random() * 2 * Math.PI;
    const dist = Math.random();
    points.push([cx + Math.cos(angle) * dist * width, cy + Math.sin(angle) * dist * height]);
  }
}


function showScenario(note) {
  document.getElementById("scenario-note").textContent = note;
  update();
}

function smallFire() {
  points = [];
  addFire(50, 50, 12, 12, 60);
  showScenario("Clustered: 60 sensors around one fire. The normal case.");
}

function windFire() {
  points = [];
  addFire(45, 50, 30, 10, 80);
  showScenario("Wind spreads the fire east to west, so the line is long and narrow.");
}

function twoFires() {
  points = [];
  addFire(25, 70, 8, 8, 40);
  addFire(75, 30, 8, 8, 40);
  showScenario("Limitation: one convex line around two fires also encloses the unburnt forest between them.");
}

function crescentFire() {
  points = [];
  for (let i = 0; i < 120; i++) {
    const angle = Math.random() * Math.PI;   // half a circle
    const r = 25 + Math.random() * 6;
    points.push([50 + Math.cos(angle) * r, 35 + Math.sin(angle) * r]);
  }
  showScenario("Limitation: a concave fire. The hull closes the open side, enclosing forest that is not burning.");
}

function roadSensors() {
  points = [];
  for (let k = 0; k < 20; k++) {
    points.push([10 + 4 * k, 20 + 3 * k]);   
  }
  showScenario("Collinear: every sensor on one straight line. Expected: 2 vertices and 0 ha.");
}

function ringSensors() {
  points = [];
  for (let k = 0; k < 72; k++) {
    const angle = k * 2 * Math.PI / 72;
    points.push([50 + 35 * Math.cos(angle), 50 + 35 * Math.sin(angle)]);
  }
  showScenario("Every sensor is on the hull, the worst case for output size. Expected: 72 vertices.");
}

function knownSquare() {
  points = [[20, 20], [80, 20], [80, 80], [20, 80], [50, 20], [80, 50], [50, 80], [20, 50]];
  for (let i = 0; i < 30; i++) {
    points.push([25 + Math.random() * 50, 25 + Math.random() * 50]);  
  }
  showScenario("Known answer. Expected: 4 vertices, 3600 ha, 24 km.");
}

function largeIncident() {
  points = [];
  for (let i = 0; i < 5000; i++) {
    points.push([Math.random() * RANGE, Math.random() * RANGE]);
  }
  showScenario("Large dataset: 5000 random sensors, the most the page allows. Tests speed.");
}