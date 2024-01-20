CREATE TABLE users (
   id BIGSERIAL PRIMARY KEY NOT NULL,
   username VARCHAR(50) NOT NULL,
   age INT NOT NULL,
   email VARCHAR(256) NOT NULL,
   phone_number VARCHAR(18) NOT NULL,
   cpf VARCHAR(14) NOT NULL,
   gender VARCHAR(1) NOT NULL
);