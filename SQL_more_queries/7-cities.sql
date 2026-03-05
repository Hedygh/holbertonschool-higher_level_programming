-- creates the database hbtn_0d_usa and the table cities with a foreign key to states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- creates cities table in hbtn_0d_usa if it doesn't exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);