-- creates user user_0d_1 with all privileges on the MySQL server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- grants all privileges to user_0d_1 on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- applies privilege changes immediately
FLUSH PRIVILEGES;