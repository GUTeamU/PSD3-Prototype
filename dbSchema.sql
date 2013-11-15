CREATE TABLE session_types (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  label TEXT
);

CREATE TABLE sessions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  session_type_id INTEGER,
  starts INTEGER,
  ends INTEGER
);

CREATE TABLE session_users (
  user_id INTEGER,
  session_id INTEGER,
  attended INTEGER DEFAULT 0
);

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE,
  full_name TEXT,
  barcode INTEGER
);
