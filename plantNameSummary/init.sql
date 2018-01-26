BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `familyList` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `scientific`    TEXT NOT NULL DEFAULT 'default' UNIQUE,
    `korean`    TEXT DEFAULT 'None',
    `orderNo`   REAL NOT NULL DEFAULT 65535 UNIQUE
);
CREATE TABLE IF NOT EXISTS `genusList` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `familyId`  INTEGER NOT NULL DEFAULT 0,
    `name`  TEXT NOT NULL,
    FOREIGN KEY(`familyId`) REFERENCES `familyList`(`id`)
);
CREATE TABLE IF NOT EXISTS `intraSpecificClass` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `classText` TEXT UNIQUE
);
CREATE TABLE IF NOT EXISTS `speciesList` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `genusId`   INTEGER NOT NULL DEFAULT 0,
    `specificEpithet`   TEXT NOT NULL,
    `intraspecificClassId`  INTEGER NOT NULL DEFAULT 1,
    `intraspecificName` TEXT,
    `korean`    TEXT UNIQUE,
    `authorSpecific`    TEXT,
    `authorIntraspecific`   TEXT,
    FOREIGN KEY(`intraspecificClassId`) REFERENCES `intraSpecificClass`(`id`),
    FOREIGN KEY(`genusId`) REFERENCES `genusList`(`id`)
);
CREATE TABLE IF NOT EXISTS `inputList` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`  TEXT NOT NULL DEFAULT 'None'
);
COMMIT;
