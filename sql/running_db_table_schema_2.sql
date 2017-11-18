DROP PROCEDURE IF EXISTS `GetTopIndividual`;

DELIMITER //
CREATE PROCEDURE `GetTopIndividual`(
	IN inputCourseId INT, 
	IN inputGenderId TINYINT, 
	IN inputLimit INT
)
BEGIN

SELECT @rownum := @rownum + 1 AS rank, t.* 
FROM (
	-- second, join the best times with runner information and sort by best time
	SELECT DISTINCT firstname,lastname,Result.time,pace,year,grade,competitorid
	FROM Result NATURAL JOIN Competitor NATURAL JOIN Runner NATURAL JOIN Gender NATURAL JOIN Race 
		RIGHT JOIN (
			-- first, get the best time for a runner by course and gender
			SELECT runnerid, MIN(time) 'best_time'
			FROM Result NATURAL JOIN Competitor NATURAL JOIN Runner 
				NATURAL JOIN Gender NATURAL JOIN Race NATURAL JOIN Course 
			WHERE courseid=inputCourseId AND genderid=inputGenderId 
			GROUP BY runnerid 
		) best ON Runner.runnerid=best.runnerid AND Result.time=best.best_time
	WHERE courseid=inputCourseId AND genderid=inputGenderId 
	ORDER BY Result.time
	LIMIT inputLimit
) t, 
(SELECT @rownum := 0) r;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetCourseInfo`;

DELIMITER //
CREATE PROCEDURE `GetCourseInfo`(
	IN inputCourseId INT
)
BEGIN

SELECT courseid,coursename,coursedistance,city,state,coursetype 
FROM Course NATURAL JOIN Location NATURAL JOIN State NATURAL JOIN CourseType 
WHERE courseid=inputCourseId;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTopTeamCourse`;

DELIMITER //
CREATE PROCEDURE `GetTopTeamCourse`(
	IN inputCourseId INT, 
	IN inputGenderId TINYINT, 
	IN inputLimit INT
)
BEGIN

-- fifth, add rank number column
SELECT @rownum := @rownum + 1 AS rank, t.* 
FROM (
	-- fourth, get the best time for each year and sort by best team time
	SELECT yr AS 'Year', 
		MIN(team_time) AS 'Team Time',
		MIN(team_avg) AS 'Avg. Ind. Time', 
		SUBSTRING_INDEX(GROUP_CONCAT(raceid ORDER BY team_time ASC SEPARATOR "#"), "#", 1) AS 'Race ID',
		SUBSTRING_INDEX(GROUP_CONCAT(competitors ORDER BY team_time ASC SEPARATOR "#"), "#", 1) AS 'Competitors'
	FROM (
		SELECT YEAR(date) yr, Result.raceid, 
			SEC_TO_TIME(AVG(TIME_TO_SEC(time))) AS team_avg, 
			SEC_TO_TIME(SUM(TIME_TO_SEC(time))) AS team_time, 
			GROUP_CONCAT(competitorid ORDER BY time ASC) AS competitors
		FROM Result NATURAL JOIN Race INNER JOIN (
				-- second, order competitors for each race by fastest time
				SELECT raceid, GROUP_CONCAT(CONCAT(competitorid,":",raceid) ORDER BY time ASC) AS finisher_key 
				FROM Result NATURAL JOIN Race NATURAL JOIN Competitor NATURAL JOIN Runner 
				WHERE genderid=inputGenderId AND raceid IN (
					SELECT raceid 
					FROM (
						-- first, get races that have at least 5 results
						SELECT raceid, count(raceid) AS 'num_racers' 
						FROM Result NATURAL JOIN Race NATURAL JOIN Competitor NATURAL JOIN Runner 
						WHERE courseid=inputCourseId AND genderid=inputGenderId
						GROUP BY raceid
					) num_racers_table
					WHERE num_racers >= 5
				)
				GROUP BY raceid
			) finisher_tbl ON Result.raceid = finisher_tbl.raceid
			-- third, retrieve only the fastest 5 competitors for each race
			AND find_in_set(CONCAT(Result.competitorid,":",Result.raceid), finisher_tbl.finisher_key) BETWEEN 1 AND 5
		GROUP BY Result.raceid
		ORDER BY yr,team_time
	) team_times 
	GROUP BY yr
	ORDER BY MIN(team_time)
	LIMIT inputLimit
) t, 
(SELECT @rownum := 0) r;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetRunnerResults`;

DELIMITER //
CREATE PROCEDURE `GetRunnerResults`(
	IN inputRunnerId INT
)
BEGIN

SELECT time,pace,grade,date,racename,coursename,coursedistance,racecondition,firstname,lastname,raceid
FROM Result NATURAL JOIN Competitor NATURAL JOIN Runner NATURAL JOIN Race 
	NATURAL JOIN RaceName NATURAL JOIN RaceCondition NATURAL JOIN Course
WHERE runnerid=inputRunnerId
ORDER BY date DESC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetRunners`;

