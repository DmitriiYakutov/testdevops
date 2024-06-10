CREATE TABLE author (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

INSERT INTO author(name) VALUES('Virginia Woolf');
INSERT INTO author(name) VALUES('Ibelive Icanflyev');