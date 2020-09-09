-- Author hirata
CREATE DATABASE IF NOT EXISTS yuru;
Use yuru;

CREATE TABLE IF NOT EXISTS users (
id                     bigint(20) NOT NULL AUTO_INCREMENT,
username               varchar (256) NULL,
email                  varchar (256) NULL,
hashed_password        varchar (256) NULL,
user_id                varchar (256) NULL,
status                 int NULL,
comment                varchar (256) NULL,
status_update_at       varchar (256) NULL,
longitude              double NULL,
latitude               double NULL,
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS chat_rooms (
id                     bigint(20) NOT NULL AUTO_INCREMENT,
deleted                tinyint(4) DEFAULT '0',
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS chats (
id                     bigint(20) NOT NULL AUTO_INCREMENT,
user_id                bigint(20) NOT NULL,
chat_room_id           bigint(20) NOT NULL,
content                varchar (256) NULL,
deleted                tinyint(4) DEFAULT '0',
created_at             bigint(20) NULL,
PRIMARY KEY (id),
KEY index_messages_on_user_id (user_id),
KEY index_messages_on_chat_room_id (chat_room_id),
CONSTRAINT fk_1 FOREIGN KEY (user_id) REFERENCES users (id),
CONSTRAINT fk_2 FOREIGN KEY (chat_room_id) REFERENCES chat_rooms (id)
);

CREATE TABLE IF NOT EXISTS friends (
id                     bigint(20) NOT NULL AUTO_INCREMENT,
user_1_id              bigint(20) NOT NULL,
user_2_id              bigint(20) NOT NULL,
PRIMARY KEY (id),
KEY index_friends_on_user_1_id (user_1_id),
KEY index_friends_on_user_2_id (user_2_id),
UNIQUE index_friends_on_user_1_2_id (user_1_id, user_2_id),
CONSTRAINT fk_3 FOREIGN KEY (user_1_id) REFERENCES users (id),
CONSTRAINT fk_4 FOREIGN KEY (user_2_id) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS favorites (
id                     bigint(20) NOT NULL AUTO_INCREMENT,
user_id                bigint(20) NOT NULL,
target_user_id         bigint(20) NOT NULL,
PRIMARY KEY (id),
KEY index_favorites_on_user_id (user_id),
KEY index_favorites_on_target_user_id (target_user_id),
CONSTRAINT fk_5 FOREIGN KEY (user_id) REFERENCES users (id),
CONSTRAINT fk_6 FOREIGN KEY (target_user_id) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS user_chat_rooms (
id                     bigint(20) NOT NULL AUTO_INCREMENT,
user_id                bigint(20) NOT NULL,
chat_room_id           bigint(20) NOT NULL,
valid                  tinyint(4) DEFAULT '0',
PRIMARY KEY (id),
KEY index_user_chat_rooms_on_user_id (user_id),
KEY index_user_chat_rooms_on_chat_room_id (chat_room_id),
CONSTRAINT fk_7 FOREIGN KEY (user_id) REFERENCES users (id),
CONSTRAINT fk_8 FOREIGN KEY (chat_room_id) REFERENCES chat_rooms (id)
);

CREATE TABLE IF NOT EXISTS timelines (
id                     bigint(20) NOT NULL AUTO_INCREMENT,
user_id                bigint(20) NOT NULL,
event_date             bigint(20) NOT NULL,
place                  varchar (256) NULL,
content                varchar (1024) NULL,
deleted                tinyint(4) DEFAULT '0',
PRIMARY KEY (id),
KEY index_time_lines_on_user_id (user_id),
CONSTRAINT fk_9 FOREIGN KEY (user_id) REFERENCES users (id)
);
