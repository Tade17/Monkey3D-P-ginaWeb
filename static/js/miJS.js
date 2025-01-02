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