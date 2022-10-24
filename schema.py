instructions = [
    'DROP TABLE IF EXISTS usuario;',
    """
        CREATE TABLE usuario (
            id INT PRIMARY KEY AUTO_INCREMENT,
            username  VARCHAR(50) NOT NULL,
            password VARCHAR(102) NOT NULL
        )
    """
]