DROP TABLE IF EXISTS users cascade;
CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    name_of_user text,
    email_address text,
    username text,
    user_password text,
    logged_in_status Boolean
);

DROP TABLE IF EXISTS peeps;
CREATE TABLE peeps (
    id SERIAL PRIMARY KEY, 
    peep text,
    peep_dateime TIMESTAMP,
    user_id int,
    CONSTRAINT fk_users FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO users (name_of_user, email_address, username, user_password) VALUES ('Katie', 'Katie@hotmail.co.uk', 'katieuser', 'password123');