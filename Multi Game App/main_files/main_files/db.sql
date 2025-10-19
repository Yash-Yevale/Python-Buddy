CREATE DATABASE pyproj;
USE pyproj;

CREATE DATABASE pyproj;
USE pyproj;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    shooter_score INT DEFAULT 0, -- Score for the "shooter" game
    quiz_score INT DEFAULT 0,    -- Score for the "quiz" game
    UNIQUE KEY (user_id)
);

describe users;
select * from users;
CREATE USER 'yash'@'localhost' IDENTIFIED BY 'SuperSpeed!2';
GRANT ALL PRIVILEGES ON pyproj.* TO 'yash'@'localhost';
