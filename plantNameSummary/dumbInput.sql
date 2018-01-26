INSERT INTO `familyList` (id,scientific,korean,orderNo) VALUES (0,'None',NULL,0),
 (1,'Faaa','과가가가',3),
 (2,'Fbbb','과가가나',2),
 (3,'Fccc','과나나가',5);
INSERT INTO `genusList` (id,familyId,name) VALUES (0,0,'None'),
 (1,1,'Gaaa'),
 (2,2,'Gaba'),
 (3,2,'Gcaa'),
 (4,3,'Gaaa'),
 (5,1,'Gabc'),
 (6,0,'Aaaa');
INSERT INTO `intraSpecificClass` (id,classText) VALUES (1,NULL),
 (2,'subsp.'),
 (3,'var.'),
 (4,'subvar.'),
 (5,'f.'),
 (6,'subf.');
INSERT INTO `speciesList` (id,genusId,specificEpithet,intraspecificClassId,intraspecificName,korean,authorSpecific,authorIntraspecific) VALUES (1,1,'Saaa',1,NULL,'가가가','James',NULL),
 (2,1,'Saab',1,NULL,'나가나','L.',NULL),
 (3,3,'Saca',3,'Vaaa',NULL,'L.','Somebody'),
 (4,2,'Scca',5,'Fccc','다다다',NULL,'L.');
INSERT INTO `inputList` (id,name) VALUES (1,'다다다'),
 (2,'ㄱㄴㄱ');
