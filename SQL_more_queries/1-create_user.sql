-- 1. Create the user 'user_0d_1' if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- 2. Grant all privileges to 'user_0d_1' on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- 3. Flush privileges to apply changes
FLUSH PRIVILEGES;
