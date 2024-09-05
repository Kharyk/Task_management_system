const birdContainer = document.getElementById('bird-container');
const birdImage = '../img/bird2.webp'; 

let birdX = 0; //  x-coordinate
let birdY = 10; //  y-coordinate
let birdSpeed = 1; 

setInterval(() => {

  const birdElement = document.createElement('img');
  birdElement.src = birdImage;
  birdElement.style.position = 'absolute';
  birdElement.style.top = `${birdY}px`;
  birdElement.style.left = `${birdX}px`;
  birdContainer.appendChild(birdElement);

  function animate() {
    birdX += birdSpeed;
    birdElement.style.left = `${birdX}px`;
    if (birdX > window.innerWidth) {
      birdContainer.removeChild(birdElement);

    } else {
      requestAnimationFrame(animate);
    }
  }
  animate();
}, 2000); 