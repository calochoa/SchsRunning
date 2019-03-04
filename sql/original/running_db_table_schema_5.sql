DROP PROCEDURE IF EXISTS `GetTrackTopRaceIndividual`;

DELIMITER //
CREATE PROCEDURE `GetTrackTopRaceIndividual`(
	IN inputEventId INT, 
	IN inputGenderId TINYINT, 
	IN inputLimit INT
)
BEGIN

SELECT @rownum := @rownum + 1 AS myrank, t.* 
FROM (
	SELECT DISTINCT `event`, `firstname`, `lastname`, `RaceResult`.`time`, `raceTimeTypeId`, `stateMark`, `year`, `grade`, `competitorid`
	FROM `RaceResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Gender` 
	WHERE `eventId`=inputEventId AND `genderid`=inputGenderId 
	ORDER BY `RaceResult`.`time`, `year`, `lastname`, `firstname`
	LIMIT inputLimit
) t, 
(SELECT @rownum := 0) r;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTrackTopFieldIndividual`;

DELIMITER //
CREATE PROCEDURE `GetTrackTopFieldIndividual`(
	IN inputEventId INT, 
	IN inputGenderId TINYINT, 
	IN inputLimit INT
)
BEGIN

SELECT @rownum := @rownum + 1 AS myrank, t.* 
FROM (
	SELECT DISTINCT `event`, `firstname`, `lastname`, `footPartOfDistance`, `inchPartOfDistance`, `stateMark`, `year`, `grade`, `competitorid`
	FROM `FieldResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Gender` 
	WHERE `eventId`=inputEventId AND `genderid`=inputGenderId 
	ORDER BY `footPartOfDistance` DESC, `inchPartOfDistance` DESC, `year`, `lastname`, `firstname`
	LIMIT inputLimit
) t, 
(SELECT @rownum := 0) r;

END //
DELIMITER ;

COMMIT;



CALL GetTrackTopRaceIndividual(1,2,15);
CALL GetTrackTopFieldIndividual(29, 2, 20);