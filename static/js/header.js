// Dropdown dinámico
const userButton = document.getElementById('userButton');
const userDropdown = document.getElementById('userDropdown');


// Botones y modal
const cartModal = document.getElementById('cart-modal');
const closeCartBtn = document.getElementById('close-cart');
const emptyCartMessage = document.getElementById('empty-cart-message');
const cartItemsContainer = document.getElementById('cart-items');
const emptyCartBtn = document.getElementById('empty-cart');

// Mostrar carrito
document.getElementById('open-cart').addEventListener('click', () => {
    cartModal.classList.add('show');
});

// Cerrar carrito
closeCartBtn.addEventListener('click', () => {
    cartModal.classList.remove('show');
});

// Vaciar carrito
emptyCartBtn.addEventListener('click', () => {
    cartItemsContainer.innerHTML = '';
    emptyCartMessage.style.display = 'block';
    document.getElementById('cart-total').textContent = '$0.00';
});




userButton.addEventListener('click', () => {
    const expanded = userButton.getAttribute('aria-expanded') === 'true' || false;
    userButton.setAttribute('aria-expanded', !expanded);
    userDropdown.classList.toggle('hidden');
});

// Menú lateral dinámico
const menuButton = document.getElementById('menuButton');
const closeMenu = document.getElementById('closeMenu');
const sideMenu = document.getElementById('sideMenu');

menuButton.addEventListener('click', () => {
    sideMenu.classList.remove('-translate-x-full');
});

closeMenu.addEventListener('click', () => {
    sideMenu.classList.add('-translate-x-full');
});

// Cerrar dropdown al hacer clic fuera
document.addEventListener('click', (e) => {
    if (!userButton.contains(e.target) && !userDropdown.contains(e.target)) {
        userDropdown.classList.add('hidden');
        userButton.setAttribute('aria-expanded', 'false');
    }
});

