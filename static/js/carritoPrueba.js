// Inicializamos el carrito vacío
let cart = [];

// Referencias a elementos del DOM
const cartItems = document.getElementById("cartItems");
const cartTotal = document.getElementById("cartTotal");
const cartCount = document.getElementById("cartCount");

// Función para renderizar los elementos del carrito
function renderCart() {
    cartItems.innerHTML = ""; // Limpiamos la tabla
    let total = 0;
    cart.forEach((item, index) => {
        const itemTotal = item.price * item.quantity;
        total += itemTotal;

        cartItems.innerHTML += `
            <tr>
                <td class="px-6 py-4">${item.name}</td>
                <td class="px-6 py-4">
                    <button onclick="updateQuantity(${index}, -1)" class="px-2 bg-red-500 text-white rounded">-</button>
                    ${item.quantity}
                    <button onclick="updateQuantity(${index}, 1)" class="px-2 bg-green-500 text-white rounded">+</button>
                </td>
                <td class="px-6 py-4">$${item.price.toFixed(2)}</td>
                <td class="px-6 py-4">$${itemTotal.toFixed(2)}</td>
                <td class="px-6 py-4">
                    <button onclick="removeItem(${index})" class="px-4 py-2 bg-red-500 text-white rounded">Eliminar</button>
                </td>
            </tr>
        `;
    });

    // Actualizamos el total y el contador
    cartTotal.textContent = `$${total.toFixed(2)}`;
    cartCount.textContent = cart.reduce((sum, item) => sum + item.quantity, 0);
}

// Función para agregar un producto al carrito
function addToCart(product) {
    const existingProduct = cart.find(item => item.id === product.id);
    if (existingProduct) {
        existingProduct.quantity += 1;
    } else {
        cart.push({ ...product, quantity: 1 });
    }
    renderCart();
}

// Función para actualizar la cantidad de un producto
function updateQuantity(index, change) {
    cart[index].quantity += change;
    if (cart[index].quantity <= 0) {
        cart.splice(index, 1); // Eliminamos si la cantidad es 0 o menos
    }
    renderCart();
}

// Función para eliminar un producto del carrito
function removeItem(index) {
    cart.splice(index, 1);
    renderCart();
}

// Función para proceder al pago
document.getElementById("checkoutButton").addEventListener("click", () => {
    if (cart.length === 0) {
        alert("El carrito está vacío. Agrega productos antes de proceder al pago.");
        return;
    }
    alert("Redirigiendo al proceso de pago...");
    // Lógica para procesar el pago (puedes redirigir a una página específica)
    console.log("Productos para pagar:", cart);
});

// Ejemplo: Agregar productos de prueba
addToCart({ id: 1, name: "Producto 1", price: 10.0 });
addToCart({ id: 2, name: "Producto 2", price: 20.0 });
