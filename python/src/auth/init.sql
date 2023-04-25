/*
CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Aauth123';
DROP USER 'auth_user'@'localhost';
*/

CREATE DATABASE auth;

/*
GRANT CREATE USER ON *.* TO 'root'@'%';
*/

CREATE USER 'auth_user'@'%' IDENTIFIED BY '';
SET PASSWORD FOR 'auth_user'@'%' = 'Aauth123';

/*
GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';
*/

GRANT SELECT, INSERT, UPDATE ON auth.* TO 'auth_user'@'%';


USE auth;

CREATE TABLE user(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
)

INSERT INTO user(email, password) VALUES ('xodmf1215@naver.com', 'Admin123');