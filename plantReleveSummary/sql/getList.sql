SELECT DISTINCT familyList.scientific AS familyName,
    familyList.korean AS familyKorean,
    genusList.name AS genusName,
    specificEpithet,
    intraSpecificClass.classText AS intraClass,
    intraspecificName,
    inputList.name AS specificKorean,
    authorSpecific,
    authorIntraspecific
    FROM inputList
        LEFT JOIN speciesList ON speciesList.korean=inputList.name
        LEFT JOIN genusList ON genusList.id=speciesList.genusId
        LEFT JOIN familyList ON familyList.id=genusList.familyId
        LEFT JOIN intraSpecificClass ON intraSpecificClass.id=speciesList.intraspecificClassId
    ORDER BY familyList.orderNo ASC, genusList.name ASC,
        specificEpithet ASC, intraSpecificClass.classText ASC,
        intraspecificName ASC;
