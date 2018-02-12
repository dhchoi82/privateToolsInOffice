BEGIN TRANSACTION;
DROP TABLE IF EXISTS `inputList`;
CREATE TABLE `inputList` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `unitNum`   INTEGER,
    `releveNum` INTEGER,
    `name`  TEXT NOT NULL DEFAULT 'None',
    `cover` REAL
);
COMMIT;
