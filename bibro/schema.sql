DROP TABLE IF EXISTS books;

CREATE TABLE books (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  author TEXT,
  publisher TEXT,
  publish_year INTEGER
);
