// Setting up the canvas
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Setting up the colors
const black = "#000";
const white = "#fff";

// Setting up the circle parameters
let circleXPos = canvas.width / 2;
let circleYPos = canvas.height / 2;
const circleRadius = 50;

// Initializing the game loop
let running = true;
function gameLoop() {
  // Filling the background
  ctx.fillStyle = black;
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Generate a random color
  const randomColor = `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`;

  // Draw the circle
  ctx.fillStyle = randomColor;
  ctx.beginPath();
  ctx.arc(circleXPos, circleYPos, circleRadius, 0, 2 * Math.PI);
  ctx.fill();

  // Check if the mouse is hovering over the circle
  let rect = canvas.getBoundingClientRect();
  let mouseXPos = event.clientX - rect.left;
  let mouseYPos = event.clientY - rect.top;
  if (Math.sqrt((mouseXPos - circleXPos)**2 + (mouseYPos - circleYPos)**2) <= circleRadius) {
    // Change the circle's color to white on mouse movement
    canvas.style.cursor = "pointer";
    canvas.addEventListener("mousemove", function() {
      ctx.fillStyle = white;
      ctx.beginPath();
      ctx.arc(circleXPos, circleYPos, circleRadius, 0, 2 * Math.PI);
      ctx.fill();
    });
    // Change the circle's color to random on mouse click
    canvas.addEventListener("click", function() {
      ctx.fillStyle = randomColor;
      ctx.beginPath();
      ctx.arc(circleXPos, circleYPos, circleRadius, 0, 2 * Math.PI);
      ctx.fill();
    });
  } else {
    canvas.style.cursor = "default";
  }

  // Check for events
  canvas.addEventListener("click", function() {
    running = false;
  });

  // Update the window
  requestAnimationFrame(gameLoop);
}

// Start the game loop
requestAnimationFrame(gameLoop);