DELIMITER //
CREATE PROCEDURE `GetRunners`(
	IN inputGenderId INT
)
BEGIN

SELECT runnerid,firstname,lastname,
	GROUP_CONCAT(year ORDER BY year ASC SEPARATOR ", ") years
FROM Competitor NATURAL JOIN Runner NATURAL JOIN Gender 
WHERE genderid=inputGenderId
GROUP BY runnerid
ORDER BY lastname,firstname;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetResultsByRaceCompetitor`;

DELIMITER //
CREATE PROCEDURE `GetResultsByRaceCompetitor`(
	IN inputRaceIds VARCHAR(255),
	IN inputCompetitorIds VARCHAR(1023)
)
BEGIN

SELECT raceid,competitorid,time,pace,grade,firstname,lastname
FROM Result NATURAL JOIN Competitor NATURAL JOIN Runner NATURAL JOIN Race 
WHERE FIND_IN_SET(raceid, inputRaceIds) AND 
FIND_IN_SET(competitorid, inputCompetitorIds)
ORDER BY time;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetCompetitorsByYear`;

DELIMITER //
CREATE PROCEDURE `GetCompetitorsByYear`(
	IN inputYear INT, 
	IN inputGenderId INT
)
BEGIN

SELECT competitorid,year,grade,firstname,lastname,gender 
FROM Competitor NATURAL JOIN Runner NATURAL JOIN Gender 
WHERE year=inputYear AND genderid=inputGenderId
ORDER BY lastname,firstname;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetRacesByYear`;

DELIMITER //
CREATE PROCEDURE `GetRacesByYear`(
	IN inputYear INT 
)
BEGIN

SELECT raceid,date,racename,coursename,coursedistance
FROM Race NATURAL JOIN RaceName NATURAL JOIN Course 
WHERE YEAR(date)=inputYear
ORDER BY date;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetCompetitorResults`;

DELIMITER //
CREATE PROCEDURE `GetCompetitorResults`(
	IN inputCompetitorId VARCHAR(15)
)
BEGIN

SELECT time,pace,grade,date,racename,coursename,coursedistance,racecondition,firstname,lastname,year,raceid
FROM Result NATURAL JOIN Competitor NATURAL JOIN Runner NATURAL JOIN Race 
	NATURAL JOIN RaceName NATURAL JOIN RaceCondition NATURAL JOIN Course
WHERE competitorId=inputCompetitorId
ORDER BY date DESC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetAllRaceResults`;

DELIMITER //
CREATE PROCEDURE `GetAllRaceResults`(
	IN inputRaceId INT
)
BEGIN

SELECT @rownum := @rownum + 1 AS rank, t.* 
FROM (
	SELECT time,pace,grade,date,racename,coursename,coursedistance,racecondition,firstname,lastname,year,competitorid
	FROM Result NATURAL JOIN Competitor NATURAL JOIN Runner NATURAL JOIN Race 
		NATURAL JOIN RaceName NATURAL JOIN RaceCondition NATURAL JOIN Course
	WHERE raceid=inputRaceId 
	ORDER BY time ASC
) t, 
(SELECT @rownum := 0) r;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetRaceResults`;

DELIMITER //
CREATE PROCEDURE `GetRaceResults`(
	IN inputRaceId INT,
	IN inputGenderId INT
)
BEGIN

