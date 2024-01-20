CREATE TABLE users_register (
   id BIGSERIAL PRIMARY KEY NOT NULL,
   username VARCHAR(50) NOT NULL,
   first_name VARCHAR(50) NOT NULL,
   last_name VARCHAR(50) NOT NULL,
   city VARCHAR(50) NOT NULL,
   state_abbr VARCHAR(2) NOT NULL,
   user_status VARCHAR(1) NOT NULL
);