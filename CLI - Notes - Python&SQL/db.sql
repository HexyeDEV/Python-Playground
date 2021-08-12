CREATE DATABASE IF NOT EXISTS cli_notes;
use playground_mysql_python;

CREATE TABLE users(
  id        int(25) auto_increment not null,
  name      varchar(100),
  surname   varchar(255),
  email     varchar(255) not null,
  password  varchar(255) not null,
  date      date not null,
  CONSTRAINT pk_users PRIMARY KEY(id),
  CONSTRAINT uq_email UNIQUE(email)
)Engine=InnoDb;

CREATE TABLE notes(
    id      int(25) auto_increment not null,
    user_id int(25) not null,
    title   varchar(255) not null,
    content MEDIUMTEXT,
    date    date not null,
    CONSTRAINT pk_notes PRIMARY KEY(id),
    CONSTRAINT fk_note_user FOREIGN KEY(user_id) REFERENCES users(id)
)Engine=InnoDb;