SELECT @rownum := @rownum + 1 AS rank, t.* 
FROM (
	SELECT time,pace,grade,date,racename,coursename,coursedistance,racecondition,firstname,lastname,year,competitorid
	FROM Result NATURAL JOIN Competitor NATURAL JOIN Runner NATURAL JOIN Race 
		NATURAL JOIN RaceName NATURAL JOIN RaceCondition NATURAL JOIN Course
	WHERE raceid=inputRaceId AND genderid=inputGenderId
	ORDER BY time ASC
) t, 
(SELECT @rownum := 0) r;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetTopIndividualByGrade`;

DELIMITER //
CREATE PROCEDURE `GetTopIndividualByGrade`(
	IN inputCourseId INT, 
	IN inputGenderId TINYINT, 
	IN inputGrade TINYINT, 
	IN inputLimit INT
)
BEGIN

SELECT @rownum := @rownum + 1 AS rank, t.* 
FROM (
	-- second, joIN the best times with runner information and sort by best time
	SELECT DISTINCT firstname,lastname,Result.time,pace,year,grade,competitorid
	FROM Result NATURAL JOIN Competitor NATURAL JOIN Runner NATURAL JOIN Gender NATURAL JOIN Race 
		RIGHT JOIN (
			-- first, get the best time for a runner by course and gender
			SELECT runnerid, MIN(time) 'best_time'
			FROM Result NATURAL JOIN Competitor NATURAL JOIN Runner 
				NATURAL JOIN Gender NATURAL JOIN Race NATURAL JOIN Course 
			WHERE courseid=inputCourseId AND genderid=inputGenderId AND grade=inputGrade
			GROUP BY runnerid 
		) best ON Runner.runnerid=best.runnerid AND Result.time=best.best_time
	WHERE courseid=inputCourseId AND genderid=inputGenderId 
	ORDER BY Result.time
	LIMIT inputLimit
) t, 
(SELECT @rownum := 0) r;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetCoachesByYear`;

DELIMITER //
CREATE PROCEDURE `GetCoachesByYear`(
	IN inputYear INT 
)
BEGIN

SELECT firstName, lastName, coachType, year, coachId 
FROM `Coach` NATURAL JOIN `CoachType` NATURAL JOIN `CoachSeason`
WHERE year=inputYear
ORDER BY coachTypeId ASC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetCoachTimeline`;

DELIMITER //
CREATE PROCEDURE `GetCoachTimeline`()
BEGIN

SELECT year, GROUP_CONCAT(
	CONCAT(firstName, " ", lastName, " (", coachType, ")") 
	ORDER BY coachTypeId ASC, firstName ASC SEPARATOR ", ") AS "Coaches" 
FROM `Coach` NATURAL JOIN `CoachType` NATURAL JOIN `CoachSeason` 
GROUP BY year 
ORDER BY year DESC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetCoachById`;

DELIMITER //
CREATE PROCEDURE `GetCoachById`(
	IN inputCoachId INT 
)
BEGIN

SELECT firstName, lastName, coachType, year 
FROM `Coach` NATURAL JOIN `CoachType` NATURAL JOIN `CoachSeason`
WHERE coachId=inputCoachId
ORDER BY year DESC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetCoaches`;

DELIMITER //
CREATE PROCEDURE `GetCoaches`()
BEGIN

SELECT coachId, firstName, lastName, COUNT(year) AS numSeasons, 
	GROUP_CONCAT(year ORDER BY year DESC SEPARATOR ", ") years
FROM `Coach` NATURAL JOIN `CoachType` NATURAL JOIN `CoachSeason`
GROUP BY coachId
ORDER BY numSeasons DESC, firstName DESC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetAwardsByYear`;

DELIMITER //
CREATE PROCEDURE `GetAwardsByYear`(
	IN inputYear INT 
)
BEGIN

SELECT firstName, lastName, awardId, awardName, awardShortName, squadId, squadName, squadAbbr, year
FROM `Award` NATURAL JOIN `Squad` NATURAL JOIN `Awardee` NATURAL JOIN `Runner`
WHERE year=inputYear
ORDER BY squadId ASC, awardId ASC, lastName ASC, firstName ASC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetAwardsById`;

DELIMITER //
CREATE PROCEDURE `GetAwardsById`(
	IN inputAwardIds VARCHAR(15),
	IN inputSquadIds VARCHAR(15)
)
BEGIN

SELECT firstName, lastName, awardName, squadName, year, runnerId 
FROM `Award` NATURAL JOIN `Squad` NATURAL JOIN `Awardee` NATURAL JOIN `Runner`
WHERE FIND_IN_SET(awardId, inputAwardIds) 
AND FIND_IN_SET(squadId, inputSquadIds) 
ORDER BY year DESC, squadId ASC, lastName ASC, firstName ASC;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetAwardsTimeline`;

DELIMITER //
CREATE PROCEDURE `GetAwardsTimeline`(
	IN inputSquadIds VARCHAR(15)
)
BEGIN

SELECT firstName, lastName, awardName, squadName, year, runnerId
FROM `Award` NATURAL JOIN `Squad` NATURAL JOIN `Awardee` NATURAL JOIN `Runner`
WHERE FIND_IN_SET(squadId, inputSquadIds) 
ORDER BY year DESC, squadId ASC, awardId ASC, lastName ASC, firstName ASC;

END //
DELIMITER ;



COMMIT;



