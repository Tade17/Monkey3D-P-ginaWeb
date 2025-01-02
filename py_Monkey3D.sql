-- Estructura de tabla para la tabla `departamento`
CREATE TABLE `departamento` (
    `id` int(11) NOT NULL,
    `nombre` varchar(100) NOT NULL,
    `disponible` tinyint(1) DEFAULT 1,
    `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `provincia`
CREATE TABLE `provincia` (
    `id` int(11) NOT NULL,
    `nombre` varchar(100) NOT NULL,
    `disponible` tinyint(1) DEFAULT 1,
    `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `distrito`
CREATE TABLE `distrito` (
    `id` int(11) NOT NULL,
    `nombre` varchar(100) NOT NULL,
    `disponible` tinyint(1) DEFAULT 1,
    `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `direccion`
CREATE TABLE `direccion` (
    `id` int(11) NOT NULL,
    `calle` varchar(255) NOT NULL,
    `referencia` varchar(255) NOT NULL,
    `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp(),
    `idDepartamento` int(11) NOT NULL,
    `idProvincia` int(11) NOT NULL,
    `idDistrito` int(11) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `domicilio`
CREATE TABLE `domicilio` (
    `id` int(11) NOT NULL,
    `predeterminado` tinyint(1) DEFAULT 0,
    `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp(),
    `idDireccion` int(11) NOT NULL,
    `idUsuario` int(11) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `departamento_provincia`
CREATE TABLE `departamento_provincia` (
    `idDepartamento` int(11) NOT NULL,
    `idProvincia` int(11) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `distrito_provincia`
CREATE TABLE `distrito_provincia` (
    `idDistrito` int(11) NOT NULL,
    `idProvincia` int(11) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `usuario`
CREATE TABLE `usuario` (
    `id` int(11) NOT NULL,
    `nombre` varchar(100) NOT NULL,
    `apellidos` varchar(100) NOT NULL,
    `email` varchar(200) NOT NULL,
    `contraseña` varchar(255) NOT NULL,
    `tipo` enum('cliente', 'administrador') DEFAULT 'cliente',
    `foto` varchar(255) DEFAULT NULL,
    `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `pedido`
CREATE TABLE `pedido` (
    `id` int(11) NOT NULL,
    `idUsuario` int(11) NOT NULL,
    `fecha_pedido` date NOT NULL DEFAULT current_timestamp(),
    `estado` varchar(20) NOT NULL,
    `idDomicilio` int(11) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `detalle_pedido`
CREATE TABLE `detalle_pedido` (
    `id` int(11) NOT NULL,
    `precioUnitario` decimal(10, 2) NOT NULL,
    `cantidad` int(11) NOT NULL,
    `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp(),
    `idProducto` int(11) NOT NULL,
    `idPedido` int(11) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `metodo_pago`
CREATE TABLE `metodo_pago` (
    `id` int(11) NOT NULL,
    `nombre` varchar(120) NOT NULL, 
    `numeroTarjeta` varchar(100) NOT NULL,
    `cvv` varchar(255) NOT NULL,
    `titular` varchar(100) NOT NULL,
    `predeterminado` tinyint(1) DEFAULT 0,
    `fechaVencimiento` date NOT NULL,
    `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp(),
    `idUsuario` int(11) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `pago`
CREATE TABLE `pago` (
    `id` int(11) NOT NULL,
    `fecha` date NOT NULL DEFAULT current_timestamp(),
    `monto` decimal(10, 2) NOT NULL,
    `idMetodoPago` int(11) NOT NULL,
    `idPedido` int(11) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `notificaciones`
CREATE TABLE `notificaciones` (
    `id` int(11) NOT NULL,
    `mensaje` varchar(255) NOT NULL,
    `visto` tinyint(1) DEFAULT 0,
    `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp(),
    `idUsuario` int(11) NOT NULL,
    `idPedido` int(11) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `producto`
CREATE TABLE `producto` (
    `id` int(11) NOT NULL,
    `nombre` varchar(100) NOT NULL,
    `descripcion` varchar(255) NOT NULL,
    `precio` decimal(10, 2) NOT NULL,
    `stock` int(11) NOT NULL,
    `imagen` varchar(255) NOT NULL,
    `destacado` tinyint(1) DEFAULT 0,
    `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp(),
    `idCategoria` int(11) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `materiales`
CREATE TABLE `materiales` (
    `id` int(11) NOT NULL,
    `nombre` varchar(100) NOT NULL,
    `descripcion` varchar(255) NOT NULL,
    `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `materiales_producto`
CREATE TABLE `materiales_producto` (
    `idMateriales` int(11) NOT NULL,
    `idProducto` int(11) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `categoria`
CREATE TABLE `categoria` (
    `id` int(11) NOT NULL,
    `nombre` varchar(100) NOT NULL,
    `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `opiniones`
CREATE TABLE `opiniones` (
    `id` int(11) NOT NULL,
    `reseña` varchar(255) NOT NULL,
    `calificacion` int(1) NOT NULL,
    `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp(),
    `idUsuario` int(11) NOT NULL,
    `idProducto` int(11) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Estructura de tabla para la tabla `favoritos`
CREATE TABLE `favoritos` (
    `id` int(11) NOT NULL,
    `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp(),
    `idUsuario` int(11) NOT NULL,
    `idProducto` int(11) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Índices para tablas volcadas
-- Indices de la tabla `departamento`
ALTER TABLE
    `departamento`
ADD
    PRIMARY KEY (`id`),
ADD
    UNIQUE KEY `nombre` (`nombre`);

-- Indices de la tabla `provincia`
ALTER TABLE
    `provincia`
ADD
    PRIMARY KEY (`id`),
ADD
    UNIQUE KEY `nombre` (`nombre`);

-- Indices de la tabla `distrito`
ALTER TABLE
    `distrito`
ADD
    PRIMARY KEY (`id`),
ADD
    UNIQUE KEY `nombre`(`nombre`);

-- Indices de la tabla `direccion`
ALTER TABLE
    `direccion`
ADD
    PRIMARY KEY (`id`),
ADD
    KEY `idDepartamento` (`idDepartamento`),
ADD
    KEY `idProvincia` (`idProvincia`),
ADD
    KEY `idDistrito` (`idDistrito`);

-- Indices de la tabla `domicilio`
ALTER TABLE
    `domicilio`
ADD
    PRIMARY KEY (`id`),
ADD
    KEY `idDireccion` (`idDireccion`);

-- Indices de la tabla `departamento_provincia`
ALTER TABLE
    `departamento_provincia`
ADD
    PRIMARY KEY (`idDepartamento`, `idProvincia`),
ADD
    KEY `idDepartamento` (`idDepartamento`),
ADD
    KEY `idProvincia` (`idProvincia`);

-- Indices de la tabla `distrito_provincia`
ALTER TABLE
    `distrito_provincia`
ADD
    PRIMARY KEY (`idDistrito`, `idProvincia`),
ADD
    KEY `idDistrito` (`idDistrito`),

ADD
    KEY `idProvincia` (`idProvincia`);

-- Indices de la tabla `producto`
ALTER TABLE
    `producto`
ADD
    PRIMARY KEY (`id`),
ADD
    KEY `idCategoria` (`idCategoria`);

-- Indices de la tabla `materiales`
ALTER TABLE
    `materiales`
ADD
    PRIMARY KEY (`id`);

-- Indices de la tabla `usuario`
ALTER TABLE
    `usuario`
ADD
    PRIMARY KEY(`id`),
ADD
    UNIQUE KEY `email`(`email`);

-- Indices de la tabla `metodo_pago`
ALTER TABLE
    `metodo_pago`
ADD
    PRIMARY KEY(`id`),
ADD
    UNIQUE KEY `nombre`(`nombre`),
ADD
    KEY `idUsuario`(`idUsuario`);

-- Indices de la tabla `materiales_producto`
ALTER TABLE
    `materiales_producto`
ADD
    PRIMARY KEY (`idMateriales`, `idProducto`),
ADD
    KEY `idMateriales` (`idMateriales`),

ADD
    KEY `idProducto` (`idProducto`);

-- Indices de la tabla `categoria`
ALTER TABLE
    `categoria`
ADD
    PRIMARY KEY (`id`);

-- Indices de la tabla `opiniones`
ALTER TABLE
    `opiniones`
ADD
    PRIMARY KEY (`id`),
ADD
    KEY `idUsuario` (`idUsuario`),
ADD
    KEY `idProducto` (`idProducto`);

-- Indices de la tabla `favoritos`
ALTER TABLE
    `favoritos`
ADD
    PRIMARY KEY (`id`),
ADD
    KEY `idUsuario` (`idUsuario`),
ADD
    KEY `idProducto` (`idProducto`);

-- Indices de la tabla `pedido`
ALTER TABLE
    `pedido`
ADD
    PRIMARY KEY (`id`),
ADD
    KEY `idUsuario` (`idUsuario`),
ADD
    KEY `idDomicilio` (`idDomicilio`);

-- Indices de la tabla `detalle_pedido`
ALTER TABLE
    `detalle_pedido`
ADD
    PRIMARY KEY (`id`),
ADD
    KEY `idPedido` (`idPedido`),
ADD
    KEY `idProducto` (`idProducto`);

-- Indices de la tabla `pago`
ALTER TABLE
    `pago`
ADD
    PRIMARY KEY (`id`),
ADD
    KEY `idMetodoPago` (`idMetodoPago`),
ADD
    KEY `idPedido` (`idPedido`);

-- Indices de la tabla `notificaciones`
ALTER TABLE
    `notificaciones`
ADD
    PRIMARY KEY (`id`),
ADD
    KEY `idUsuario` (`idUsuario`),
ADD
    KEY `idPedido` (`idPedido`);

-- AUTO_INCREMENT para las tablas volcadas
-- AUTO_INCREMENT de la tabla `departamento`
ALTER TABLE
    `departamento`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- AUTO_INCREMENT de la tabla `provincia`
ALTER TABLE
    `provincia`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- AUTO_INCREMENT de la tabla `distrito`
ALTER TABLE
    `distrito`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- AUTO_INCREMENT de la tabla `direccion`
ALTER TABLE
    `direccion`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- AUTO_INCREMENT de la tabla `domicilio`
ALTER TABLE
    `domicilio`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE
    `producto`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- AUTO_INCREMENT de la tabla `materiales`
ALTER TABLE
    `materiales`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- AUTO_INCREMENT de la tabla `categoria`
ALTER TABLE
    `categoria`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- AUTO_INCREMENT de la tabla `opiniones`
ALTER TABLE
    `opiniones`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- AUTO_INCREMENT de la tabla `favoritos`
ALTER TABLE
    `favoritos`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- AUTO_INCREMENT de la tabla `notificaciones`
ALTER TABLE
    `notificaciones`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- AUTO_INCREMENT de la tabla `pedido`
ALTER TABLE
    `pedido`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- AUTO_INCREMENT de la tabla `usuario`
ALTER TABLE
    `usuario`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- AUTO_INCREMENT de la tabla `detalle_pedido`
ALTER TABLE
    `detalle_pedido`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- AUTO_INCREMENT de la tabla `pago`
ALTER TABLE
    `pago`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- AUTO_INCREMENT de la tabla `metodo_pago`
ALTER TABLE
    `metodo_pago`
MODIFY
    `id` int(11) NOT NULL AUTO_INCREMENT;

-- Restricciones para tablas volcadas
-- Filtros para la tabla `direccion`
ALTER TABLE
    `direccion`
ADD
    CONSTRAINT `direccion_ibfk_1` FOREIGN KEY (`idDepartamento`) REFERENCES `departamento` (`id`),
ADD
    CONSTRAINT `direccion_ibfk_2` FOREIGN KEY (`idProvincia`) REFERENCES `provincia` (`id`),
ADD
    CONSTRAINT `direccion_ibfk_3` FOREIGN KEY (`idDistrito`) REFERENCES `distrito` (`id`);

-- Filtros para la tabla `domicilio`
ALTER TABLE
    `domicilio`
ADD
    CONSTRAINT `domicilio_ibfk_1` FOREIGN KEY (`idDireccion`) REFERENCES `direccion` (`id`),

ADD
    CONSTRAINT `domicilio_ibfk_2` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`id`);

-- Filtros para la tabla `departamento_provincia`
ALTER TABLE
    `departamento_provincia`
ADD
    CONSTRAINT `departamento_provincia_ibfk_1` FOREIGN KEY (`idDepartamento`) REFERENCES `departamento` (`id`),
ADD
    CONSTRAINT `departamento_provincia_ibfk_2` FOREIGN KEY (`idProvincia`) REFERENCES `provincia` (`id`);

-- Filtros para la tabla `distrito_provincia`
ALTER TABLE
    `distrito_provincia`
ADD
    CONSTRAINT `distrito_provincia_ibfk_1` FOREIGN KEY (`idDistrito`) REFERENCES `distrito` (`id`),
ADD
    CONSTRAINT `distrito_provincia_ibfk_2` FOREIGN KEY (`idProvincia`) REFERENCES `provincia` (`id`);


-- Filtros para la tabla `pedido`
ALTER TABLE
    `pedido`
ADD
    CONSTRAINT `pedido_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`id`),
ADD
    CONSTRAINT `pedido_ibfk_2` FOREIGN KEY (`idDomicilio`) REFERENCES `domicilio` (`id`);


-- Filtros para la tabla `detalle_pedido`
ALTER TABLE
    `detalle_pedido`
ADD
    CONSTRAINT `detalle_pedido_ibfk_1` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`id`),
ADD
    CONSTRAINT `detalle_pedido_ibfk_2` FOREIGN KEY (`idPedido`) REFERENCES `pedido` (`id`);



-- Filtros para la tabla `metodo_pago`
ALTER TABLE
    `metodo_pago`
ADD
    CONSTRAINT `metodo_pago_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`id`);




-- Filtros para la tabla `pago`
ALTER TABLE
    `pago`
ADD
    CONSTRAINT `pago_ibfk_1` FOREIGN KEY (`idMetodoPago`) REFERENCES `metodo_pago` (`id`),
ADD
    CONSTRAINT `pago_ibfk_2` FOREIGN KEY (`idPedido`) REFERENCES `pedido` (`id`);


-- Filtros para la tabla `notificaciones`
ALTER TABLE
    `notificaciones`
ADD
    CONSTRAINT `notificaciones_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`id`),
ADD
    CONSTRAINT `notificaciones_ibfk_2` FOREIGN KEY (`idPedido`) REFERENCES `pedido` (`id`);

-- Filtros para la tabla `producto`
ALTER TABLE
    `producto`
ADD
    CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`idCategoria`) REFERENCES `categoria` (`id`);


-- Filtros para la tabla `materiales_producto`
ALTER TABLE
    `materiales_producto`
ADD
    CONSTRAINT `materiales_producto_ibfk_1` FOREIGN KEY (`idMateriales`) REFERENCES `materiales` (`id`),
ADD
    CONSTRAINT `materiales_producto_ibfk_2` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`id`);

-- Filtros para la tabla `opiniones`
ALTER TABLE
    `opiniones`
ADD
    CONSTRAINT `opiniones_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`id`),
ADD
    CONSTRAINT `opiniones_ibfk_2` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`id`);

-- Filtros para la tabla `favoritos`
ALTER TABLE
    `favoritos`
ADD
    CONSTRAINT `favoritos_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`id`),
ADD
    CONSTRAINT `favoritos_ibfk_2` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`id`);

COMMIT;

