// Productos de ejemplo (simulando datos del carrito)
const cartData = [
    { id: 1, nombre: "Producto 1", precio: 50, cantidad: 2 },
    { id: 2, nombre: "Producto 2", precio: 30, cantidad: 1 },
];

const cartItems = document.getElementById("cartItems");
const cartTotal = document.getElementById("cartTotal");

function renderCart() {
    cartItems.innerHTML = ""; // Limpiar la tabla
    let total = 0;

    cartData.forEach((item, index) => {
        const row = document.createElement("tr");
        row.classList.add(index % 2 === 0 ? "bg-gray-50" : "bg-white");

        row.innerHTML = `
            <td class="px-6 py-4">${item.nombre}</td>
            <td class="px-6 py-4">
                <input type="number" value="${item.cantidad}" min="1" class="w-16 border border-gray-300 rounded-md px-2 text-center" onchange="updateQuantity(${item.id}, this.value)">
            </td>
            <td class="px-6 py-4">$${item.precio.toFixed(2)}</td>
            <td class="px-6 py-4">$${(item.precio * item.cantidad).toFixed(2)}</td>
            <td class="px-6 py-4">
                <button class="text-red-500 font-bold" onclick="removeItem(${item.id})">Eliminar</button>
            </td>
        `;

        cartItems.appendChild(row);
        total += item.precio * item.cantidad;
    });

    cartTotal.textContent = `$${total.toFixed(2)}`;
}

function updateQuantity(id, quantity) {
    const product = cartData.find(item => item.id === id);
    if (product) {
        product.cantidad = parseInt(quantity, 10) || 1;
        renderCart();
    }
}

function removeItem(id) {
    const index = cartData.findIndex(item => item.id === id);
    if (index !== -1) {
        cartData.splice(index, 1);
        renderCart();
    }
}

// Renderizar el carrito al cargar la página
renderCart();