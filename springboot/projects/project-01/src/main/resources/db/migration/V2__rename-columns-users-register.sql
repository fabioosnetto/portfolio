
-- rename first_name to firstName
ALTER TABLE users_register
RENAME COLUMN first_name TO firstName;

-- rename last_name to lastName
ALTER TABLE users_register
RENAME COLUMN last_name TO lastName;

-- rename state_abbr to state
ALTER TABLE users_register
RENAME COLUMN state_abbr TO state;

-- rename user_status to status
ALTER TABLE users_register
RENAME COLUMN user_status TO status;