
-- rename firstName to first_name
ALTER TABLE users_register
RENAME COLUMN firstname TO first_name;

-- rename lastName to last_name
ALTER TABLE users_register
RENAME COLUMN lastname TO last_name;

-- rename state to state_abbr
ALTER TABLE users_register
RENAME COLUMN state TO state_abbr;

-- rename status to user_status
ALTER TABLE users_register
RENAME COLUMN status TO user_status