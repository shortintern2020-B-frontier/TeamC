CREATE DATABASE IF NOT EXISTS yuru;

CREATE TABLE IF NOT EXISTS users (
id                     bigint(20) NOT NULL AUTO_INCREMENT,
username               varchar (256) NULL,
email                  varchar (256) NULL,
hashed_password        varchar (256) NULL,
user_id                varchar (256) NULL,
status                 int NULL,
comment                varchar (256) NULL,
PRIMARY KEY (id)
);