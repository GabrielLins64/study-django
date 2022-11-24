CREATE USER djuser WITH ENCRYPTED PASSWORD 'djuser';
CREATE DATABASE django_tutorial_db;
GRANT ALL PRIVILEGES ON DATABASE django_tutorial_db TO djuser;
