// Datos de los productos
const productos = [
  { id: 1, nombre: "Led lumninoso (YEAH)", precio: 29.99, categoria: "ofertas", imagen: "led-yeah.jpg", descripcion: "Creamos leds únicos basados en tus diseños o ideas." },
  { id: 2, nombre: "Led luminoso(BRUTAL)", precio: 29.99, categoria: "ofertas", imagen: "led-brutal.jpg", descripcion: "Creamos leds únicos basados en tus diseños o ideas." },
  { id: 3, nombre: "Funko personalizable (CR7)", precio: 40.99, categoria: "ofertas", imagen: "funko-bicho.jpg", descripcion: "Creamos funkos únicos basados en tus diseños o ideas." },
  { id: 4, nombre: "Funko personalizable(WWE)", precio: 40.99, categoria: "ofertas", imagen: "funko-roman-reings.jpg", descripcion: "Creamos funkos únicos basados en tus diseños o ideas." },
  { id: 5, nombre: "Soporte switch", precio: 25.99, categoria: "nuevos", imagen: "soporte-switch.jpg", descripcion: "Creamos figuras únicas basadas en tus diseños o ideas. Este es un soporte para Switch." },
  { id: 6, nombre: "Soporte mando ps5", precio: 25.99, categoria: "nuevos", imagen: "soporteMando2.jpg", descripcion: "Creamos figuras únicas basadas en tus diseños o ideas.Presentamos Soportes para mando de ps5" },
  { id: 7, nombre: "Llavero personalizado de Pokemon", precio: 14.99, categoria: "nuevos", imagen: "llavero-pokemon.jpg", descripcion: "Creamos llaveros únicos basadas en tus diseños o ideas." },
  { id: 8, nombre: "Llavero personalizado de spiderman", precio: 14.99, categoria: "nuevos", imagen: "llavero-spiderman.jpg", descripcion: "Creamos llaveros únicos basadas en tus diseños o ideas." },
  { id: 9, nombre: "Máscara Squid game", precio: 34.99, categoria: "destacados", imagen: "mascara-casa-papel.jpg", descripcion: "Creamos máscaras personalizadas basadas en tus diseños o ideas." },
  { id: 10, nombre: "Soporte audfionos Darth Veader", precio: 25.99, categoria: "destacados", imagen: "soporte_audifonos.DARTH.jpg", descripcion: "Creamos soportes de audífonos personalizados basadas en tus diseños o ideas." },
  { id: 11, nombre: "Soporte audifonos Batman", precio: 25.99, categoria: "destacados", imagen: "soporte_audifonos.batman.jpg", descripcion: "Creamos soportes de audífonos personalizados basadas en tus diseños o ideas." },
  { id: 12, nombre: "Umbrella Squid game", precio: 10.99, categoria: "destacados", imagen: "casa-papel-paraguas.jpg", descripcion: "Creamos soportes de audífonos personalizados basadas en tus diseños o ideas." }
];

// Función para renderizar productos
function renderProductos(categoria, containerId) {
  const container = document.getElementById(containerId).querySelector('div');
  const filtrados = productos.filter(producto => producto.categoria === categoria);
  filtrados.forEach(({ id, nombre, precio, imagen, categoria, descripcion }) => {
    let etiquetaColor = "";
    if (categoria === "ofertas") etiquetaColor = "bg-red-500";
    if (categoria === "nuevos") etiquetaColor = "bg-blue-500";
    if (categoria === "destacados") etiquetaColor = "bg-green-500";


    container.innerHTML += `
        <div class="bg-white shadow-md rounded-lg overflow-hidden hover:shadow-xl hover:shadow-blue-400 transition-all duration-300 relative"
             data-id="${id}" 
             data-name="${nombre}" 
             data-price="${precio}" 
             data-description="${descripcion}" 
             data-image="${imagen}" 
             data-category="${categoria}">
            <div class="absolute top-2 right-2 ${etiquetaColor} text-white text-xs font-semibold py-1 px-2 rounded">
                ${categoria.toUpperCase()}
            </div>
            <img src="/static/img/${imagen}" alt="${nombre}" class="w-full h-72 object-cover">
            <div class="p-4">
                <h3 class="text-lg font-semibold">${nombre}</h3>
                <p class="text-gray-600">$${precio}</p>
                <p class="text-gray-500 text-sm mb-2">${descripcion || "Descripción no disponible"}</p>
                <button 
                    class="ver-detalles mt-2 bg-blue-500 text-white py-1 px-3 rounded hover:bg-blue-700" 
                    data-id="${id}">Ver detalles</button>
                <button 
                    class="agregar-carrito mt-2 bg-blue-500 text-white py-1 px-3 rounded hover:bg-blue-700"
                    data-id="${id}" 
                    data-name="${nombre}" 
                    data-price="${precio}" 
                    data-description="${descripcion}" 
                    data-image="${imagen}" 
                    data-category="${categoria}">Agregar al Carrito</button>
            </div>
        </div>`;
  });
}

document.addEventListener("click", (e) => {
  if (e.target.classList.contains("ver-detalles")) {
    const idProducto = e.target.getAttribute("data-id");
    const producto = productos.find(p => p.id == idProducto);
    localStorage.setItem("productoSeleccionado", JSON.stringify(producto)); // Guarda el producto en localStorage
    window.location.href = "/templates/detalles.html"; // Redirige a la página de detalles
  }
});

// Renderizar cada sección
renderProductos("ofertas", "ofertas");
renderProductos("nuevos", "nuevos");
renderProductos("destacados", "destacados");