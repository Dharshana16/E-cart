INSERT INTO categories ("name") VALUES ('grocery');
INSERT INTO categories ("name") VALUES ('beauty');
INSERT INTO categories ("name") VALUES ('diy products');

INSERT INTO products ("name", "price", "description", "stock", "image", "category_id") VALUES
('Apple', 30.00, 'Fresh red apples', 300, 'apple.jpg', 1),
('Bread', 35.00, 'Whole grain bread', 300, 'bread.jpg', 1),
('Milk', 32.00, 'Low-fat milk', 300, 'milk.jpg', 1),
('Eggs', 40.00, 'Organic eggs', 300, 'eggs.jpg', 1),
('Rice', 50.00, 'Basmati rice', 300, 'rice.jpg', 1),
('Lipstick', 45.00, 'Matte lipstick', 300, 'lipstick.jpg', 2),
('Face Cream', 60.00, 'Anti-aging face cream', 300, 'facecream.jpg', 2),
('Shampoo', 30.00, 'Moisturizing shampoo', 300, 'shampoo.jpg', 2),
('Perfume', 50.00, 'Floral scent perfume', 300, 'perfume.jpg', 2),
('Nail Polish', 35.00, 'Gel nail polish', 300, 'nailpolish.jpg', 2),
('Hammer', 35.00, 'Steel hammer', 300, 'hammer.jpg', 3),
('Screwdriver', 30.00, 'Flathead screwdriver', 300, 'screwdriver.jpg', 3),
('Paint Brush', 32.00, 'Fine paint brush', 300, 'paintbrush.jpg', 3),
('Tape Measure', 38.00, '25 ft tape measure', 300, 'tapemeasure.jpg', 3),
('Drill', 60.00, 'Cordless power drill', 300, 'drill.jpg', 3);