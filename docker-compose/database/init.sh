#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER chat_user WITH PASSWORD 'chat_password';
    CREATE DATABASE chat_db;
    GRANT ALL PRIVILEGES ON DATABASE chat_db TO chat_user;
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER hash_user WITH PASSWORD 'hash_password';
    CREATE DATABASE hash_db;
    GRANT ALL PRIVILEGES ON DATABASE hash_db TO hash_user;
EOSQL