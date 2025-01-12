CREATE TABLE pais(
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    codigo_iso VARCHAR(4),
    disponible TINYINT(1) DEFAULT 1,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE departamento (
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    codigo_postal VARCHAR(10),
    disponible TINYINT(1) DEFAULT 1,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    pais_id INT(10) UNSIGNED NOT null,
    FOREIGN KEY( pais_id) REFERENCES pais(id)
);

CREATE TABLE provincia(
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    disponible TINYINT(1) DEFAULT 1,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    departamento_id INT(10) UNSIGNED NOT NULL,
    codigo_postal VARCHAR(10),
    FOREIGN KEY (departamento_id) REFERENCES departamento(id)
);

CREATE TABLE distrito(
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    disponible TINYINT(1) DEFAULT 1,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    provincia_id INT(10) UNSIGNED NOT NULL,
    codigo_postal VARCHAR(10),
    FOREIGN KEY (provincia_id) REFERENCES provincia(id)
);

CREATE TABLE direccion(
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    calle VARCHAR(255) not null,
    numero_casa VARCHAR(255) not null,
    referencia VARCHAR(255),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    distrito_id INT(10) UNSIGNED NOT NULL,
    FOREIGN KEY (distrito_id) REFERENCES distrito(id)
);

CREATE TABLE usuario(
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(255) not null,
    apellidos varchar(255) not null,
    email varchar(255) not null UNIQUE,
    -- Añadido UNIQUE para email
    contraseña varchar(255) not null,
    rol enum('administrador', 'cliente') DEFAULT 'cliente',
    foto varchar(255),
    telefono varchar(15) not null,
    activo TINYINT(1) DEFAULT 1,
    fecha_creacion timestamp DEFAULT current_timestamp
);

CREATE TABLE categoria(
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(200) not null UNIQUE,
    fecha_creacion timestamp DEFAULT current_timestamp
);

CREATE TABLE producto (
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255) not null,
    precio NUMERIC(10, 2) not null,
    stock INT(10) not null,
    imagen VARCHAR(255),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado TINYINT(1) DEFAULT 1,
    categoria_id INT(10) UNSIGNED,
    FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);

CREATE TABLE domicilio(
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    predeterminado TINYINT(1) DEFAULT 1,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    direccion_id INT(10) UNSIGNED NOT NULL,
    usuario_id INT(10) UNSIGNED NOT NULL,
    FOREIGN KEY (direccion_id) REFERENCES direccion(id),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

CREATE TABLE metodo_pago(
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre_metodo_pago varchar(100) not null UNIQUE,
    numeroTarjeta varchar(50) not null,
    cvv varchar(5) not null,
    titular varchar(200) not null,
    predeterminado TINYINT(1) DEFAULT 1,
    fecha_vencimiento date,
    fecha_creacion timestamp DEFAULT current_timestamp,
    usuario_id INT(10) UNSIGNED,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

create table pedido(
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fecha_pedido date DEFAULT current_date,
    total NUMERIC(10, 2) not null,
    estado CHAR(1) not null,
    domicilio_id INT(10) UNSIGNED not null,
    usuario_id INT(10) UNSIGNED not null,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id),
    FOREIGN KEY(domicilio_id) REFERENCES domicilio(id)
);

CREATE TABLE pago (
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    monto NUMERIC(10, 2),
    estado VARCHAR(15),
    MetodoPago_id INT(10) UNSIGNED,
    -- Corregido el nombre de la columna
    pedido_id INT(10) UNSIGNED,
    FOREIGN KEY (MetodoPago_id) REFERENCES metodo_pago(id),
    -- Corregido el nombre de la columna
    FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);

-- Tabla DETALLE_PEDIDO
CREATE TABLE detalle_pedido (
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    precioUnitario NUMERIC(8, 2) not null,
    descuento NUMERIC(5, 2) not null,
    cantidad INT(10) not null,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    producto_id INT(10) UNSIGNED,
    pedido_id INT(10) UNSIGNED,
    FOREIGN KEY (producto_id) REFERENCES producto(id),
    FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);

CREATE TABLE opiniones (
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    reseña VARCHAR(255),
    calificacion INT(1),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario_id INT(10) UNSIGNED,
    producto_id INT(10) UNSIGNED,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id),
    FOREIGN KEY (producto_id) REFERENCES producto(id)
);

