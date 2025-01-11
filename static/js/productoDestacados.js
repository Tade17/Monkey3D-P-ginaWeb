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
// Filtrar productos destacados
const productosDestacados = productos.filter(producto => producto.categoria === "destacados");

// Seleccionar el contenedor de la sección
// const contenedorDestacados = document.querySelector('.grid.grid-cols-1.md:grid-cols-3.gap-8');
const contenedorDestacados2= document.getElementById('container-destacados');

// Generar el HTML dinámico
productosDestacados.forEach(producto => {
    const productoHTML = `
        <div class="bg-white rounded-lg shadow-lg overflow-hidden group hover:shadow-xl hover:shadow-blue-400 transition-all duration-300">
            <div class="relative">
                <img src="/static/img/${producto.imagen}" alt="${producto.nombre}" class="w-full h-72 object-cover group-hover:scale-105 transition-transform duration-300">
                <div class="absolute top-2 right-2 bg-green-500 text-white px-3 py-1 rounded-full text-sm">Destacado</div>
            </div>
            <div class="p-6">
                <h3 class="font-bold text-xl text-gray-800 mb-2">${producto.nombre}</h3>
                <p class="text-gray-600 mb-4">${producto.descripcion}</p>
                <div class="flex justify-between items-center">
                    <span class="text-blue-500 font-bold text-xl">$${producto.precio.toFixed(2)}</span>
                    <a href="/templates/detalles${producto.id}.html">
                        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg transition-colors">
                            Ver detalles
                        </button>
                    </a>
                </div>
            </div>
        </div>
    `;
    contenedorDestacados2.innerHTML += productoHTML;
});

