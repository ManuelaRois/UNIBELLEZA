INSERT OR IGNORE INTO Categoria (CategoriaID, NomCategoria, Descripcion) VALUES 
(101, 'Maquillaje', 'Productos de maquillaje como bases, sombras y labiales.'),
(102, 'Skincare', 'Productos para el cuidado de la piel como cremas y tónicos.'),
(103, 'Uñas', 'Productos para el cuidado y decoración de uñas.'),
(104, 'Accesorios', 'Accesorios de maquillaje como brochas y esponjas.');

-- Maquillaje
INSERT INTO Productos (NomProducto, Descripcion, CategoriaID, Precio, CantidadStock) VALUES 
('Lápiz delineador', 'Lápiz para delinear los ojos', 101, 40, 7),
('Paleta de sombras', 'Paleta de colores variados para sombras', 101, 250, 10),
('Base líquida', 'Base para el rostro de acabado natural', 101, 30, 5),
('Iluminador', 'Iluminador para resaltar el rostro', 101, 20, 5),
('Pestañina', 'Máscara para pestañas', 101, 17, 20),
('Labial mate', 'Labial de textura mate', 101, 50, 15),
('Corrector líquido', 'Corrector de textura líquida', 101, 35, 12),
('Rubor en polvo', 'Rubor compacto para mejillas', 101, 45, 8),
('Primer facial', 'Preparador para el rostro antes del maquillaje', 101, 60, 6);

-- Skincare
INSERT INTO Productos (NomProducto, Descripcion, CategoriaID, Precio, CantidadStock) VALUES 
('Crema hidratante', 'Crema para mantener la piel hidratada', 102, 80, 20),
('Serum vitamina C', 'Suero con vitamina C para la piel', 102, 100, 10),
('Protector solar SPF 50', 'Protector solar con factor 50', 102, 90, 15),
('Tónico facial', 'Tónico para equilibrar la piel', 102, 55, 12),
('Agua micelar', 'Agua limpiadora para el rostro', 102, 50, 18),
('Aceite limpiador', 'Aceite para retirar el maquillaje', 102, 65, 10);

-- Uñas
INSERT INTO Productos (NomProducto, Descripcion, CategoriaID, Precio, CantidadStock) VALUES 
('Esmalte rojo', 'Esmalte de color rojo', 103, 20, 20),
('Esmalte nude', 'Esmalte de tono natural', 103, 25, 18),
('Quitaesmalte', 'Removedor de esmalte de uñas', 103, 15, 15),
('Lima de uñas', 'Lima para dar forma a las uñas', 103, 10, 25);

-- Accesorios
INSERT INTO Productos (NomProducto, Descripcion, CategoriaID, Precio, CantidadStock) VALUES 
('Brocha para base', 'Brocha para aplicar base de maquillaje', 104, 35, 10),
('Esponja de maquillaje', 'Esponja para aplicar productos líquidos', 104, 20, 15),
('Pinza para cejas', 'Pinza para depilar cejas', 104, 15, 8),
('Cepillo para pestañas', 'Cepillo para dar forma a las pestañas', 104, 12, 10),
('Neceser de maquillaje', 'Estuche para guardar maquillaje', 104, 100, 5);


INSERT INTO Clientes (Nombre, Apellido, Email, Telefono, Direccion) VALUES
('Ana', 'Pérez', 'ana.perez@gmail.com', '3201234567', 'Calle 123 #45-67, Bogotá'),
('Carlos', 'Gómez', 'carlos.gomez@gmail.com', '3107654321', 'Carrera 10 #20-30, Medellín'),
('Lucía', 'Martínez', 'lucia.martinez@gmail.com', '3156789123', 'Avenida 5 #15-25, Cali'),
('Diego', 'López', 'diego.lopez@gmail.com', '3229876543', 'Calle 7 #8-12, Barranquilla'),
('Sofía', 'Torres', 'sofia.torres@gmail.com', '3191239876', 'Carrera 3 #4-56, Cartagena');

INSERT INTO Ventas (ClienteID, FechaVenta, TotalVenta) VALUES
(1, '2025-03-01', 120000.50),  -- Venta para Ana Pérez
(2, '2025-03-03', 85000.75),   -- Venta para Carlos Gómez
(3, '2025-03-05', 95000.00),   -- Venta para Lucía Martínez
(4, '2025-03-08', 72000.20),   -- Venta para Diego López
(5, '2025-03-10', 150000.00),  -- Venta para Sofía Torres
(1, '2025-03-15', 135000.00),  -- Segunda venta para Ana Pérez
(3, '2025-03-25', 110000.40);  -- Segunda venta para Lucía Martínez
