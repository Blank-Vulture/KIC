-- 既存のユーザー、データベース、テーブルを削除
SELECT COUNT(*) INTO @user_exists FROM mysql.user WHERE user = 'reservation';
SET @drop_sql = IF(@user_exists > 0, 'DROP USER `reservation`@`localhost`;', 'SELECT 1;');
PREPARE stmt FROM @drop_sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

DROP DATABASE IF EXISTS flight_db;
CREATE DATABASE flight_db;
USE flight_db;

-- ユーザー作成 & 権限付与
CREATE USER IF NOT EXISTS 'reservation'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON flight_db.* TO 'reservation'@'localhost';

-- 既存のテーブルを削除
DROP TABLE IF EXISTS flights;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS reservations;

-- `flights` テーブル
CREATE TABLE flights (
    id INTEGER PRIMARY KEY,
    flight_name CHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    departure_place CHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    arrival_place CHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    time CHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    cap_business INTEGER,
    cap_economy INTEGER
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- `customers` テーブル
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    password CHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    customer_name CHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- `reservations` テーブル
CREATE TABLE reservations (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    customer_id INTEGER,
    flight_id INTEGER,
    seat_class INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
    FOREIGN KEY (flight_id) REFERENCES flights(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;