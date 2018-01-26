BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `familyList` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `scientific`    TEXT NOT NULL UNIQUE,
    `korean`    TEXT UNIQUE,
    `orderNo`   INTEGER NOT NULL UNIQUE
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
    FOREIGN KEY(`genusId`) REFERENCES `genusList`(`id`),
    FOREIGN KEY(`intraspecificClassId`) REFERENCES `intraSpecificClass`(`id`)
);
CREATE TABLE IF NOT EXISTS `inputList` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`  TEXT NOT NULL DEFAULT 'None'
);
COMMIT;
