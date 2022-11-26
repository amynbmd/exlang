select * from AVAILABILITY;

select * from FRIENDS;

select * from INTERESTS;

select * from LEARNING_LANG;

select * from USER;

select * from USER_PROFILE;


CREATE TABLE USER(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   name           TEXT      NOT NULL,
   email          CHAR(100)       NOT NULL,
   password       CHAR(100)
);


CREATE TABLE USER_PROFIKE(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   email          CHAR(100)       NOT NULL,
   word_of_the_day          CHAR(200),
   isOnline          BOOLEAN,
   countryCode          CHAR(100),
   picURL          CHAR(250),
   bio          CHAR(1000),
   native_lang          CHAR(100),
   level          CHAR(100)
);


CREATE TABLE LEARNING_LANG(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   email          CHAR(100)       NOT NULL,
   learning_lang       CHAR(100)
);


CREATE TABLE INTERESTS(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   email          CHAR(100)       NOT NULL,
   interest       CHAR(100)
);


CREATE TABLE FRIENDS(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   email          CHAR(100)       NOT NULL,
   friend_name       CHAR(100)
);

CREATE TABLE AVAILABILITY(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   email          CHAR(100)       NOT NULL,
   time       CHAR(100)
);
