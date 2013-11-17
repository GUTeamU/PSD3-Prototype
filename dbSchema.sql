PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
DROP TABLE sessions;
DROP TABLE session_types;
DROP TABLE users;
DROP TABLE session_users;
CREATE TABLE session_types (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  label TEXT
);
INSERT INTO "session_types" VALUES(1,'PSD3');
INSERT INTO "session_types" VALUES(2,'Alg3');
INSERT INTO "session_types" VALUES(3,'AP3');
INSERT INTO "session_types" VALUES(4,'PL3');
CREATE TABLE sessions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  session_type_id INTEGER,
  label TEXT,
  starts INTEGER,
  ends INTEGER,
  capacity INTEGER
);
INSERT INTO "sessions" VALUES(1,1,'Laboratory 1',1380546000,1380553200,NULL);
INSERT INTO "sessions" VALUES(2,1,'Laboratory 2',1381150800,1381158000,NULL);
INSERT INTO "sessions" VALUES(3,1,'Laboratory 3',1381755600,1381762800,NULL);
INSERT INTO "sessions" VALUES(4,1,'Laboratory 4',1382360400,1382367600,NULL);
INSERT INTO "sessions" VALUES(5,1,'Laboratory 5',1382968800,1382976000,NULL);
INSERT INTO "sessions" VALUES(6,1,'Laboratory 6',1383573600,1383580800,NULL);
INSERT INTO "sessions" VALUES(7,1,'Laboratory 7',1384178400,1384185600,NULL);
INSERT INTO "sessions" VALUES(8,1,'Laboratory 8',1384783200,1384790400,NULL);
INSERT INTO "sessions" VALUES(9,1,'Laboratory 9',1385388000,1385395200,NULL);
INSERT INTO "sessions" VALUES(10,2,'Laboratory 1',1380546000,1380553200,NULL);
INSERT INTO "sessions" VALUES(11,2,'Laboratory 2',1381150800,1381158000,NULL);
INSERT INTO "sessions" VALUES(12,2,'Laboratory 3',1381755600,1381762800,NULL);
INSERT INTO "sessions" VALUES(13,2,'Laboratory 4',1382360400,1382367600,NULL);
INSERT INTO "sessions" VALUES(14,2,'Laboratory 5',1382968800,1382976000,NULL);
INSERT INTO "sessions" VALUES(15,2,'Laboratory 6',1383573600,1383580800,NULL);
INSERT INTO "sessions" VALUES(16,2,'Laboratory 7',1384178400,1384185600,NULL);
INSERT INTO "sessions" VALUES(17,2,'Laboratory 8',1384783200,1384790400,NULL);
INSERT INTO "sessions" VALUES(18,2,'Laboratory 9',1385388000,1385395200,NULL);
INSERT INTO "sessions" VALUES(19,3,'Laboratory 1',1380546000,1380553200,NULL);
INSERT INTO "sessions" VALUES(20,3,'Laboratory 2',1381150800,1381158000,NULL);
INSERT INTO "sessions" VALUES(21,3,'Laboratory 3',1381755600,1381762800,NULL);
INSERT INTO "sessions" VALUES(22,3,'Laboratory 4',1382360400,1382367600,NULL);
INSERT INTO "sessions" VALUES(23,3,'Laboratory 5',1382968800,1382976000,NULL);
INSERT INTO "sessions" VALUES(24,3,'Laboratory 6',1383573600,1383580800,NULL);
INSERT INTO "sessions" VALUES(25,3,'Laboratory 7',1384178400,1384185600,NULL);
INSERT INTO "sessions" VALUES(26,3,'Laboratory 8',1384783200,1384790400,NULL);
INSERT INTO "sessions" VALUES(27,3,'Laboratory 9',1385388000,1385395200,NULL);
INSERT INTO "sessions" VALUES(28,4,'Laboratory 1',1380546000,1380553200,NULL);
INSERT INTO "sessions" VALUES(29,4,'Laboratory 2',1381150800,1381158000,NULL);
INSERT INTO "sessions" VALUES(30,4,'Laboratory 3',1381755600,1381762800,NULL);
INSERT INTO "sessions" VALUES(31,4,'Laboratory 4',1382360400,1382367600,NULL);
INSERT INTO "sessions" VALUES(32,4,'Laboratory 5',1382968800,1382976000,NULL);
INSERT INTO "sessions" VALUES(33,4,'Laboratory 6',1383573600,1383580800,NULL);
INSERT INTO "sessions" VALUES(34,4,'Laboratory 7',1384178400,1384185600,NULL);
INSERT INTO "sessions" VALUES(35,4,'Laboratory 8',1384783200,1384790400,NULL);
INSERT INTO "sessions" VALUES(36,4,'Laboratory 9',1385388000,1385395200,NULL);
CREATE TABLE session_users (
  user_id INTEGER,
  session_id INTEGER,
  attended INTEGER DEFAULT 0
);
INSERT INTO "session_users" VALUES(1,1,0);
INSERT INTO "session_users" VALUES(2,1,0);
INSERT INTO "session_users" VALUES(3,1,0);
INSERT INTO "session_users" VALUES(4,1,0);
INSERT INTO "session_users" VALUES(5,1,0);
INSERT INTO "session_users" VALUES(1,2,0);
INSERT INTO "session_users" VALUES(2,2,0);
INSERT INTO "session_users" VALUES(3,2,0);
INSERT INTO "session_users" VALUES(4,2,0);
INSERT INTO "session_users" VALUES(5,2,0);
INSERT INTO "session_users" VALUES(1,3,0);
INSERT INTO "session_users" VALUES(2,3,0);
INSERT INTO "session_users" VALUES(3,3,0);
INSERT INTO "session_users" VALUES(4,3,0);
INSERT INTO "session_users" VALUES(5,3,0);
INSERT INTO "session_users" VALUES(1,4,0);
INSERT INTO "session_users" VALUES(2,4,0);
INSERT INTO "session_users" VALUES(3,4,0);
INSERT INTO "session_users" VALUES(4,4,0);
INSERT INTO "session_users" VALUES(5,4,0);
INSERT INTO "session_users" VALUES(1,5,0);
INSERT INTO "session_users" VALUES(2,5,0);
INSERT INTO "session_users" VALUES(3,5,0);
INSERT INTO "session_users" VALUES(4,5,0);
INSERT INTO "session_users" VALUES(5,5,0);
INSERT INTO "session_users" VALUES(1,6,0);
INSERT INTO "session_users" VALUES(2,6,0);
INSERT INTO "session_users" VALUES(3,6,0);
INSERT INTO "session_users" VALUES(4,6,0);
INSERT INTO "session_users" VALUES(5,6,0);
INSERT INTO "session_users" VALUES(1,7,0);
INSERT INTO "session_users" VALUES(2,7,0);
INSERT INTO "session_users" VALUES(3,7,0);
INSERT INTO "session_users" VALUES(4,7,0);
INSERT INTO "session_users" VALUES(5,7,0);
INSERT INTO "session_users" VALUES(1,8,0);
INSERT INTO "session_users" VALUES(2,8,0);
INSERT INTO "session_users" VALUES(3,8,0);
INSERT INTO "session_users" VALUES(4,8,0);
INSERT INTO "session_users" VALUES(5,8,0);
INSERT INTO "session_users" VALUES(1,9,0);
INSERT INTO "session_users" VALUES(2,9,0);
INSERT INTO "session_users" VALUES(3,9,0);
INSERT INTO "session_users" VALUES(4,9,0);
INSERT INTO "session_users" VALUES(5,9,0);
INSERT INTO "session_users" VALUES(1,10,0);
INSERT INTO "session_users" VALUES(2,10,0);
INSERT INTO "session_users" VALUES(3,10,0);
INSERT INTO "session_users" VALUES(4,10,0);
INSERT INTO "session_users" VALUES(5,10,0);
INSERT INTO "session_users" VALUES(1,11,0);
INSERT INTO "session_users" VALUES(2,11,0);
INSERT INTO "session_users" VALUES(3,11,0);
INSERT INTO "session_users" VALUES(4,11,0);
INSERT INTO "session_users" VALUES(5,11,0);
INSERT INTO "session_users" VALUES(1,12,0);
INSERT INTO "session_users" VALUES(2,12,0);
INSERT INTO "session_users" VALUES(3,12,0);
INSERT INTO "session_users" VALUES(4,12,0);
INSERT INTO "session_users" VALUES(5,12,0);
INSERT INTO "session_users" VALUES(1,13,0);
INSERT INTO "session_users" VALUES(2,13,0);
INSERT INTO "session_users" VALUES(3,13,0);
INSERT INTO "session_users" VALUES(4,13,0);
INSERT INTO "session_users" VALUES(5,13,0);
INSERT INTO "session_users" VALUES(1,14,0);
INSERT INTO "session_users" VALUES(2,14,0);
INSERT INTO "session_users" VALUES(3,14,0);
INSERT INTO "session_users" VALUES(4,14,0);
INSERT INTO "session_users" VALUES(5,14,0);
INSERT INTO "session_users" VALUES(1,15,0);
INSERT INTO "session_users" VALUES(2,15,0);
INSERT INTO "session_users" VALUES(3,15,0);
INSERT INTO "session_users" VALUES(4,15,0);
INSERT INTO "session_users" VALUES(5,15,0);
INSERT INTO "session_users" VALUES(1,16,0);
INSERT INTO "session_users" VALUES(2,16,0);
INSERT INTO "session_users" VALUES(3,16,0);
INSERT INTO "session_users" VALUES(4,16,0);
INSERT INTO "session_users" VALUES(5,16,0);
INSERT INTO "session_users" VALUES(1,17,0);
INSERT INTO "session_users" VALUES(2,17,0);
INSERT INTO "session_users" VALUES(3,17,0);
INSERT INTO "session_users" VALUES(4,17,0);
INSERT INTO "session_users" VALUES(5,17,0);
INSERT INTO "session_users" VALUES(1,18,0);
INSERT INTO "session_users" VALUES(2,18,0);
INSERT INTO "session_users" VALUES(3,18,0);
INSERT INTO "session_users" VALUES(4,18,0);
INSERT INTO "session_users" VALUES(5,18,0);
INSERT INTO "session_users" VALUES(1,19,0);
INSERT INTO "session_users" VALUES(2,19,0);
INSERT INTO "session_users" VALUES(3,19,0);
INSERT INTO "session_users" VALUES(4,19,0);
INSERT INTO "session_users" VALUES(5,19,0);
INSERT INTO "session_users" VALUES(1,20,0);
INSERT INTO "session_users" VALUES(2,20,0);
INSERT INTO "session_users" VALUES(3,20,0);
INSERT INTO "session_users" VALUES(4,20,0);
INSERT INTO "session_users" VALUES(5,20,0);
INSERT INTO "session_users" VALUES(1,21,0);
INSERT INTO "session_users" VALUES(2,21,0);
INSERT INTO "session_users" VALUES(3,21,0);
INSERT INTO "session_users" VALUES(4,21,0);
INSERT INTO "session_users" VALUES(5,21,0);
INSERT INTO "session_users" VALUES(1,22,0);
INSERT INTO "session_users" VALUES(2,22,0);
INSERT INTO "session_users" VALUES(3,22,0);
INSERT INTO "session_users" VALUES(4,22,0);
INSERT INTO "session_users" VALUES(5,22,0);
INSERT INTO "session_users" VALUES(1,23,0);
INSERT INTO "session_users" VALUES(2,23,0);
INSERT INTO "session_users" VALUES(3,23,0);
INSERT INTO "session_users" VALUES(4,23,0);
INSERT INTO "session_users" VALUES(5,23,0);
INSERT INTO "session_users" VALUES(1,24,0);
INSERT INTO "session_users" VALUES(2,24,0);
INSERT INTO "session_users" VALUES(3,24,0);
INSERT INTO "session_users" VALUES(4,24,0);
INSERT INTO "session_users" VALUES(5,24,0);
INSERT INTO "session_users" VALUES(1,25,0);
INSERT INTO "session_users" VALUES(2,25,0);
INSERT INTO "session_users" VALUES(3,25,0);
INSERT INTO "session_users" VALUES(4,25,0);
INSERT INTO "session_users" VALUES(5,25,0);
INSERT INTO "session_users" VALUES(1,26,0);
INSERT INTO "session_users" VALUES(2,26,0);
INSERT INTO "session_users" VALUES(3,26,0);
INSERT INTO "session_users" VALUES(4,26,0);
INSERT INTO "session_users" VALUES(5,26,0);
INSERT INTO "session_users" VALUES(1,27,0);
INSERT INTO "session_users" VALUES(2,27,0);
INSERT INTO "session_users" VALUES(3,27,0);
INSERT INTO "session_users" VALUES(4,27,0);
INSERT INTO "session_users" VALUES(5,27,0);
INSERT INTO "session_users" VALUES(1,28,0);
INSERT INTO "session_users" VALUES(2,28,0);
INSERT INTO "session_users" VALUES(3,28,0);
INSERT INTO "session_users" VALUES(4,28,0);
INSERT INTO "session_users" VALUES(5,28,0);
INSERT INTO "session_users" VALUES(1,29,0);
INSERT INTO "session_users" VALUES(2,29,0);
INSERT INTO "session_users" VALUES(3,29,0);
INSERT INTO "session_users" VALUES(4,29,0);
INSERT INTO "session_users" VALUES(5,29,0);
INSERT INTO "session_users" VALUES(1,30,0);
INSERT INTO "session_users" VALUES(2,30,0);
INSERT INTO "session_users" VALUES(3,30,0);
INSERT INTO "session_users" VALUES(4,30,0);
INSERT INTO "session_users" VALUES(5,30,0);
INSERT INTO "session_users" VALUES(1,31,0);
INSERT INTO "session_users" VALUES(2,31,0);
INSERT INTO "session_users" VALUES(3,31,0);
INSERT INTO "session_users" VALUES(4,31,0);
INSERT INTO "session_users" VALUES(5,31,0);
INSERT INTO "session_users" VALUES(1,32,0);
INSERT INTO "session_users" VALUES(2,32,0);
INSERT INTO "session_users" VALUES(3,32,0);
INSERT INTO "session_users" VALUES(4,32,0);
INSERT INTO "session_users" VALUES(5,32,0);
INSERT INTO "session_users" VALUES(1,33,0);
INSERT INTO "session_users" VALUES(2,33,0);
INSERT INTO "session_users" VALUES(3,33,0);
INSERT INTO "session_users" VALUES(4,33,0);
INSERT INTO "session_users" VALUES(5,33,0);
INSERT INTO "session_users" VALUES(1,34,0);
INSERT INTO "session_users" VALUES(2,34,0);
INSERT INTO "session_users" VALUES(3,34,0);
INSERT INTO "session_users" VALUES(4,34,0);
INSERT INTO "session_users" VALUES(5,34,0);
INSERT INTO "session_users" VALUES(1,35,0);
INSERT INTO "session_users" VALUES(2,35,0);
INSERT INTO "session_users" VALUES(3,35,0);
INSERT INTO "session_users" VALUES(4,35,0);
INSERT INTO "session_users" VALUES(5,35,0);
INSERT INTO "session_users" VALUES(1,36,0);
INSERT INTO "session_users" VALUES(2,36,0);
INSERT INTO "session_users" VALUES(3,36,0);
INSERT INTO "session_users" VALUES(4,36,0);
INSERT INTO "session_users" VALUES(5,36,0);
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE,
  full_name TEXT,
  barcode INTEGER
);
INSERT INTO "users" VALUES(1,'1003492c','Michael Cromie',12345678536014);
INSERT INTO "users" VALUES(2,'1102103l','Fraser Leishman',23456789457015);
INSERT INTO "users" VALUES(3,'1102115m','Andrew McDonald',34567890467016);
INSERT INTO "users" VALUES(4,'1102374p','Matthew Paterson',45678901400017);
INSERT INTO "users" VALUES(5,'2039411m','Edvin Malinovskis',56789901645017);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('users',5);
INSERT INTO "sqlite_sequence" VALUES('session_types',4);
INSERT INTO "sqlite_sequence" VALUES('sessions',36);
COMMIT;
