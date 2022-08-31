CREATE TABLE IF NOT EXISTS books (
    id INT PRIMARY KEY AUTO_INCREMENT,
    book_name VARCHAR(50) NOT NULL,
    book_author VARCHAR(50) NOT NULL,
    book_release_date DATE NOT NULL
    
);