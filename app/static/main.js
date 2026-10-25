const SIZE = 600
const RANGE  = 100

const canvas = document.getElementById("canvas")
const ctx = canvas.getContext("2d")

let points = []
let hull = []

function toPixel([x, y]) {
  return [x / RANGE * SIZE, SIZE - y / RANGE * SIZE];
}

function toData(px, py) {
  return [px / SIZE * RANGE, (SIZE - py) / SIZE * RANGE];
}

function draw(){
  ctx.clearRect(0,0,SIZE,SIZE)
    
  ctx.fillStyle = "#2c2c2c";
  for (const p of points) {
    const [x, y] = toPixel(p);
    ctx.fillRect(x - 2, y - 2, 4, 4);
  }

  // Hull
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


