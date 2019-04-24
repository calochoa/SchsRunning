USE `highSchoolRunning`;




DROP PROCEDURE IF EXISTS `GetTopXcIndividual`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTopXcIndividual`(
	IN `inputCourseId` INT, 
	IN `inputGenderId` TINYINT, 
	IN `inputLimit` INT
)
BEGIN

SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	-- second, join the best times with athlete information and sort by best time
    -- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
	SELECT DISTINCT `firstname`, `lastname`, `Result`.`time`, `pace`, `year`, `grade`, `competitorid`
	FROM `Result` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` 
		NATURAL JOIN `Gender` NATURAL JOIN `Race` RIGHT JOIN (
			-- first, get the best time for a xc athlete by course and gender
			SELECT `athleteId`, MIN(time) `best_time`
			FROM `Result` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` 
				NATURAL JOIN `Gender` NATURAL JOIN `Race` NATURAL JOIN `Course` 
			WHERE `courseid`=`inputCourseId` AND `genderid`=`inputGenderId` AND `grade` != 0
			GROUP BY `athleteId` 
		) `best` ON `Athlete`.`athleteId`=`best`.`athleteId` AND `Result`.`time`=`best`.`best_time`
	WHERE `courseid`=`inputCourseId` AND `genderid`=`inputGenderId` AND YEAR(`Race`.`date`)=`year`
	ORDER BY `Result`.`time`
	LIMIT `inputLimit`
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetCourseInfo`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetCourseInfo`(
	IN `inputCourseId` INT
)
BEGIN

SELECT `courseid`, `coursename`, `coursedistance`, `city`, `state`, `coursetype` 
FROM `Course` NATURAL JOIN `Location` NATURAL JOIN `State` NATURAL JOIN `CourseType` 
WHERE `courseid`=`inputCourseId`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTopTeamCourse`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTopTeamCourse`(
	IN `inputCourseId` INT, 
	IN `inputGenderId` TINYINT, 
	IN `inputLimit` INT
)
BEGIN

-- fifth, add myrank number column
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	-- fourth, get the best time for each year and sort by best team time
	SELECT `yr` AS `Year`, 
		MIN(`team_time`) AS `Team Time`,
		MIN(`team_avg`) AS `Avg. Ind. Time`, 
		SUBSTRING_INDEX(GROUP_CONCAT(`raceid` ORDER BY `team_time` ASC SEPARATOR "#"), "#", 1) AS `Race ID`,
		SUBSTRING_INDEX(GROUP_CONCAT(`competitors` ORDER BY `team_time` ASC SEPARATOR "#"), "#", 1) AS `Competitors`
	FROM (
		SELECT YEAR(`date`) `yr`, `Result`.`raceid`, 
			SEC_TO_TIME(AVG(TIME_TO_SEC(`time`))) AS `team_avg`, 
			SEC_TO_TIME(SUM(TIME_TO_SEC(`time`))) AS `team_time`, 
			GROUP_CONCAT(`competitorid` ORDER BY `time` ASC) AS `competitors`
		FROM `Result` NATURAL JOIN `Race` INNER JOIN (
				-- second, order competitors for each race by fastest time
                -- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
				SELECT `raceid`, GROUP_CONCAT(CONCAT(`competitorid`,":",`raceid`) ORDER BY time ASC) AS `finisher_key` 
				FROM `Result` NATURAL JOIN `Race` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` 
				WHERE `genderid`=`inputGenderId` AND YEAR(`Race`.`date`)=`year` AND `raceid` IN (
					SELECT `raceid` 
					FROM (
						-- first, get races that have at least 5 results
						-- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
						SELECT `raceid`, COUNT(`raceid`) AS `num_racers` 
						FROM `Result` NATURAL JOIN `Race` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` 
						WHERE `courseid`=`inputCourseId` AND `genderid`=`inputGenderId` AND YEAR(`Race`.`date`)=`year`
						GROUP BY `raceid`
					) `num_racers_table`
					WHERE `num_racers` >= 5
				)
				GROUP BY `raceid`
			) `finisher_tbl` ON `Result`.`raceid`=`finisher_tbl`.`raceid`
			-- third, retrieve only the fastest 5 competitors for each race
			AND FIND_IN_SET(CONCAT(`Result`.`competitorid`,":",`Result`.`raceid`), `finisher_tbl`.`finisher_key`) BETWEEN 1 AND 5
		GROUP BY `Result`.`raceid`
		ORDER BY `yr`, `team_time`
	) `team_times` 
	GROUP BY `yr`
	ORDER BY MIN(`team_time`)
	LIMIT `inputLimit`
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetXcRunnerResults`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetXcRunnerResults`(
	IN `inputAthleteId` INT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
SELECT `time`, `pace`, `grade`, `date`, `racename`, `coursename`, `coursedistance`, 
	`racecondition`, `firstname`, `lastname`, `raceid`, `genderId`
FROM `Result` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Race` 
	NATURAL JOIN `RaceName` NATURAL JOIN `RaceCondition` NATURAL JOIN `Course`
WHERE `athleteid`=`inputAthleteId` AND YEAR(`Race`.`date`)=`year`
ORDER BY date DESC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetXcRunners`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetXcRunners`(
	IN `inputGenderIds` VARCHAR(15)
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
SELECT `athleteid`, `firstname`, `lastname`,
	GROUP_CONCAT(DISTINCT `year` ORDER BY `year` ASC SEPARATOR ", ") `years`
FROM `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Gender` 
	NATURAL JOIN `Result` NATURAL JOIN `Race` 
WHERE FIND_IN_SET(`genderId`, `inputGenderIds`) AND YEAR(`Race`.`date`)=`year`
GROUP BY `athleteid`
ORDER BY `lastname`, `firstname`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetXcResultsByRaceCompetitor`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetXcResultsByRaceCompetitor`(
	IN `inputRaceIds` VARCHAR(255),
	IN `inputCompetitorIds` VARCHAR(1023)
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
SELECT `raceid`, `competitorid`, `time`, `pace`, `grade`, `firstname`, `lastname`
FROM `Result` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Race` 
WHERE FIND_IN_SET(`raceid`, `inputRaceIds`) 
	AND FIND_IN_SET(`competitorid`, `inputCompetitorIds`) 
    AND YEAR(`Race`.`date`)=`year`
ORDER BY time;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetXcCompetitorsByYear`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetXcCompetitorsByYear`(
	IN `inputYear` INT, 
	IN `inputGenderId` INT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
SELECT DISTINCT `competitorid`, `year`, `grade`, `firstname`, `lastname`, `gender` 
FROM `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Gender`  
	NATURAL JOIN `Result` NATURAL JOIN `Race` 
WHERE `year`=`inputYear` AND `genderid`=`inputGenderId` AND `grade` != 0 
	AND YEAR(`Race`.`date`)=`year`
ORDER BY `lastname`, `firstname`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetXcRacesByYear`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetXcRacesByYear`(
	IN `inputYear` INT 
)
BEGIN

SELECT `raceid`, `date`, `racename`, `coursename`, `coursedistance`
FROM `Race` NATURAL JOIN `RaceName` NATURAL JOIN `Course` 
WHERE YEAR(`date`)=`inputYear` AND `raceid` >=1000000
ORDER BY `date` DESC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetXcCompetitorResults`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetXcCompetitorResults`(
	IN `inputCompetitorId` VARCHAR(15)
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
SELECT `time`, `pace`, `grade`, `date`, `racename`, `coursename`, `coursedistance`, 
	`racecondition`, `firstname`, `lastname`, `year`, `raceid`, `athleteId`
FROM `Result` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Race` 
	NATURAL JOIN `RaceName` NATURAL JOIN `RaceCondition` NATURAL JOIN `Course`
WHERE `competitorId`=`inputCompetitorId` AND YEAR(`Race`.`date`)=`year`
ORDER BY date DESC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetAllXcRaceResults`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetAllXcRaceResults`(
	IN `inputRaceId` INT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	SELECT `time`, `pace`, `grade`, `date`, `racename`, `coursename`, `coursedistance`, 
		`racecondition`, `firstname`, `lastname`, `year`, `competitorid`
	FROM `Result` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Race` 
		NATURAL JOIN `RaceName` NATURAL JOIN `RaceCondition` NATURAL JOIN `Course`
	WHERE `raceid`=`inputRaceId` AND YEAR(`Race`.`date`)=`year`
	ORDER BY time ASC
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetXcRaceResults`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetXcRaceResults`(
	IN `inputRaceId` INT,
	IN `inputGenderId` INT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	SELECT `time`, `pace`, `grade`, `date`, `racename`, `coursename`, `coursedistance`,
		`racecondition`, `firstname`, `lastname`, `year`, `competitorid`
	FROM `Result` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Race` 
		NATURAL JOIN `RaceName` NATURAL JOIN `RaceCondition` NATURAL JOIN `Course`
	WHERE `raceid`=`inputRaceId` AND `genderid`=`inputGenderId` AND YEAR(`Race`.`date`)=`year`
	ORDER BY time ASC
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTopXcIndividualByGrade`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTopXcIndividualByGrade`(
	IN `inputCourseId` INT, 
	IN `inputGenderId` TINYINT, 
	IN `inputGrade` TINYINT, 
	IN `inputLimit` INT
)
BEGIN

SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	-- second, join the best times with runner information and sort by best time
	-- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
	SELECT DISTINCT `firstname`, `lastname`, `Result`.`time`, `pace`, `year`, `grade`, `competitorid`
	FROM `Result` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Gender` NATURAL JOIN `Race` 
		RIGHT JOIN (
			-- first, get the best time for a xc athlete by course and gender
			SELECT `athleteid`, MIN(time) `best_time`
			FROM `Result` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` 
				NATURAL JOIN `Gender` NATURAL JOIN `Race` NATURAL JOIN `Course` 
			WHERE `courseid`=`inputCourseId` AND `genderid`=`inputGenderId` AND `grade`=`inputGrade`
			GROUP BY `athleteid` 
		) `best` ON `Athlete`.`athleteid`=`best`.`athleteid` AND `Result`.`time`=`best`.`best_time`
	WHERE `courseid`=`inputCourseId` AND `genderid`=`inputGenderId` AND `grade`=`inputGrade` 
		AND YEAR(`Race`.`date`)=`year`
	ORDER BY `Result`.`time`
	LIMIT `inputLimit`
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetCoachesByYear`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetCoachesByYear`(
	IN `inputYear` INT, 
	IN `inputCoachTypeIds` VARCHAR(255)
)
BEGIN

SELECT `firstName`, `lastName`, GROUP_CONCAT(`coachType` ORDER BY `coachTypeId` ASC SEPARATOR ", ") 
	AS `coachType`, `year`, `coachId`, MIN(`coachTypeId`) AS `coachTypeId`
FROM `Coach` NATURAL JOIN `CoachType` NATURAL JOIN `CoachSeason`
WHERE `year`=`inputYear` AND FIND_IN_SET(`coachTypeId`, `inputCoachTypeIds`) 
GROUP BY `coachId`
ORDER BY `coachTypeId` ASC;


END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetCoachTimeline`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetCoachTimeline`(
	IN `inputCoachTypeIds` VARCHAR(255)
)
BEGIN

SELECT `year`, GROUP_CONCAT(`coaches` ORDER BY `coachTypeId` ASC, `coachId` ASC SEPARATOR ", ") AS `coaches`
FROM (
	SELECT `year`, `coachId`, MIN(`coachTypeId`) AS `coachTypeId`, 
		CONCAT(
			`firstName`, " ", `lastName`, " (", 
            GROUP_CONCAT(`coachType` ORDER BY `coachTypeId` ASC SEPARATOR ", "), ")"
		) AS `coaches` 
	FROM `Coach` NATURAL JOIN `CoachType` NATURAL JOIN `CoachSeason` 
	WHERE FIND_IN_SET(`coachTypeId`, `inputCoachTypeIds`) 
	GROUP BY `year`, `coachId` 
) AS `t`
GROUP BY `year`
ORDER BY `year` DESC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetCoachById`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetCoachById`(
	IN `inputCoachId` INT, 
	IN `inputCoachTypeIds` VARCHAR(255)
)
BEGIN

SELECT `firstName`, `lastName`, 
	GROUP_CONCAT(`coachType` ORDER BY `coachTypeId` ASC SEPARATOR ", ") AS `coachType`, `year` 
FROM `Coach` NATURAL JOIN `CoachType` NATURAL JOIN `CoachSeason`
WHERE `coachId`=`inputCoachId` AND FIND_IN_SET(`coachTypeId`, `inputCoachTypeIds`) 
GROUP BY `year`
ORDER BY year DESC;


END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetCoaches`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetCoaches`(
	IN `inputCoachTypeIds` VARCHAR(255)
)
BEGIN

SELECT `coachId`, `firstName`, `lastName`, COUNT(DISTINCT `year`) AS `numSeasons`, 
	GROUP_CONCAT(DISTINCT `year` ORDER BY `year` DESC SEPARATOR ", ") `years`
FROM `Coach` NATURAL JOIN `CoachType` NATURAL JOIN `CoachSeason`
WHERE FIND_IN_SET(`coachTypeId`, `inputCoachTypeIds`) 
GROUP BY `coachId`
ORDER BY `numSeasons` DESC, `firstName` DESC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetAwardsByYear`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetAwardsByYear`(
	IN `inputYear` INT, 
	IN `inputSportId` TINYINT 
)
BEGIN

SELECT `firstName`, `lastName`, `awardId`, `awardName`, `awardShortName`, 
	`squadId`, `squadName`, `squadAbbr`, `year`
FROM `Award` NATURAL JOIN `Squad` NATURAL JOIN `Awardee` NATURAL JOIN `Athlete`
WHERE `year`=`inputYear` AND `sportId`=`inputSportId`
ORDER BY `squadId` ASC, `awardId` ASC, `lastName` ASC, `firstName` ASC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetAwardsById`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetAwardsById`(
	IN `inputAwardIds` VARCHAR(15),
	IN `inputSquadIds` VARCHAR(15), 
	IN `inputSportId` TINYINT 
)
BEGIN

SELECT `firstName`, `lastName`, `awardName`, `squadName`, `year`, `athleteId` 
FROM `Award` NATURAL JOIN `Squad` NATURAL JOIN `Awardee` NATURAL JOIN `Athlete`
WHERE FIND_IN_SET(`awardId`, `inputAwardIds`) 
	AND FIND_IN_SET(`squadId`, `inputSquadIds`) 
	AND `sportId`=`inputSportId`
ORDER BY `year` DESC, `squadId` ASC, `lastName` ASC, `firstName` ASC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetAwardsTimeline`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetAwardsTimeline`(
	IN `inputSquadIds` VARCHAR(15), 
	IN `inputSportId` TINYINT 
)
BEGIN

SELECT `firstName`, `lastName`, `awardName`, `squadName`, `year`, `athleteId`
FROM `Award` NATURAL JOIN `Squad` NATURAL JOIN `Awardee` NATURAL JOIN `Athlete`
WHERE FIND_IN_SET(`squadId`, `inputSquadIds`) AND `sportId`=`inputSportId`
ORDER BY `year` DESC, `squadId` ASC, `awardId` ASC, `lastName` ASC, `firstName` ASC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetXcAlumniResultsByYear`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetXcAlumniResultsByYear`(
	IN `inputYear` INT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
SELECT `time`, `pace`, `grade`, `firstname`, `lastname`, `date`, `racename`,
	`coursename`, `coursedistance`, `racecondition`, `raceid`
FROM `Result` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Race` 
	NATURAL JOIN `RaceName` NATURAL JOIN `RaceCondition` NATURAL JOIN `Course`
WHERE `raceId` < 1000000 AND `year`=`inputYear` AND YEAR(`Race`.`date`)=`year`
ORDER BY `time` ASC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetPastXcAlumniChampions`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetPastXcAlumniChampions`()
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
SELECT `time`, `pace`, `grade`, `firstname`, `lastname`, `athleteid`, `date`, 
	`racename`, `coursename`, `coursedistance`, `racecondition`, `raceid`
FROM `Result` RIGHT JOIN (
		SELECT MIN(`time`) `best_time` 
		FROM `Result` NATURAL JOIN `Race` NATURAL JOIN `Competitor`
		WHERE `raceId` < 1000000 AND `grade`=0
		GROUP BY `date`
	) `best` ON `Result`.`time`=`best`.`best_time`
	NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Race` 
	NATURAL JOIN `RaceName` NATURAL JOIN `RaceCondition` NATURAL JOIN `Course`
WHERE `raceId` < 1000000 AND YEAR(`Race`.`date`)=`year`
ORDER BY YEAR(`date`) DESC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetSpecialAchieversById`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetSpecialAchieversById`(
	IN `inputSpecialAchievementIds` VARCHAR(15), 
	IN `inputSportId` TINYINT 
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
SELECT `specialAchievementName`, `athleteId`, `firstName`, `lastName`, `grade`, `year`, `notes`
FROM `SpecialAchiever` NATURAL JOIN `Competitor` NATURAL JOIN `SpecialAchievement` NATURAL JOIN `Athlete`
WHERE FIND_IN_SET(`specialAchievementId`, `inputSpecialAchievementIds`) 
	AND `sportId`=`inputSportId` AND `SpecialAchiever`.`year`=`Competitor`.`year`
ORDER BY `year` DESC, FIELD(`specialAchievementId`, 3,2,1), `notes` ASC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTopXcIndividualByRace`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTopXcIndividualByRace`(
	IN `inputRaceId` TINYINT, 
	IN `inputGenderId` TINYINT, 
	IN `inputGrade` TINYINT, 
	IN `inputLimit` INT
)
BEGIN

-- for first query: get the best time for an athlete by race, (optionally) gender, (optionally) grade

-- create start of first query
SET @firstQuery = CONCAT(
		"SELECT `athleteid`, MIN(`time`) 'best_time'
		FROM `Result` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` 
			NATURAL JOIN `Gender` NATURAL JOIN `Race` 
		WHERE `racenameid`=",inputRaceId 
	);

-- check if valid input gender
IF inputGenderId > 0 THEN 
	SET @firstQuery = CONCAT(@firstQuery, " AND `genderid`=", inputGenderId);
END IF;

-- check if valid input grade
IF inputGrade > 0 THEN 
	SET @firstQuery = CONCAT(@firstQuery, " AND `grade`=", inputGrade);
END IF;

-- append end of first query
SET @firstQuery = CONCAT(@firstQuery, " GROUP BY `athleteid` ");


-- for middle query: join the best times with runner information and sort by best time

-- create start of second query
-- this part is necessary to distinguish between a competitor in xc vs track season:  AND YEAR(`Race`.`date`)=`year`
SET @secondQuery = CONCAT(
		"SELECT DISTINCT `firstname`, `lastname`, `Result`.`time`, `pace`, `year`, `grade`
		FROM `Result` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Gender` NATURAL JOIN `Race` 
			RIGHT JOIN (", @firstQuery, ") best ON `Athlete`.`athleteid`=`best`.`athleteid` AND `Result`.`time`=`best`.`best_time`
		WHERE `racenameid`=",inputRaceId," AND YEAR(`Race`.`date`)=`year`"
		" ORDER BY `Result`.`time` "
	);

-- check if valid input limit
IF inputLimit > 0 THEN 
	SET @secondQuery = CONCAT(@secondQuery, " LIMIT ", inputLimit);
END IF;


-- for final query: add myrank

-- create final query
SET @finalQuery = CONCAT(
		"SELECT @rownum := @rownum + 1 AS `myrank`, `t`.* 
		FROM (", @secondQuery, ") `t`, 
		(SELECT @rownum := 0) `r`;"
	);

-- execute final query
PREPARE stmt FROM @finalQuery;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;


END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTopTrackRaceIndividual`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTopTrackRaceIndividual`(
	IN `inputEventId` INT, 
	IN `inputGenderId` TINYINT, 
	IN `inputLimit` INT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND `RaceResult`.`year`=`Competitor`.`year`
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	SELECT DISTINCT `event`, `firstname`, `lastname`, `RaceResult`.`time`, 
		`raceTimeTypeId`, `year`, `grade`, `competitorid`
	FROM `RaceResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` 
		NATURAL JOIN `Athlete` NATURAL JOIN `Gender` 
	WHERE `eventId`=`inputEventId` AND `genderid`=`inputGenderId` 
		AND `RaceResult`.`year`=`Competitor`.`year`
	ORDER BY `RaceResult`.`time`, `year`, `lastname`, `firstname`
	LIMIT `inputLimit`
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTopFieldIndividual`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTopFieldIndividual`(
	IN `inputEventId` INT, 
	IN `inputGenderId` TINYINT, 
	IN `inputLimit` INT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND `FieldResult`.`year`=`Competitor`.`year`
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	SELECT DISTINCT `event`, `firstname`, `lastname`, `footPartOfDistance`, 
		`inchPartOfDistance`, `year`, `grade`, `competitorid`
	FROM `FieldResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` 
		NATURAL JOIN `Athlete` NATURAL JOIN `Gender` 
	WHERE `eventId`=`inputEventId` AND `genderid`=`inputGenderId` 
		AND `FieldResult`.`year`=`Competitor`.`year`
	ORDER BY `footPartOfDistance` DESC, `inchPartOfDistance` DESC, `year`, `lastname`, `firstname`
	LIMIT `inputLimit`
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTopTrackRelayTeam`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTopTrackRelayTeam`(
	IN `inputEventId` INT, 
	IN `inputGenderId` TINYINT, 
	IN `inputLimit` INT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND `RelayResult`.`year`=`C1`.`year`
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	SELECT DISTINCT `event`, `RelayResult`.`time`, `raceTimeTypeId`, `RelayResult`.`year`, 
        `C1`.`competitorId` AS `competitorId1`, CONCAT(`A1`.`firstName`, " ", `A1`.`lastName`) AS `fullName1`, `C1`.`grade` AS `grade1`,
        `C2`.`competitorId` AS `competitorId`, CONCAT(`A2`.`firstName`, " ", `A2`.`lastName`) AS `fullName2`, `C2`.`grade` AS `grade2`,
        `C3`.`competitorId` AS `competitorId3`, CONCAT(`A3`.`firstName`, " ", `A3`.`lastName`) AS `fullName3`, `C3`.`grade` AS `grade3`,
        `C4`.`competitorId` AS `competitorId4`, CONCAT(`A4`.`firstName`, " ", `A4`.`lastName`) AS `fullName4`, `C4`.`grade` AS `grade4`
	FROM `RelayResult` NATURAL JOIN `Event` 
		JOIN `Competitor` AS `C1` ON (`C1`.`competitorId`=`competitorId1`) JOIN `Athlete` AS `A1` ON (`A1`.`athleteId`=`C1`.`athleteId`) 
        JOIN `Competitor` AS `C2` ON (`C2`.`competitorId`=`competitorId2`) JOIN `Athlete` AS `A2` ON (`A2`.`athleteId`=`C2`.`athleteId`) 
        JOIN `Competitor` AS `C3` ON (`C3`.`competitorId`=`competitorId3`) JOIN `Athlete` AS `A3` ON (`A3`.`athleteId`=`C3`.`athleteId`) 
        JOIN `Competitor` AS `C4` ON (`C4`.`competitorId`=`competitorId4`) JOIN `Athlete` AS `A4` ON (`A4`.`athleteId`=`C4`.`athleteId`) 
        JOIN `Gender` ON (`Gender`.`genderId`=`A1`.`genderId`)
	WHERE `eventId`=`inputEventId` AND `Gender`.`genderid`=`inputGenderId` AND `RelayResult`.`year`=`C1`.`year`
	ORDER BY `RelayResult`.`time`, `RelayResult`.`year`
	LIMIT `inputLimit`
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTrackCompetitorsByYear`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTrackCompetitorsByYear`(
	IN `inputYear` INT 
)
BEGIN


SELECT DISTINCT `competitorid`, `year`, `grade`, `firstname`, `lastname`, `gender` 
FROM `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Gender` NATURAL JOIN `FieldResult` 
WHERE `Competitor`.`year`=`inputYear` AND `FieldResult`.`year`=`inputYear` AND `grade` != 0 
UNION
SELECT DISTINCT `competitorid`, `year`, `grade`, `firstname`, `lastname`, `gender` 
FROM `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Gender` NATURAL JOIN `RaceResult` 
WHERE `Competitor`.`year`=`inputYear` AND `RaceResult`.`year`=`inputYear` AND `grade` != 0 
UNION
SELECT DISTINCT `competitorid`, `RR`.`year`, `grade`, `firstname`, `lastname`, `gender` 
FROM `RelayResult` AS `RR` 
	JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId1`) 
    JOIN `Athlete` ON (`Athlete`.`athleteId`=`Competitor`.`athleteId`) 
    JOIN `Gender` ON (`Gender`.`genderId`=`Athlete`.`genderId`) 
WHERE `Competitor`.`year`=`inputYear` AND `RR`.`year`=`inputYear` AND `grade` != 0 
UNION
SELECT DISTINCT `competitorid`, `RR`.`year`, `grade`, `firstname`, `lastname`, `gender` 
FROM `RelayResult` AS `RR` 
	JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId2`) 
    JOIN `Athlete` ON (`Athlete`.`athleteId`=`Competitor`.`athleteId`) 
    JOIN `Gender` ON (`Gender`.`genderId`=`Athlete`.`genderId`) 
WHERE `Competitor`.`year`=`inputYear` AND `RR`.`year`=`inputYear` AND `grade` != 0 
UNION
SELECT DISTINCT `competitorid`, `RR`.`year`, `grade`, `firstname`, `lastname`, `gender` 
FROM `RelayResult` AS `RR` 
	JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId3`) 
    JOIN `Athlete` ON (`Athlete`.`athleteId`=`Competitor`.`athleteId`) 
    JOIN `Gender` ON (`Gender`.`genderId`=`Athlete`.`genderId`) 
WHERE `Competitor`.`year`=`inputYear` AND `RR`.`year`=`inputYear` AND `grade` != 0 
UNION
SELECT DISTINCT `competitorid`, `RR`.`year`, `grade`, `firstname`, `lastname`, `gender` 
FROM `RelayResult` AS `RR` 
	JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId4`) 
    JOIN `Athlete` ON (`Athlete`.`athleteId`=`Competitor`.`athleteId`) 
    JOIN `Gender` ON (`Gender`.`genderId`=`Athlete`.`genderId`) 
WHERE `Competitor`.`year`=`inputYear` AND `RR`.`year`=`inputYear` AND `grade` != 0 
ORDER BY `gender`, `lastname`, `firstname`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTrackEventsByYear`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTrackEventsByYear`(
	IN `inputYear` INT 
)
BEGIN

SELECT  ANY_VALUE(`event`) AS `event`, ANY_VALUE(`eventId`) AS `eventId`, 
	ANY_VALUE(`squadName`) AS `squadName`, ANY_VALUE(`squadId`) AS `squadID`, 
    CONCAT(`eventId`, ":", `squadId`) AS `eventBySquad`, COUNT(`squadID`) AS `numResults`,
    ANY_VALUE(`eventSubType`) AS `eventSubType`, ANY_VALUE(`eventSubTypeId`) AS `eventSubTypeId`
FROM `Event` NATURAL JOIN `RaceResult` NATURAL JOIN `Squad` NATURAL JOIN `EventSubType`
WHERE `year`=`inputYear` AND `raceTimeTypeId` NOT IN ("c", "F")
GROUP BY `eventBySquad`
UNION
SELECT  ANY_VALUE(`event`) AS `event`, ANY_VALUE(`eventId`) AS `eventId`, 
	ANY_VALUE(`squadName`) AS `squadName`, ANY_VALUE(`squadId`) AS `squadID`, 
    CONCAT(`eventId`, ":", `squadId`) AS `eventBySquad`, COUNT(`squadID`) AS `numResults`,
    ANY_VALUE(`eventSubType`) AS `eventSubType`, ANY_VALUE(`eventSubTypeId`) AS `eventSubTypeId`
FROM `Event` NATURAL JOIN `FieldResult` NATURAL JOIN `Squad` NATURAL JOIN `EventSubType`
WHERE `year`=`inputYear`
GROUP BY `eventBySquad`
UNION
SELECT  ANY_VALUE(`event`) AS `event`, ANY_VALUE(`eventId`) AS `eventId`, 
	ANY_VALUE(`squadName`) AS `squadName`, ANY_VALUE(`squadId`) AS `squadID`, 
    CONCAT(`eventId`, ":", `squadId`) AS `eventBySquad`, COUNT(`squadID`) AS `numResults`,
    ANY_VALUE(`eventSubType`) AS `eventSubType`, ANY_VALUE(`eventSubTypeId`) AS `eventSubTypeId`
FROM `Event` NATURAL JOIN `RelayResult` NATURAL JOIN `Squad` NATURAL JOIN `EventSubType`
WHERE `year`=`inputYear` AND `raceTimeTypeId` NOT IN ("c", "F")
GROUP BY `eventBySquad`
ORDER BY `eventSubTypeId`, `eventId`, `squadId`;


END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTrackRaceResults`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTrackRaceResults`(
	IN `inputEventId` INT, 
	IN `inputSquadId` TINYINT,
	IN `inputYear` INT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND `RaceResult`.`year`=`Competitor`.`year`
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	SELECT DISTINCT `event`, `firstname`, `lastname`, `time`, 
		`raceTimeTypeId`, `grade`, `competitorid`, `year`, `squadName`
	FROM `RaceResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` 
		NATURAL JOIN `Athlete` NATURAL JOIN `Squad` 
	WHERE `eventId`=`inputEventId` AND `squadId`=`inputSquadId`
		AND `RaceResult`.`year`=`inputYear` AND `RaceResult`.`year`=`Competitor`.`year`
	ORDER BY `RaceResult`.`time`, `lastname`, `firstname`
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTrackFieldResults`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTrackFieldResults`(
	IN `inputEventId` INT, 
	IN `inputSquadId` TINYINT,
	IN `inputYear` INT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND `FieldResult`.`year`=`Competitor`.`year`
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	SELECT DISTINCT `event`, `firstname`, `lastname`, `footPartOfDistance`, `inchPartOfDistance`, 
        `grade`, `competitorid`, `year`, `squadName`
	FROM `FieldResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` 
		NATURAL JOIN `Athlete` NATURAL JOIN `Squad` 
	WHERE `eventId`=`inputEventId` AND `squadId`=`inputSquadId`
		AND `FieldResult`.`year`=`inputYear` AND `FieldResult`.`year`=`Competitor`.`year`
	ORDER BY `footPartOfDistance` DESC, `inchPartOfDistance` DESC, `lastname`, `firstname`
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTrackRelayResults`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTrackRelayResults`(
	IN `inputEventId` INT, 
	IN `inputSquadId` TINYINT,
	IN `inputYear` INT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND `RelayResult`.`year`=`C1`.`year`
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	SELECT DISTINCT `event`, `RelayResult`.`time`, `raceTimeTypeId`, `RelayResult`.`year`, `squadName`, 
        `C1`.`competitorId` AS `competitorId1`, CONCAT(`A1`.`firstName`, " ", `A1`.`lastName`) AS `fullName1`, `C1`.`grade` AS `grade1`,
        `C2`.`competitorId` AS `competitorId`, CONCAT(`A2`.`firstName`, " ", `A2`.`lastName`) AS `fullName2`, `C2`.`grade` AS `grade2`,
        `C3`.`competitorId` AS `competitorId3`, CONCAT(`A3`.`firstName`, " ", `A3`.`lastName`) AS `fullName3`, `C3`.`grade` AS `grade3`,
        `C4`.`competitorId` AS `competitorId4`, CONCAT(`A4`.`firstName`, " ", `A4`.`lastName`) AS `fullName4`, `C4`.`grade` AS `grade4`
	FROM `RelayResult` NATURAL JOIN `Event` NATURAL JOIN `Squad` 
		JOIN `Competitor` AS `C1` ON (`C1`.`competitorId`=`competitorId1`) JOIN `Athlete` AS `A1` ON (`A1`.`athleteId`=`C1`.`athleteId`) 
        JOIN `Competitor` AS `C2` ON (`C2`.`competitorId`=`competitorId2`) JOIN `Athlete` AS `A2` ON (`A2`.`athleteId`=`C2`.`athleteId`) 
        JOIN `Competitor` AS `C3` ON (`C3`.`competitorId`=`competitorId3`) JOIN `Athlete` AS `A3` ON (`A3`.`athleteId`=`C3`.`athleteId`) 
        JOIN `Competitor` AS `C4` ON (`C4`.`competitorId`=`competitorId4`) JOIN `Athlete` AS `A4` ON (`A4`.`athleteId`=`C4`.`athleteId`) 
	WHERE `eventId`=`inputEventId` AND `squadId`=`inputSquadId` AND `RelayResult`.`year`=`inputYear` AND `RelayResult`.`year`=`C1`.`year`
	ORDER BY `RelayResult`.`time`    
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTrackCompetitorResults`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTrackCompetitorResults`(
	IN `inputCompetitorId` VARCHAR(15)
)
BEGIN

-- declare the program variables where we'll hold the values we're sending into the procedure
DECLARE `myEventId` TINYINT DEFAULT NULL;
DECLARE `myEventSubTypeId` TINYINT DEFAULT NULL;
DECLARE `myGenderId` TINYINT DEFAULT NULL;

-- we need a boolean variable to tell us when the cursor is out of data
DECLARE `done` TINYINT DEFAULT FALSE;

-- declare a cursor to select the desired columns from the desired source table1
-- the input argument (which you might or might not need) is used in this example for row selection
DECLARE `cursor1`CURSOR FOR
	SELECT `eventId`, `eventSubTypeId`, `genderId` FROM `RaceResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` WHERE `competitorId`=`inputCompetitorId`
	UNION
	SELECT `eventId`, `eventSubTypeId`, `genderId` FROM `FieldResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` WHERE `competitorId`=`inputCompetitorId`
	UNION
	SELECT `eventId`, `eventSubTypeId`, `genderId` FROM `RelayResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` WHERE `competitorId1`=`inputCompetitorId`
	UNION
	SELECT `eventId`, `eventSubTypeId`, `genderId` FROM `RelayResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` WHERE `competitorId2`=`inputCompetitorId`
	UNION
	SELECT `eventId`, `eventSubTypeId`, `genderId` FROM `RelayResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` WHERE `competitorId3`=`inputCompetitorId`
	UNION
	SELECT `eventId`, `eventSubTypeId`, `genderId` FROM `RelayResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` WHERE `competitorId4`=`inputCompetitorId`
	ORDER BY `eventSubTypeId`, `eventId`;

-- a cursor that runs out of data throws an exception; we need to catch this.
-- when the NOT FOUND condition fires, "done" -- which defaults to FALSE -- will be set to true,
-- and since this is a CONTINUE handler, execution continues with the next statement.   
DECLARE CONTINUE HANDLER FOR NOT FOUND SET `done` = TRUE;

-- open the cursor
OPEN `cursor1`;

`myLoop`: -- loops have to have an arbitrary label; it's used to leave the loop
LOOP

	-- read the values from the next row that is available in the cursor
	FETCH NEXT FROM `cursor1` INTO `myEventId`, `myEventSubTypeId`, `myGenderId`;

	IF `done` THEN -- this will be true when we are out of rows to read, so we go to the statement after END LOOP.
		LEAVE `myLoop`; 
	ELSE -- val1 and val2 will be the next values from c1 and c2 in table t1, 
		-- so now we call the procedure with them for this "row"
		CALL `GetTrackCompetitorResultsPart2`(`myEventId`, `myGenderId`);
    -- maybe do more stuff here
	END IF; 
END LOOP;

CLOSE `cursor1`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTrackCompetitorResultsPart2`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTrackCompetitorResultsPart2`(
	IN `inputEventId` INT,
    IN `inputGenderId` TINYINT
)
BEGIN

SELECT `t1`.*,@`rownum` := @`rownum` + 1 AS `myrank`
FROM (
	SELECT `event`, `eventId`, CONCAT(`firstname`, " ", `lastname`) AS `fullName`,
	`time` AS `result1`, `raceTimeTypeId` AS `result2`, `grade`, `competitorid`, `year`, 
    `squadName`, `squadId`, `Athlete`.`athleteId`, `genderId`
	FROM `RaceResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` 
		NATURAL JOIN `Athlete` NATURAL JOIN `Squad` 
	WHERE `eventId`=`inputEventId` AND `genderId`=`inputGenderId` 
	ORDER BY `RaceResult`.`time`, `lastname`, `firstname`
) `t1`, (SELECT @`rownum` := 0) `r`
UNION
SELECT `t1`.*,@`rownum` := @`rownum` + 1 AS `myrank`
FROM (
	SELECT `event`, `eventId`, CONCAT(`firstname`, " ", `lastname`) AS `fullName`, 
		`footPartOfDistance` AS `result1`, `inchPartOfDistance` AS `result2`, 
		`grade`, `competitorid`, `year`, `squadName`, `squadId`, `Athlete`.`athleteId`, `genderId`
	FROM `FieldResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` 
		NATURAL JOIN `Athlete` NATURAL JOIN `Squad` 
	WHERE `eventId`=`inputEventId` AND `genderId`=`inputGenderId` 
	ORDER BY `footPartOfDistance` DESC, `inchPartOfDistance` DESC, `year`, `lastname`, `firstname`
) `t1`, (SELECT @`rownum` := 0) `r`
UNION
SELECT `t1`.*,@`rownum` := @`rownum` + 1 AS `myrank`
FROM (
	SELECT `t1`.*
	FROM (
		SELECT `event`, `eventId`, CONCAT(`firstname`, " ", `lastname`) AS `fullName`, 
			`RelayResult`.`time` AS `result1`, `raceTimeTypeId` AS `result2`, 
			`grade`, `competitorid`, `RelayResult`.`year`, `squadName`, `squadId`, 
			`Athlete`.`athleteId`, `genderId`
		FROM `RelayResult` NATURAL JOIN `Event` NATURAL JOIN `Squad` 
			JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId1`) 
			JOIN `Athlete`ON (`Athlete`.`athleteId`=`Competitor`.`athleteId`) 
		WHERE `eventId`=`inputEventId` AND `genderId`=`inputGenderId` 
			AND `RelayResult`.`year`=`Competitor`.`year` 
	) `t1`
	UNION
	SELECT `t1`.*
	FROM (
		SELECT `event`, `eventId`, CONCAT(`firstname`, " ", `lastname`) AS `fullName`, 
			`RelayResult`.`time` AS `result1`, `raceTimeTypeId` AS `result2`, 
			`grade`, `competitorid`, `RelayResult`.`year`, `squadName`, `squadId`, 
			`Athlete`.`athleteId`, `genderId`
		FROM `RelayResult` NATURAL JOIN `Event` NATURAL JOIN `Squad` 
			JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId2`) 
			JOIN `Athlete`ON (`Athlete`.`athleteId`=`Competitor`.`athleteId`) 
		WHERE `eventId`=`inputEventId` AND `genderId`=`inputGenderId` 
			AND `RelayResult`.`year`=`Competitor`.`year` 
	) `t1`
	UNION
	SELECT `t1`.*
	FROM (
		SELECT `event`, `eventId`, CONCAT(`firstname`, " ", `lastname`) AS `fullName`, 
			`RelayResult`.`time` AS `result1`, `raceTimeTypeId` AS `result2`, 
			`grade`, `competitorid`, `RelayResult`.`year`, `squadName`, `squadId`, 
			`Athlete`.`athleteId`, `genderId`
		FROM `RelayResult` NATURAL JOIN `Event` NATURAL JOIN `Squad` 
			JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId3`) 
			JOIN `Athlete`ON (`Athlete`.`athleteId`=`Competitor`.`athleteId`) 
		WHERE `eventId`=`inputEventId` AND `genderId`=`inputGenderId` 
			 AND `RelayResult`.`year`=`Competitor`.`year` 
	) `t1`
	UNION
	SELECT `t1`.*
	FROM (
		SELECT `event`, `eventId`, CONCAT(`firstname`, " ", `lastname`) AS `fullName`, 
			`RelayResult`.`time` AS `result1`, `raceTimeTypeId` AS `result2`, 
			`grade`, `competitorid`, `RelayResult`.`year`, `squadName`, `squadId`, 
			`Athlete`.`athleteId`, `genderId`
		FROM `RelayResult` NATURAL JOIN `Event` NATURAL JOIN `Squad` 
			JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId4`) 
			JOIN `Athlete`ON (`Athlete`.`athleteId`=`Competitor`.`athleteId`) 
		WHERE `eventId`=`inputEventId` AND `genderId`=`inputGenderId` 
			 AND `RelayResult`.`year`=`Competitor`.`year` 
	) `t1`
	ORDER BY `result1`, `result2`
) `t1`, (SELECT @`rownum` := 0) `r`;


END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTrackAthletes`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTrackAthletes`(
	IN `inputGenderIds` VARCHAR(15)
)
BEGIN

-- these parts are necessary to distinguish between a competitor in xc vs track season:  
-- `RaceResult`.`year`=`year` ... `FieldResult`.`year`=`year` ... `RelayResult`.`year`=`Competitor`.`year`
SELECT `athleteid`, `firstname`, `lastname`,
	GROUP_CONCAT(DISTINCT `year` ORDER BY `year` ASC SEPARATOR ", ") `years`
FROM (
	-- query all race results
	SELECT  `athleteid`, `firstname`, `lastname`, `year`
	FROM `RaceResult` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Gender` 
	WHERE  `RaceResult`.`year`=`year` AND FIND_IN_SET(`genderId`, `inputGenderIds`) 
	UNION
    -- query all field results
	SELECT  `athleteid`, `firstname`, `lastname`, `year`
	FROM `FieldResult` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Gender` 
	WHERE  `FieldResult`.`year`=`year` AND FIND_IN_SET(`genderId`, `inputGenderIds`) 
    UNION
    -- query 1st leg of all relay results
    SELECT `Competitor`.`athleteid`, `firstname`, `lastname`, `Competitor`.`year`
	FROM `RelayResult` NATURAL JOIN `Gender` 
		JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId1`) 
        JOIN `Athlete` ON (`Athlete`.`athleteId`=`Competitor`.`athleteId`) 
	WHERE `RelayResult`.`year`=`Competitor`.`year` AND FIND_IN_SET(`Athlete`.`genderId`, `inputGenderIds`) 
    UNION
    -- query 2nd leg of all relay results
    SELECT `Competitor`.`athleteid`, `firstname`, `lastname`, `Competitor`.`year`
	FROM `RelayResult` NATURAL JOIN `Gender` 
		JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId2`) 
        JOIN `Athlete` ON (`Athlete`.`athleteId`=`Competitor`.`athleteId`) 
	WHERE `RelayResult`.`year`=`Competitor`.`year` AND FIND_IN_SET(`Athlete`.`genderId`, `inputGenderIds`) 
    UNION
    -- query 3rd leg of all relay results
    SELECT `Competitor`.`athleteid`, `firstname`, `lastname`, `Competitor`.`year`
	FROM `RelayResult` NATURAL JOIN `Gender` 
		JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId3`) 
        JOIN `Athlete` ON (`Athlete`.`athleteId`=`Competitor`.`athleteId`) 
	WHERE `RelayResult`.`year`=`Competitor`.`year` AND FIND_IN_SET(`Athlete`.`genderId`, `inputGenderIds`) 
    UNION
    -- query 4th leg of all relay results
    SELECT `Competitor`.`athleteid`, `firstname`, `lastname`, `Competitor`.`year`
	FROM `RelayResult` NATURAL JOIN `Gender` 
		JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId4`) 
        JOIN `Athlete` ON (`Athlete`.`athleteId`=`Competitor`.`athleteId`) 
	WHERE `RelayResult`.`year`=`Competitor`.`year` AND FIND_IN_SET(`Athlete`.`genderId`, `inputGenderIds`) 
) `t`
GROUP BY `athleteid`, `firstname`, `lastname`
ORDER BY `lastname`, `firstname`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTrackAthleteResults`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTrackAthleteResults`(
	IN `inputAthleteId` VARCHAR(15)
)
BEGIN

-- declare the program variables where we'll hold the values we're sending into the procedure
DECLARE `myEventId` TINYINT DEFAULT NULL;
DECLARE `myGenderId` TINYINT DEFAULT NULL;

-- we need a boolean variable to tell us when the cursor is out of data
DECLARE `done` TINYINT DEFAULT FALSE;

-- declare a cursor to select the desired columns from the desired source table1
-- the input argument (which you might or might not need) is used in this example for row selection
DECLARE `cursor1`CURSOR FOR
	SELECT `eventId`, `genderId` 
    FROM `RaceResult` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` 
    WHERE `RaceResult`.`year`=`Competitor`.`year` AND `athleteid`=`inputAthleteId`
	UNION
	SELECT `eventId`, `genderId` 
    FROM `FieldResult` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` 
    WHERE `FieldResult`.`year`=`Competitor`.`year` AND `athleteid`=`inputAthleteId`
	UNION
	SELECT `eventId`, `genderId` 
    FROM `RelayResult` JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId1`) NATURAL JOIN `Athlete` 
    WHERE `RelayResult`.`year`=`Competitor`.`year` AND `athleteid`=`inputAthleteId`
	UNION
	SELECT `eventId`, `genderId` 
    FROM `RelayResult` JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId2`) NATURAL JOIN `Athlete` 
    WHERE `RelayResult`.`year`=`Competitor`.`year` AND `athleteid`=`inputAthleteId`
	UNION
	SELECT `eventId`, `genderId` 
    FROM `RelayResult` JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId3`) NATURAL JOIN `Athlete` 
    WHERE `RelayResult`.`year`=`Competitor`.`year` AND `athleteid`=`inputAthleteId`
	UNION
	SELECT `eventId`, `genderId` 
    FROM `RelayResult` JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId4`) NATURAL JOIN `Athlete` 
    WHERE `RelayResult`.`year`=`Competitor`.`year` AND `athleteid`=`inputAthleteId`;

-- a cursor that runs out of data throws an exception; we need to catch this.
-- when the NOT FOUND condition fires, "done" -- which defaults to FALSE -- will be set to true,
-- and since this is a CONTINUE handler, execution continues with the next statement.   
DECLARE CONTINUE HANDLER FOR NOT FOUND SET `done` = TRUE;

CALL `GetTrackAthleteResultsPart2`(`inputAthleteId`);

-- open the cursor
OPEN `cursor1`;

`myLoop`: -- loops have to have an arbitrary label; it's used to leave the loop
LOOP

	-- read the values from the next row that is available in the cursor
	FETCH NEXT FROM `cursor1` INTO `myEventId`, `myGenderId`;

	IF `done` THEN -- this will be true when we are out of rows to read, so we go to the statement after END LOOP.
		LEAVE `myLoop`; 
	ELSE -- val1 and val2 will be the next values from c1 and c2 in table t1, 
		-- so now we call the procedure with them for this "row"
		CALL `GetTrackCompetitorResultsPart2`(`myEventId`, `myGenderId`);
    -- maybe do more stuff here
	END IF; 
END LOOP;

CLOSE `cursor1`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTrackAthleteResultsPart2`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTrackAthleteResultsPart2`(
	IN `inputAthleteId` VARCHAR(15)
)
BEGIN

	SELECT `eventId`, `year`, `competitorid`, `eventSubTypeId` 
    FROM `RaceResult` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Event` 
    WHERE `RaceResult`.`year`=`Competitor`.`year` AND `athleteid`=`inputAthleteId`
	UNION
	SELECT `eventId`, `year`, `competitorid`, `eventSubTypeId` 
    FROM `FieldResult` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` NATURAL JOIN `Event` 
    WHERE `FieldResult`.`year`=`Competitor`.`year` AND `athleteid`=`inputAthleteId`
	UNION
	SELECT `eventId`, `RelayResult`.`year`, `competitorid`, `eventSubTypeId` 
    FROM `RelayResult` JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId1`) NATURAL JOIN `Athlete` NATURAL JOIN `Event` 
    WHERE `RelayResult`.`year`=`Competitor`.`year` AND `athleteid`=`inputAthleteId`
	UNION
	SELECT `eventId`, `RelayResult`.`year`, `competitorid`, `eventSubTypeId` 
    FROM `RelayResult` JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId2`) NATURAL JOIN `Athlete` NATURAL JOIN `Event` 
    WHERE `RelayResult`.`year`=`Competitor`.`year` AND `athleteid`=`inputAthleteId`
	UNION
	SELECT `eventId`, `RelayResult`.`year`, `competitorid`, `eventSubTypeId` 
    FROM `RelayResult` JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId3`) NATURAL JOIN `Athlete` NATURAL JOIN `Event` 
    WHERE `RelayResult`.`year`=`Competitor`.`year` AND `athleteid`=`inputAthleteId`
	UNION
	SELECT `eventId`, `RelayResult`.`year`, `competitorid`, `eventSubTypeId` 
    FROM `RelayResult` JOIN `Competitor` ON (`Competitor`.`competitorId`=`competitorId4`) NATURAL JOIN `Athlete` NATURAL JOIN `Event` 
    WHERE `RelayResult`.`year`=`Competitor`.`year` AND `athleteid`=`inputAthleteId`
	ORDER BY `year` DESC, `eventSubTypeId`, `eventId`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTrackRaceResultsByGrade`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTrackRaceResultsByGrade`(
	IN `inputEventId` INT, 
	IN `inputGenderId` TINYINT,
	IN `inputGrade` SMALLINT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND `RaceResult`.`year`=`Competitor`.`year`
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t1`.* 
FROM (
	SELECT `event`, CONCAT(`firstname`, " ", `lastname`) AS `fullName`,
		`time` AS `result1`, `raceTimeTypeId` AS `result2`, `grade`, `year`, 
		`competitorid`, `Athlete`.`athleteId` 
	FROM `RaceResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` 
	WHERE `eventId`=`inputEventId` AND `genderId`=`inputGenderId` AND `grade`=`inputGrade` 
		AND `RaceResult`.`year`=`Competitor`.`year`
	ORDER BY `RaceResult`.`time`, `lastname`, `firstname`
) `t1`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTrackFieldResultsByGrade`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTrackFieldResultsByGrade`(
	IN `inputEventId` INT, 
	IN `inputGenderId` TINYINT,
	IN `inputGrade` SMALLINT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND `FieldResult`.`year`=`Competitor`.`year`
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	SELECT `event`, CONCAT(`firstname`, " ", `lastname`) AS `fullName`, 
		`footPartOfDistance` AS `result1`, `inchPartOfDistance` AS `result2`, 
		`grade`, `year`, `competitorid`, `Athlete`.`athleteId` 
	FROM `FieldResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` 
	WHERE `eventId`=`inputEventId` AND `genderId`=`inputGenderId` AND `grade`=`inputGrade` 
		AND `FieldResult`.`year`=`Competitor`.`year` 
	ORDER BY `footPartOfDistance` DESC, `inchPartOfDistance` DESC, `lastname`, `firstname`
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetAllTrackRaceResults`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetAllTrackRaceResults`(
	IN `inputEventId` INT, 
	IN `inputGenderId` TINYINT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND `RaceResult`.`year`=`Competitor`.`year`
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t1`.* 
FROM (
	SELECT `event`, CONCAT(`firstname`, " ", `lastname`) AS `fullName`,
		`time` AS `result1`, `raceTimeTypeId` AS `result2`, `grade`, `year`, 
		`competitorid`, `Athlete`.`athleteId` 
	FROM `RaceResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` 
	WHERE `eventId`=`inputEventId` AND `genderId`=`inputGenderId` AND `RaceResult`.`year`=`Competitor`.`year`
	ORDER BY `RaceResult`.`time`, `lastname`, `firstname`, `grade` 
) `t1`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetAllTrackFieldResults`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetAllTrackFieldResults`(
	IN `inputEventId` INT, 
	IN `inputGenderId` TINYINT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND `FieldResult`.`year`=`Competitor`.`year`
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	SELECT `event`, CONCAT(`firstname`, " ", `lastname`) AS `fullName`, 
		`footPartOfDistance` AS `result1`, `inchPartOfDistance` AS `result2`, 
		`grade`, `year`, `competitorid`, `Athlete`.`athleteId` 
	FROM `FieldResult` NATURAL JOIN `Event` NATURAL JOIN `Competitor` NATURAL JOIN `Athlete` 
	WHERE `eventId`=`inputEventId` AND `genderId`=`inputGenderId` AND `FieldResult`.`year`=`Competitor`.`year`
	ORDER BY `footPartOfDistance` DESC, `inchPartOfDistance` DESC, `lastname`, `firstname`, `grade` 
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetAllTrackRelayResults`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetAllTrackRelayResults`(
	IN `inputEventId` INT, 
	IN `inputGenderId` TINYINT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND `RelayResult`.`year`=`C1`.`year`
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	SELECT DISTINCT `event`, `RelayResult`.`time` AS `result1`, `raceTimeTypeId` AS `result2`, `RelayResult`.`year`, 
        CONCAT(`A1`.`firstName`, " ", `A1`.`lastName`) AS `fullName1`, `C1`.`grade` AS `grade1`, `C1`.`competitorId` AS `competitorId1`, `A1`.`athleteId` AS `athleteId1`, 
        CONCAT(`A2`.`firstName`, " ", `A2`.`lastName`) AS `fullName2`, `C2`.`grade` AS `grade2`, `C2`.`competitorId` AS `competitorId2`, `A2`.`athleteId` AS `athleteId2`, 
        CONCAT(`A3`.`firstName`, " ", `A3`.`lastName`) AS `fullName3`, `C3`.`grade` AS `grade3`, `C3`.`competitorId` AS `competitorId3`, `A3`.`athleteId` AS `athleteId3`, 
        CONCAT(`A4`.`firstName`, " ", `A4`.`lastName`) AS `fullName4`, `C4`.`grade` AS `grade4`, `C4`.`competitorId` AS `competitorId4`, `A4`.`athleteId` AS `athleteId4` 
	FROM `RelayResult` NATURAL JOIN `Event` NATURAL JOIN `Squad` 
		JOIN `Competitor` AS `C1` ON (`C1`.`competitorId`=`competitorId1`) JOIN `Athlete` AS `A1` ON (`A1`.`athleteId`=`C1`.`athleteId`) 
        JOIN `Competitor` AS `C2` ON (`C2`.`competitorId`=`competitorId2`) JOIN `Athlete` AS `A2` ON (`A2`.`athleteId`=`C2`.`athleteId`) 
        JOIN `Competitor` AS `C3` ON (`C3`.`competitorId`=`competitorId3`) JOIN `Athlete` AS `A3` ON (`A3`.`athleteId`=`C3`.`athleteId`) 
        JOIN `Competitor` AS `C4` ON (`C4`.`competitorId`=`competitorId4`) JOIN `Athlete` AS `A4` ON (`A4`.`athleteId`=`C4`.`athleteId`) 
	WHERE `eventId`=`inputEventId` AND `A1`.`genderId`=`inputGenderId` AND `RelayResult`.`year`=`C1`.`year`
	ORDER BY `RelayResult`.`time`, `RelayResult`.`year`
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTrackRelayResultsBySquad`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetTrackRelayResultsBySquad`(
	IN `inputEventId` INT, 
	IN `inputGenderId` TINYINT,
    IN `inputSquadId` TINYINT
)
BEGIN

-- this part is necessary to distinguish between a competitor in xc vs track season:  AND `RelayResult`.`year`=`C1`.`year`
SELECT @`rownum` := @`rownum` + 1 AS `myrank`, `t`.* 
FROM (
	SELECT DISTINCT `event`, `RelayResult`.`time` AS `result1`, `raceTimeTypeId` AS `result2`, `RelayResult`.`year`, 
        CONCAT(`A1`.`firstName`, " ", `A1`.`lastName`) AS `fullName1`, `C1`.`grade` AS `grade1`, `C1`.`competitorId` AS `competitorId1`, `A1`.`athleteId` AS `athleteId1`, 
        CONCAT(`A2`.`firstName`, " ", `A2`.`lastName`) AS `fullName2`, `C2`.`grade` AS `grade2`, `C2`.`competitorId` AS `competitorId2`, `A2`.`athleteId` AS `athleteId2`, 
        CONCAT(`A3`.`firstName`, " ", `A3`.`lastName`) AS `fullName3`, `C3`.`grade` AS `grade3`, `C3`.`competitorId` AS `competitorId3`, `A3`.`athleteId` AS `athleteId3`, 
        CONCAT(`A4`.`firstName`, " ", `A4`.`lastName`) AS `fullName4`, `C4`.`grade` AS `grade4`, `C4`.`competitorId` AS `competitorId4`, `A4`.`athleteId` AS `athleteId4` 
	FROM `RelayResult` NATURAL JOIN `Event` NATURAL JOIN `Squad` 
		JOIN `Competitor` AS `C1` ON (`C1`.`competitorId`=`competitorId1`) JOIN `Athlete` AS `A1` ON (`A1`.`athleteId`=`C1`.`athleteId`) 
        JOIN `Competitor` AS `C2` ON (`C2`.`competitorId`=`competitorId2`) JOIN `Athlete` AS `A2` ON (`A2`.`athleteId`=`C2`.`athleteId`) 
        JOIN `Competitor` AS `C3` ON (`C3`.`competitorId`=`competitorId3`) JOIN `Athlete` AS `A3` ON (`A3`.`athleteId`=`C3`.`athleteId`) 
        JOIN `Competitor` AS `C4` ON (`C4`.`competitorId`=`competitorId4`) JOIN `Athlete` AS `A4` ON (`A4`.`athleteId`=`C4`.`athleteId`) 
	WHERE `eventId`=`inputEventId` AND `squadId`=`inputSquadId` AND `A1`.`genderId`=`inputGenderId` AND `RelayResult`.`year`=`C1`.`year`
	ORDER BY `RelayResult`.`time`, `RelayResult`.`year`
) `t`, 
(SELECT @`rownum` := 0) `r`;

END //
DELIMITER ;


COMMIT;



-- test stored procedure calls
CALL `GetTopXcIndividual`(1,2,25);
CALL `GetCourseInfo`(25);
CALL `GetTopTeamCourse`(1,2,15);
CALL `GetXcRunnerResults`(1);
CALL `GetXcRunners`("2,3");
CALL `GetXcResultsByRaceCompetitor`("1000173,1000160,1000075,1000183,1000131,1000088,1000139,1000149,1000259,1000248,1000062,1000122,1000239,1000003,1000101",
"1000259.11,1000179.12,1000348.12,1000257.11,1000167.11,1000179.11,1000259.10,1000348.11,1000257.10,1000065.11,1000261.11,1000212.12,1000193.10,1000356.10,1000107.11,1000041.12,1000257.12,1000071.12,1000340.9,1000334.9,1000345.12,1000142.12,1.12,1000197.11,1000239.12,1000261.12,1000193.11,1000296.10,1000107.12,1000276.9,1000115.12,1000179.9,1000197.12,1000357.11,1000348.9,1000179.10,1000348.10,1000259.9,1000150.10,1000257.9,1000063.12,1000220.11,1000122.12,1000267.11,1000373.10,1000220.10,1000063.11,1000267.10,1000122.11,1000346.11,1000261.10,1000305.12,1000356.9,1000212.11,1000311.12,1.11,1000345.11,1000006.12,1000331.12,1000357.9,1000300.12,1000220.9,1000063.10,1000122.10,1000053.10,1000289.12,1000298.12,1000043.11,1000159.12,1000199.11,1000193.12,1000239.9,1000345.9,1000047.11,1.9");
CALL `GetXcCompetitorsByYear`(2003,2);
CALL `GetXcRacesByYear`(2003);
CALL `GetXcCompetitorResults`(1.12);
CALL `GetAllXcRaceResults`(1000131);
CALL `GetXcRaceResults`(1000131,2);
CALL `GetTopXcIndividualByGrade`(1,2,12,25);
CALL `GetCoachesByYear`(2018, "1,2");
CALL `GetCoachTimeline`("1,2");
CALL `GetCoachById`(1,"1,2");
CALL `GetCoaches`("1,2");
CALL `GetAwardsByYear`(2017,1);
CALL `GetAwardsById`("1,2","1,2,3,4",1);
CALL `GetAwardsTimeline`("2",1);
CALL `GetXcAlumniResultsByYear`(2017);
CALL `GetPastXcAlumniChampions`();
CALL `GetSpecialAchieversById`("1,2,3", 1);
-- track specific calls
CALL `GetTopTrackRaceIndividual`(1,3,15);
CALL `GetTopFieldIndividual`(29, 3, 20);
CALL `GetTopTrackRelayTeam`(25, 2, 20);
CALL `GetTrackCompetitorsByYear`(2018);
CALL `GetTrackEventsByYear`(2018);
CALL `GetTrackRaceResults`(1,2,2018);
CALL `GetTrackFieldResults`(29,1,2018);
CALL `GetTrackRelayResults`(25,1,2018);
CALL `GetTrackCompetitorResults`("1000464.12");
CALL `GetTrackAthletes`("3");
CALL `GetTrackAthleteResults`(1000464);
CALL `GetTrackRaceResultsByGrade`(8, 2, 12);
CALL `GetTrackFieldResultsByGrade`(29, 3, 9);
CALL `GetAllTrackRaceResults`(1, 3);
CALL `GetAllTrackFieldResults`(29, 2);
CALL `GetAllTrackRelayResults`(26, 3);
CALL `GetTrackRelayResultsBySquad`(25, 3, 1);


-- need to consider if i want to separate by course, ie ccs: Crystal vs Toro
-- or if i just want ORDER BY pace... discuss with Julie
USE `highSchoolRunning`;
CALL `GetTopXcIndividualByRace`(3,3,0,0);
