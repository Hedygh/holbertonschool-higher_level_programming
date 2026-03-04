-- 17. Go to UTF8
-- converts hbtn_0c_0 database, first_table and name field to utf8mb4 unicode collation

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL;