const marqueeContainer = document.getElementById('marquee-container');
const emojis = ['&#x1F33B;', '&#127807;', '&#x1F338;']; // add more emojis as needed
const emojiWidth = 20; // adjust the width of each emoji
let currentEmojiIndex = 0;
let marqueeText = '        ';

function createMarquee() {
  marqueeText = '';
  for (let i = 0; i < 10; i++) { // adjust the number of repetitions
    marqueeText += emojis[currentEmojiIndex] + ' ';
    currentEmojiIndex = (currentEmojiIndex + 1) % emojis.length;
  }
  marqueeContainer.innerHTML = `<marquee>${marqueeText}</marquee>`;
}

function animateMarquee() {
  marqueeText = marqueeText.substring(1) + marqueeText[0]; // shift the text
  marqueeContainer.innerHTML = `<marquee>${marqueeText}</marquee>`;
  requestAnimationFrame(animateMarquee);
}

createMarquee();
animateMarquee();