CREATE TABLE favoritos (
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario_id INT(10) UNSIGNED,
    producto_id INT(10) UNSIGNED,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id),
    FOREIGN KEY (producto_id) REFERENCES producto(id)
);

CREATE TABLE notificaciones (
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(255),
    visto TINYINT(1) DEFAULT 0,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario_id INT(10) UNSIGNED,
    pedido_id INT(10) UNSIGNED,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id),
    FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);


INSERT INTO PAIS (codigo_iso, nombre) VALUES
('PER', 'Perú'),
('COL', 'Colombia'),
('ARG','Argentina');
-- inserts departamento 
INSERT INTO
    departamento (nombre, codigo_postal,pais_id)
VALUES
    ('Amazonas', '01',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Áncash', '02',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Apurímac', '03',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Arequipa', '04',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Ayacucho', '05',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Cajamarca', '06',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Callao', '07',(SELECT id FROM pais WHERE nombre = 'Perú')),   
    ('Cusco', '08',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Huancavelica', '09',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Huánuco', '10',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Ica', '11',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Junín', '12',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('La Libertad', '13',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Lambayeque', '14',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Lima', '15',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Loreto', '16',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Madre de Dios', '17',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Moquegua', '18',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Pasco', '19',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Piura', '20',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Puno', '21',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('San Martín', '22',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Tacna', '23',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Tumbes', '24',(SELECT id FROM pais WHERE nombre = 'Perú')),
    ('Ucayali', '25',(SELECT id FROM pais WHERE nombre = 'Perú'));

-- inserts provincia
INSERT INTO provincia (nombre, departamento_id, codigo_postal) VALUES
('Chiclayo', (SELECT id FROM departamento WHERE nombre = 'Lambayeque'), '1401'),
('Lambayeque', (SELECT id FROM departamento WHERE nombre = 'Lambayeque'), '1402'),
('Ferreñafe', (SELECT id FROM departamento WHERE nombre = 'Lambayeque'), '1403'),
('Trujillo', (SELECT id FROM departamento WHERE nombre = 'La Libertad'), '1301'),
('Arequipa', (SELECT id FROM departamento WHERE nombre = 'Arequipa'), '0401'),
('Cusco', (SELECT id FROM departamento WHERE nombre = 'Cusco'), '0801');



-- inserts distrito
INSERT INTO distrito (nombre, provincia_id, codigo_postal) VALUES
('Chiclayo', (SELECT id FROM provincia WHERE nombre = 'Chiclayo'), '140101'),
('José Leonardo Ortiz', (SELECT id FROM provincia WHERE nombre = 'Chiclayo'), '140105'),
('La Victoria', (SELECT id FROM provincia WHERE nombre = 'Chiclayo'), '140104'),
('Lambayeque', (SELECT id FROM provincia WHERE nombre = 'Lambayeque'), '140201'),
('Mórrope', (SELECT id FROM provincia WHERE nombre = 'Lambayeque'), '140203'),
('Ferreñafe', (SELECT id FROM provincia WHERE nombre = 'Ferreñafe'), '140301'),
('Trujillo', (SELECT id FROM provincia WHERE nombre = 'Trujillo'), '130101'),
('Huanchaco', (SELECT id FROM provincia WHERE nombre = 'Trujillo'), '130104'),
('Arequipa', (SELECT id FROM provincia WHERE nombre = 'Arequipa'), '040101'),
('Miraflores', (SELECT id FROM provincia WHERE nombre = 'Arequipa'), '040109'),
('Cusco', (SELECT id FROM provincia WHERE nombre = 'Cusco'), '080101'),
('San Sebastián', (SELECT id FROM provincia WHERE nombre = 'Cusco'), '080108');