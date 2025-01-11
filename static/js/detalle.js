document.addEventListener("DOMContentLoaded", () => {
    // Recuperar los datos del producto desde localStorage
    const producto = JSON.parse(localStorage.getItem("productoSeleccionado"));
    if (!producto) {
        // Si no hay datos, redirigir a la página principal
        window.location.href = "/";
        return;
    }

    // Insertar los datos del producto en los elementos HTML
    document.getElementById("imagen").src = `/static/img/${producto.imagen}`;
    document.getElementById("nombre").innerText = producto.nombre;
    document.getElementById("precio").innerText = `$${producto.precio}`;
    document.getElementById("descripcion").innerText = producto.descripcion || "Descripción no disponible.";
});