BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `sources` (
    `no`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `author`    TEXT,
    `year`  INTEGER,
    `title` TEXT,
    `publisher` TEXT,
    `pages` TEXT,
    `url`   INTEGER,
    `etc`   INTEGER
);
CREATE TABLE IF NOT EXISTS `sorts` (
    `no`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `field` TEXT
);
CREATE TABLE IF NOT EXISTS `data` (
    `no`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `sort`  INTEGER,
    `datum` TEXT,
    `source`    INTEGER
);
COMMIT;
