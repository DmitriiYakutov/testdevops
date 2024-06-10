CREATE TABLE author (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

INSERT INTO author(id, name) VALUES(1, 'Virginia Woolf');
INSERT INTO author(id, name) VALUES(2, 'Ibelive Icanflyev');