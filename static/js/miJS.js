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


// pal filtro del catalogo
const productosData = [
    {
        nombre: "Led lumninoso (YEAH)",
        imagen: "/static/img/led-yeah.jpg",
        categoria: "leds",
        precio: 14.99,
        tipo: "oferta" // "nuevo", "destacado", "oferta"
    },
    {
        nombre: "Led luminoso(BRUTAL)",
        imagen: "/static/img/led-brutal.jpg",
        categoria: "leds",
        precio: 14.99,
        tipo: "oferta"
    },
    {
        nombre: "Led luminoso(ANA)",
        imagen: "/static/img/led-ana.jpg",
        categoria: "leds",
        precio: 14.99,
        tipo: "oferta"
    },
    {
        nombre: "Soporte switch",
        imagen: "/static/img/soporte-switch.jpg",
        categoria: "soportes",
        precio: 25.99,
        tipo: "nuevo"
    },
    {
        nombre: "Soporte mando ps5",
        imagen: "/static/img/soporteMando2.jpg",
        categoria: "soportes",
        precio: 14.99,
        tipo: "nuevo"
    },
    {
        nombre: "Llavero personalizables",
        imagen: "/static/img/llavero-pokemon.jpg",
        categoria: "llaveros",
        precio: 14.99,
        tipo: "nuevo"
    },
    {
        nombre: "Llaveros personalizables",
        imagen: "/static/img/llavero-spiderman.jpg",
        categoria: "llaveros",
        precio: 14.99,
        tipo: "nuevo"
    },
    {
        nombre: "Máscara Papel's house",
        imagen: "/static/img/mascara-casa-papel.jpg",
        categoria: "accesorios",
        precio: 34.99,
        tipo: "destacado"
    },
    {
        nombre: "Circle Papel's house",
        imagen: "/static/img/casa-papel-circulo.jpg",
        categoria: "accesorios",
        precio: 34.99,
        tipo: "destacado"
    },
    {
        nombre: "Umbrella Papel's house",
        imagen: "/static/img/casa-papel-paraguas.jpg",
        categoria: "accesorios",
        precio: 34.99,
        tipo: "destacado"
    },
];

const filtroCategoria = document.getElementById('categoria');
const contenedores = {
    oferta: document.getElementById('ofertas-container'),
    nuevo: document.getElementById('nuevos-container'),
    destacado: document.getElementById('destacados-container')
};

function crearProducto(producto) {
    const productoDiv = document.createElement('div');
    productoDiv.classList.add('producto', 'border', 'rounded-lg', 'shadow-md', 'overflow-hidden', 'group', 'hover:shadow-xl', 'transition-all', 'duration-300', 'hover:shadow-blue-400', 'p-4'); // Corrección: sombra azul al hover
    productoDiv.dataset.categoria = producto.categoria;

    const relativeDiv = document.createElement('div');
    relativeDiv.classList.add('relative');

    const img = document.createElement('img');
    img.src = producto.imagen;
    img.alt = producto.nombre;
    img.classList.add('w-full', 'h-72', 'object-cover', 'group-hover:scale-105', 'transition-transform', 'duration-300');

    const tipoDiv = document.createElement('div');
    tipoDiv.classList.add('absolute', 'top-2', 'right-2', 'text-white', 'px-3', 'py-1', 'rounded-full', 'text-sm');

    switch (producto.tipo) { // Usando switch para mayor claridad
        case "oferta":
            tipoDiv.classList.add('bg-red-500');
            tipoDiv.textContent = "Oferta";
            break;
        case "nuevo":
            tipoDiv.classList.add('bg-blue-500');
            tipoDiv.textContent = "Nuevo";
            break;
        case "destacado":
            tipoDiv.classList.add('bg-green-500');
            tipoDiv.textContent = "Destacado";
            break;
    }

    const infoDiv = document.createElement('div');
    infoDiv.classList.add('p-4');

    const h3 = document.createElement('h3');
    h3.classList.add('font-bold', 'text-lg');
    h3.textContent = producto.nombre;

    const p = document.createElement('p');
    p.classList.add('text-gray-700');
    p.textContent = `$${producto.precio}`;

    const botonesDiv = document.createElement('div'); // Contenedor para los botones
    botonesDiv.classList.add('flex', 'flex-col', 'gap-2')

    const verDetallesBtn = document.createElement('button');
    verDetallesBtn.textContent = "Ver detalles";
    verDetallesBtn.classList.add('bg-blue-500', 'hover:bg-blue-700', 'text-white', 'font-bold', 'py-2', 'px-4', 'rounded', 'mt-2', 'w-full');

    const anadirCarritoBtn = document.createElement('button');
    anadirCarritoBtn.textContent = "Añadir al carrito";
    anadirCarritoBtn.classList.add('bg-blue-500', 'hover:bg-blue-700', 'text-white', 'font-bold', 'py-2', 'px-4', 'rounded', 'mt-2', 'w-full');

    relativeDiv.appendChild(img);
    relativeDiv.appendChild(tipoDiv);
    infoDiv.appendChild(h3);
    infoDiv.appendChild(p);
    botonesDiv.appendChild(verDetallesBtn)
    botonesDiv.appendChild(anadirCarritoBtn)
    infoDiv.appendChild(botonesDiv)
    productoDiv.appendChild(relativeDiv);
    productoDiv.appendChild(infoDiv);

    return productoDiv;
}

function mostrarProductos(categoria = 'todos') {
    for (const tipo in contenedores) {
        contenedores[tipo].innerHTML = ''; // Limpia los contenedores
        productosData.filter(producto => (categoria === 'todos' || producto.categoria === categoria) && producto.tipo === tipo)
            .forEach(producto => contenedores[tipo].appendChild(crearProducto(producto)));
    }
}

mostrarProductos(); // Muestra todos los productos al cargar la página

filtroCategoria.addEventListener('change', function () {
    mostrarProductos(this.value);
});

