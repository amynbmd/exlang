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


/*
-- Seed database
--------------------------------------------------------------------------- USER ---------------------------------------------------------------------------
INSERT INTO USER (name, email, password) VALUES (
   'User 1',
   'user1@email.com',
   '$2b$12$GEEOuw336t3M9oOMMOMGxe403qZXRTbxSGw05gvxhD.gsTvVhfv1S'
);

INSERT INTO USER (name, email, password) VALUES (
   'User 2',
   'user2@email.com',
   '$2b$12$GEEOuw336t3M9oOMMOMGxe403qZXRTbxSGw05gvxhD.gsTvVhfv1S'
);

INSERT INTO USER (name, email, password) VALUES (
   'User 3',
   'user3@email.com',
   '$2b$12$GEEOuw336t3M9oOMMOMGxe403qZXRTbxSGw05gvxhD.gsTvVhfv1S'
);

INSERT INTO USER (name, email, password) VALUES (
   'User 4',
   'user4@email.com',
   '$2b$12$GEEOuw336t3M9oOMMOMGxe403qZXRTbxSGw05gvxhD.gsTvVhfv1S'
);

INSERT INTO USER (name, email, password) VALUES (
   'User 5',
   'user5@email.com',
   '$2b$12$GEEOuw336t3M9oOMMOMGxe403qZXRTbxSGw05gvxhD.gsTvVhfv1S'
);

INSERT INTO USER (name, email, password) VALUES (
   'User 6',
   'user6@email.com',
   '$2b$12$GEEOuw336t3M9oOMMOMGxe403qZXRTbxSGw05gvxhD.gsTvVhfv1S'
);

INSERT INTO USER (name, email, password) VALUES (
   'User 7',
   'user7@email.com',
   '$2b$12$GEEOuw336t3M9oOMMOMGxe403qZXRTbxSGw05gvxhD.gsTvVhfv1S'
);

INSERT INTO USER (name, email, password) VALUES (
   'User 8',
   'user8@email.com',
   '$2b$12$GEEOuw336t3M9oOMMOMGxe403qZXRTbxSGw05gvxhD.gsTvVhfv1S'
);

INSERT INTO USER (name, email, password) VALUES (
   'User 9',
   'user9@email.com',
   '$2b$12$GEEOuw336t3M9oOMMOMGxe403qZXRTbxSGw05gvxhD.gsTvVhfv1S'
);

INSERT INTO USER (name, email, password) VALUES (
   'User 10',
   'user10@email.com',
   '$2b$12$GEEOuw336t3M9oOMMOMGxe403qZXRTbxSGw05gvxhD.gsTvVhfv1S'
);

INSERT INTO USER (name, email, password) VALUES (
   'User 11',
   'user11@email.com',
   '$2b$12$GEEOuw336t3M9oOMMOMGxe403qZXRTbxSGw05gvxhD.gsTvVhfv1S'
);

INSERT INTO USER (name, email, password) VALUES (
   'User 12',
   'user12@email.com',
   '$2b$12$GEEOuw336t3M9oOMMOMGxe403qZXRTbxSGw05gvxhD.gsTvVhfv1S'
);

--------------------------------------------------------------------------- USER_PROFILE ---------------------------------------------------------------------------
INSERT INTO USER_PROFILE (email, word_of_the_day, isOnline, countryCode, picURL, bio, native_lang, level) VALUES (
   'user1@email.com',
   'word',
   'false',
   'US',
   'url',
   'bio',
   'en',
   'Intermediate'
);

INSERT INTO USER_PROFILE (email, word_of_the_day, isOnline, countryCode, picURL, bio, native_lang, level) VALUES (
   'user2@email.com',
   'word',
   'false',
   'US',
   'url',
   'bio',
   'en',
   'Intermediate'
);

INSERT INTO USER_PROFILE (email, word_of_the_day, isOnline, countryCode, picURL, bio, native_lang, level) VALUES (
   'user3@email.com',
   'word',
   'false',
   'US',
   'url',
   'bio',
   'en',
   'Intermediate'
);

INSERT INTO USER_PROFILE (email, word_of_the_day, isOnline, countryCode, picURL, bio, native_lang, level) VALUES (
   'user4@email.com',
   'word',
   'false',
   'US',
   'url',
   'bio',
   'en',
   'Intermediate'
);

INSERT INTO USER_PROFILE (email, word_of_the_day, isOnline, countryCode, picURL, bio, native_lang, level) VALUES (
   'user5@email.com',
   'word',
   'false',
   'US',
   'url',
   'bio',
   'en',
   'Intermediate'
);

INSERT INTO USER_PROFILE (email, word_of_the_day, isOnline, countryCode, picURL, bio, native_lang, level) VALUES (
   'user6@email.com',
   'word',
   'false',
   'US',
   'url',
   'bio',
   'en',
   'Intermediate'
);

INSERT INTO USER_PROFILE (email, word_of_the_day, isOnline, countryCode, picURL, bio, native_lang, level) VALUES (
   'user7@email.com',
   'word',
   'false',
   'US',
   'url',
   'bio',
   'en',
   'Intermediate'
);

INSERT INTO USER_PROFILE (email, word_of_the_day, isOnline, countryCode, picURL, bio, native_lang, level) VALUES (
   'user8@email.com',
   'word',
   'false',
   'US',
   'url',
   'bio',
   'en',
   'Intermediate'
);

INSERT INTO USER_PROFILE (email, word_of_the_day, isOnline, countryCode, picURL, bio, native_lang, level) VALUES (
   'user9@email.com',
   'word',
   'false',
   'US',
   'url',
   'bio',
   'en',
   'Intermediate'
);

INSERT INTO USER_PROFILE (email, word_of_the_day, isOnline, countryCode, picURL, bio, native_lang, level) VALUES (
   'user10@email.com',
   'word',
   'false',
   'US',
   'url',
   'bio',
   'en',
   'Intermediate'
);

INSERT INTO USER_PROFILE (email, word_of_the_day, isOnline, countryCode, picURL, bio, native_lang, level) VALUES (
   'user11@email.com',
   'word',
   'false',
   'US',
   'url',
   'bio',
   'en',
   'Intermediate'
);

INSERT INTO USER_PROFILE (email, word_of_the_day, isOnline, countryCode, picURL, bio, native_lang, level) VALUES (
   'user12@email.com',
   'word',
   'false',
   'US',
   'url',
   'bio',
   'en',
   'Intermediate'
);



--------------------------------------------------------------------------- LEARNING_LANG ---------------------------------------------------------------------------
INSERT INTO LEARNING_LANG (email, learning_lang) VALUES (
   'user1@email.com',
   'de'
);

INSERT INTO LEARNING_LANG (email, learning_lang) VALUES (
   'user2@email.com',
   'de'
);

INSERT INTO LEARNING_LANG (email, learning_lang) VALUES (
   'user3@email.com',
   'de'
);

INSERT INTO LEARNING_LANG (email, learning_lang) VALUES (
   'user4@email.com',
   'de'
);

INSERT INTO LEARNING_LANG (email, learning_lang) VALUES (
   'user5@email.com',
   'de'
);

INSERT INTO LEARNING_LANG (email, learning_lang) VALUES (
   'user6@email.com',
   'de'
);

INSERT INTO LEARNING_LANG (email, learning_lang) VALUES (
   'user7@email.com',
   'de'
);

INSERT INTO LEARNING_LANG (email, learning_lang) VALUES (
   'user8@email.com',
   'de'
);

INSERT INTO LEARNING_LANG (email, learning_lang) VALUES (
   'user9@email.com',
   'de'
);

INSERT INTO LEARNING_LANG (email, learning_lang) VALUES (
   'user10@email.com',
   'de'
);

INSERT INTO LEARNING_LANG (email, learning_lang) VALUES (
   'user11@email.com',
   'de'
);

INSERT INTO LEARNING_LANG (email, learning_lang) VALUES (
   'user12@email.com',
   'de'
);
*/