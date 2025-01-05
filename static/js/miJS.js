let cartCount = 0;
const cartCountElement = document.getElementById('cartCount');
const menuButton = document.getElementById('menuButton');
const closeMenu = document.getElementById('closeMenu');
const sideMenu = document.getElementById('sideMenu');

function toggleMenu() {
    sideMenu.classList.toggle('-translate-x-full');
}

menuButton.addEventListener('click', toggleMenu);
closeMenu.addEventListener('click', toggleMenu);

document.addEventListener('click', (e) => {
    if (!sideMenu.contains(e.target) && !menuButton.contains(e.target) && !sideMenu.classList.contains('-translate-x-full')) {
        toggleMenu();
    }
});

function incrementCart() {
    cartCount++;
    cartCountElement.textContent = cartCount;
}


// para el carrusel del index pa 
const carousel = document.getElementById('carousel');
const images = carousel.querySelectorAll('img');
let currentImageIndex = 0;

function showImage(index) {
    images.forEach((image, i) => {
        if (i === index) {
            image.classList.remove('opacity-0');
        } else {
            image.classList.add('opacity-0');
        }
    });
}

function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    showImage(currentImageIndex);
}

setInterval(nextImage, 3000);