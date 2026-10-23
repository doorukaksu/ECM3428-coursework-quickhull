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
      ctx.fillStyle = "#757575";
      ctx.fill();
    }
    ctx.strokeStyle = "#c01515";
    ctx.lineWidth = 2;
    ctx.stroke();
  }
}




