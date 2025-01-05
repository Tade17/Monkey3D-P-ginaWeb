const userButton = document.getElementById('userButton');
const userDropdown = document.getElementById('userDropdown');

userButton.addEventListener('click', () => {
    userDropdown.classList.toggle('hidden');
});

// Cerrar el dropdown si se hace clic fuera de él
window.addEventListener('click', (event) => {
    if (!userButton.contains(event.target) && !userDropdown.contains(event.target)) {
        userDropdown.classList.add('hidden');
    }
});