CALL GetTopIndividual(1,2,25);
CALL GetCourseInfo(25);
CALL GetTopTeamCourse(1,3,15);
CALL GetRunnerResults(1);
CALL GetRunners(3);
CALL GetResultsByRaceCompetitor('1000173,1000160,1000075,1000183,1000131,1000088,1000139,1000149,1000259,1000248,1000062,1000122,1000239,1000003,1000101',
'1000259.11,1000179.12,1000348.12,1000257.11,1000167.11,1000179.11,1000259.10,1000348.11,1000257.10,1000065.11,1000261.11,1000212.12,1000193.10,1000356.10,1000107.11,1000041.12,1000257.12,1000071.12,1000340.9,1000334.9,1000345.12,1000142.12,1.12,1000197.11,1000239.12,1000261.12,1000193.11,1000296.10,1000107.12,1000276.9,1000115.12,1000179.9,1000197.12,1000357.11,1000348.9,1000179.10,1000348.10,1000259.9,1000150.10,1000257.9,1000063.12,1000220.11,1000122.12,1000267.11,1000373.10,1000220.10,1000063.11,1000267.10,1000122.11,1000346.11,1000261.10,1000305.12,1000356.9,1000212.11,1000311.12,1.11,1000345.11,1000006.12,1000331.12,1000357.9,1000300.12,1000220.9,1000063.10,1000122.10,1000053.10,1000289.12,1000298.12,1000043.11,1000159.12,1000199.11,1000193.12,1000239.9,1000345.9,1000047.11,1.9');
CALL GetCompetitorsByYEAR(2003,3);
CALL GetRacesByYEAR(2003);
CALL GetCompetitorResults(1000157.10);
CALL GetAllRaceResults(1000131);
CALL GetRaceResults(1000131,3);
CALL GetTopIndividualByGrade(1,2,10,25);
CALL GetCoachesByYear(2015);
CALL GetCoachTimeline();
CALL GetCoachById(1);
CALL GetCoaches();
CALL GetAwardsByYear(2017);
CALL GetAwardsById('1,2','1,2,3,4');
CALL GetAwardsTimeline('2');



-- need to consider if i want to separate by course, ie ccs: Crystal vs Toro
-- or if i just want ORDER BY pace... discuss with Julie
CALL GetTopIndividualByRace(3,3,0,0);


DROP PROCEDURE IF EXISTS `GetTopIndividualByRace`;

DELIMITER //
CREATE PROCEDURE `GetTopIndividualByRace`(
	IN inputRaceId TINYINT, 
	IN inputGenderId TINYINT, 
	IN inputGrade TINYINT, 
	IN inputLimit INT
)
BEGIN

-- for first query: get the best time for a runner by race, (optionally) gender, (optionally) grade

-- create start of first query
SET @firstQuery = CONCAT(
		"SELECT runnerid, MIN(time) 'best_time'
		FROM Result NATURAL JOIN Competitor NATURAL JOIN Runner 
			NATURAL JOIN Gender NATURAL JOIN Race 
		WHERE racenameid=",inputRaceId 
	);

-- check if valid input gender
IF inputGenderId > 0 THEN 
	SET @firstQuery = CONCAT(@firstQuery, " AND genderid=", inputGenderId);
END IF;

-- check if valid input grade
IF inputGrade > 0 THEN 
	SET @firstQuery = CONCAT(@firstQuery, " AND grade=", inputGrade);
END IF;

-- append end of first query
SET @firstQuery = CONCAT(@firstQuery, " GROUP BY runnerid ");


-- for middle query: join the best times with runner information and sort by best time

-- create start of second query
SET @secondQuery = CONCAT(
		"SELECT DISTINCT firstname,lastname,Result.time,pace,year,grade
		FROM Result NATURAL JOIN Competitor NATURAL JOIN Runner NATURAL JOIN Gender NATURAL JOIN Race 
			RIGHT JOIN (", @firstQuery, ") best ON Runner.runnerid=best.runnerid AND Result.time=best.best_time
		WHERE racenameid=",inputRaceId,
		" ORDER BY Result.time "
	);

-- check if valid input limit
IF inputLimit > 0 THEN 
	SET @secondQuery = CONCAT(@secondQuery, " LIMIT ", inputLimit);
END IF;


-- for final query: add rank

-- create final query
SET @finalQuery = CONCAT(
		"SELECT @rownum := @rownum + 1 AS rank, t.* 
		FROM (", @secondQuery, ") t, 
		(SELECT @rownum := 0) r;"
	);

-- execute final query
PREPARE stmt FROM @finalQuery;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;


END //
DELIMITER ;

