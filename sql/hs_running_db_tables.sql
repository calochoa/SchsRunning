DROP DATABASE IF EXISTS `hsRunning`;

-- CREATING DATABASE
CREATE DATABASE IF NOT EXISTS `hsRunning`
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci
;


USE `hsRunning`;



-- REMOVING TABLES
DROP TABLE IF EXISTS `RelayResult`;
DROP TABLE IF EXISTS `RaceResult`;
DROP TABLE IF EXISTS `RaceTimeType`;
DROP TABLE IF EXISTS `FieldResult`;
DROP TABLE IF EXISTS `Event`;
DROP TABLE IF EXISTS `EventSubType`;
DROP TABLE IF EXISTS `EventType`;
DROP TABLE IF EXISTS `SpecialAchiever`;
DROP TABLE IF EXISTS `SpecialAchievement`;
DROP TABLE IF EXISTS `Awardee`;
DROP TABLE IF EXISTS `Sport`;
DROP TABLE IF EXISTS `Award`;
DROP TABLE IF EXISTS `Squad`;
DROP TABLE IF EXISTS `CoachSeason`;
DROP TABLE IF EXISTS `CoachType`;
DROP TABLE IF EXISTS `Coach`;
DROP TABLE IF EXISTS `Result`;
DROP TABLE IF EXISTS `Race`;
DROP TABLE IF EXISTS `Course`;
DROP TABLE IF EXISTS `RaceName`;
DROP TABLE IF EXISTS `RaceCondition`;
DROP TABLE IF EXISTS `Location`;
DROP TABLE IF EXISTS `State`;
DROP TABLE IF EXISTS `CourseType`;
DROP TABLE IF EXISTS `Competitor`;
DROP TABLE IF EXISTS `Athlete`;
DROP TABLE IF EXISTS `Gender`;



-- CREATING TABLES

-- Common
CREATE TABLE `Gender` (
	`genderId` TINYINT NOT NULL AUTO_INCREMENT,
	`gender` VARCHAR(191) UNIQUE NOT NULL,

	PRIMARY KEY (`genderId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Common
CREATE TABLE `Athlete` (
	`athleteId` BIGINT NOT NULL AUTO_INCREMENT,
	`firstName` VARCHAR(191) NOT NULL,
	`lastName` VARCHAR(191) NOT NULL,
	`startHsYear` YEAR NOT NULL,
	`endHsYear` YEAR NOT NULL,
	`genderId` TINYINT DEFAULT 1,
	`confidentHsYear` TINYINT(1) DEFAULT 1,
	
	PRIMARY KEY (`athleteId`),
	INDEX (`lastName`),
	UNIQUE KEY (`firstName`,`lastName`,`startHsYear`,`endHsYear`),
	FOREIGN KEY (`genderId`) REFERENCES `Gender` (`genderId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci AUTO_INCREMENT=1000000;



-- Common
CREATE TABLE `Competitor` (
	`competitorId` VARCHAR(15) NOT NULL,
	`athleteId` BIGINT NOT NULL,
	`year` YEAR NOT NULL,
	`grade` SMALLINT NOT NULL,
	
	PRIMARY KEY (`competitorId`,`athleteId`,`year`,`grade`),
	FOREIGN KEY (`athleteId`) REFERENCES `Athlete` (`athleteId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- XC
CREATE TABLE `CourseType` (
	`courseTypeId` TINYINT NOT NULL AUTO_INCREMENT,
	`courseType` VARCHAR(191) UNIQUE NOT NULL,

	PRIMARY KEY (`courseTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- XC, but could be common
CREATE TABLE `State` (
	`stateId` TINYINT NOT NULL AUTO_INCREMENT,
	`state` VARCHAR(191) UNIQUE NOT NULL,

	PRIMARY KEY (`stateId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- XC, but could be common
CREATE TABLE `Location` (
	`locationId` INT NOT NULL AUTO_INCREMENT,
	`stateId` TINYINT DEFAULT 1,
	`city` VARCHAR(191) NOT NULL,

	PRIMARY KEY (`locationId`),
	UNIQUE KEY (`stateId`,`city`),
	FOREIGN KEY (`stateId`) REFERENCES `State` (`stateId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci AUTO_INCREMENT=1000000;



-- XC, but could be common
CREATE TABLE `RaceCondition` (
	`raceConditionId` TINYINT NOT NULL AUTO_INCREMENT,
	`raceCondition` VARCHAR(191) UNIQUE NOT NULL,

	PRIMARY KEY (`raceConditionId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- XC, but could be common
CREATE TABLE `RaceName` (
	`raceNameId` TINYINT NOT NULL AUTO_INCREMENT,
	`raceName` VARCHAR(191) UNIQUE NOT NULL,

	PRIMARY KEY (`raceNameId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- XC
CREATE TABLE `Course` (
	`courseId` INT NOT NULL AUTO_INCREMENT,
	`courseName` VARCHAR(191) NOT NULL,
	`courseDistance` DECIMAL(4,2) NOT NULL,
	`locationId` INT DEFAULT 1,
	`courseTypeId` TINYINT DEFAULT 1,

	PRIMARY KEY (`courseId`),
	UNIQUE KEY (`courseName`,`courseDistance`,`locationId`),
	FOREIGN KEY (`locationId`) REFERENCES `Location` (`locationId`),
	FOREIGN KEY (`courseTypeId`) REFERENCES `CourseType` (`courseTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci AUTO_INCREMENT=1000000;



-- XC
CREATE TABLE `Race` (
	`raceId` BIGINT NOT NULL AUTO_INCREMENT,
	`raceNameId` TINYINT DEFAULT 1,
	`raceConditionId` TINYINT DEFAULT 1,
	`courseId` INT NOT NULL,
	`date` DATE NOT NULL,
	
	PRIMARY KEY (`raceId`),
	UNIQUE KEY (`courseId`,`date`),
	FOREIGN KEY (`raceNameId`) REFERENCES `RaceName` (`raceNameId`),
	FOREIGN KEY (`raceConditionId`) REFERENCES `RaceCondition` (`raceConditionId`),
	FOREIGN KEY (`courseId`) REFERENCES `Course` (`courseId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci AUTO_INCREMENT=1000000;



-- XC
CREATE TABLE `Result` (
	`competitorId` VARCHAR(15) NOT NULL,
	`raceId` BIGINT NOT NULL,
	`time` TIME(1) NOT NULL,
	`pace` TIME(1) NOT NULL,
	
	PRIMARY KEY (`competitorId`,`raceId`),
	FOREIGN KEY (`competitorId`) REFERENCES `Competitor` (`competitorId`),
	FOREIGN KEY (`raceId`) REFERENCES `Race` (`raceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Common
CREATE TABLE `Coach` (
	`coachId` TINYINT NOT NULL AUTO_INCREMENT,
	`firstName` VARCHAR(191) NOT NULL,
	`lastName` VARCHAR(191) NOT NULL,
	`genderId` TINYINT DEFAULT 1,
	
	PRIMARY KEY (`coachId`),
	INDEX (`lastName`),
	UNIQUE KEY (`firstName`,`lastName`),
	FOREIGN KEY (`genderId`) REFERENCES `Gender` (`genderId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci AUTO_INCREMENT=1;



-- Common
CREATE TABLE `CoachType` (
	`coachTypeId` TINYINT NOT NULL AUTO_INCREMENT,
	`coachType` VARCHAR(191) UNIQUE NOT NULL,

	PRIMARY KEY (`coachTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Common
CREATE TABLE `CoachSeason` (
	`coachId` TINYINT NOT NULL,
	`coachTypeId` TINYINT NOT NULL,
	`year` YEAR NOT NULL,
	
	UNIQUE KEY (`coachId`, `coachTypeId`, `year`),
	FOREIGN KEY (`coachId`) REFERENCES `Coach` (`coachId`),
	FOREIGN KEY (`coachTypeId`) REFERENCES `CoachType` (`coachTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Common
CREATE TABLE `Squad` (
	`squadId` TINYINT NOT NULL AUTO_INCREMENT,
	`squadName` VARCHAR(191) UNIQUE NOT NULL,
	`squadAbbr` VARCHAR(7) UNIQUE NOT NULL,

	PRIMARY KEY (`squadId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Common
CREATE TABLE `Award` (
	`awardId` TINYINT NOT NULL AUTO_INCREMENT,
	`awardName` VARCHAR(191) UNIQUE NOT NULL,
	`awardShortName` VARCHAR(31) UNIQUE NOT NULL,

	PRIMARY KEY (`awardId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Common
CREATE TABLE `Sport` (
	`sportId` TINYINT NOT NULL AUTO_INCREMENT,
	`sportName` VARCHAR(191) UNIQUE NOT NULL,

	PRIMARY KEY (`sportId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Common
CREATE TABLE `Awardee` (
	`athleteId` BIGINT NOT NULL,
	`awardId` TINYINT NOT NULL,
	`squadId` TINYINT NOT NULL,
	`year` YEAR NOT NULL,
    `sportId` TINYINT DEFAULT 1,

	UNIQUE KEY (`athleteId`,`awardId`,`squadId`,`year`),
	FOREIGN KEY (`athleteId`) REFERENCES `Athlete` (`athleteId`), 
	FOREIGN KEY (`awardId`) REFERENCES `Award` (`awardId`), 
	FOREIGN KEY (`squadId`) REFERENCES `Squad` (`squadId`), 
	FOREIGN KEY (`sportId`) REFERENCES `Sport` (`sportId`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Common
CREATE TABLE `SpecialAchievement` (
	`specialAchievementId` TINYINT NOT NULL AUTO_INCREMENT,
	`specialAchievementName` VARCHAR(191) UNIQUE NOT NULL,

	PRIMARY KEY (`specialAchievementId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Common
CREATE TABLE `SpecialAchiever` (
	`competitorId` VARCHAR(15) NOT NULL,
	`specialAchievementId` TINYINT NOT NULL,
	`notes` VARCHAR(191) NOT NULL,
    `sportId` TINYINT DEFAULT 1,
	`year` YEAR NOT NULL,

	UNIQUE KEY (`competitorId`,`specialAchievementId`),
	FOREIGN KEY (`competitorId`) REFERENCES `Competitor` (`competitorId`), 
	FOREIGN KEY (`specialAchievementId`) REFERENCES `SpecialAchievement` (`specialAchievementId`),
	FOREIGN KEY (`sportId`) REFERENCES `Sport` (`sportId`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Track & Field
CREATE TABLE `EventType` (
	`eventTypeId` TINYINT NOT NULL AUTO_INCREMENT,
	`eventType` VARCHAR(191) UNIQUE NOT NULL,

	PRIMARY KEY (`eventTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Track & Field
CREATE TABLE `EventSubType` (
	`eventSubTypeId` TINYINT NOT NULL AUTO_INCREMENT,
	`eventSubType` VARCHAR(191) UNIQUE NOT NULL,
	`eventTypeId` TINYINT,

	PRIMARY KEY (`eventSubTypeId`),
	FOREIGN KEY (`eventTypeId`) REFERENCES `EventType` (`eventTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Track & Field
CREATE TABLE `Event` (
	`eventId` TINYINT NOT NULL AUTO_INCREMENT,
	`event` VARCHAR(191) UNIQUE NOT NULL,
	`eventSubTypeId` TINYINT,

	PRIMARY KEY (`eventId`),
	FOREIGN KEY (`eventSubTypeId`) REFERENCES `EventSubType` (`eventSubTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Track & Field
CREATE TABLE `FieldResult` (
	`competitorId` VARCHAR(15) NOT NULL,
	`eventId` TINYINT,
	`footPartOfDistance` SMALLINT,
    `inchPartOfDistance` DECIMAL(4, 2),
	`year` YEAR NOT NULL,
	`squadId` TINYINT NOT NULL,

	PRIMARY KEY (`competitorId`,`eventId`),
	FOREIGN KEY (`competitorId`) REFERENCES `Competitor` (`competitorId`),
	FOREIGN KEY (`eventId`) REFERENCES Event(`eventId`),
	FOREIGN KEY (`squadId`) REFERENCES `Squad` (`squadId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Track & Field
CREATE TABLE `RaceTimeType` (
	`raceTimeTypeId` VARCHAR(1) UNIQUE NOT NULL,
	`raceTimeType` VARCHAR(191) UNIQUE NOT NULL,

	PRIMARY KEY (`raceTimeTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Track & Field
CREATE TABLE `RaceResult` (
	`competitorId` VARCHAR(15) NOT NULL,
	`eventId` TINYINT,
	`time` TIME(2) NOT NULL,
    `raceTimeTypeId` VARCHAR(1) NOT NULL DEFAULT "",
	`year` YEAR NOT NULL,
	`squadId` TINYINT NOT NULL,
	
	PRIMARY KEY (`competitorId`,`eventId`),
	FOREIGN KEY (`competitorId`) REFERENCES `Competitor` (`competitorId`),
	FOREIGN KEY (`eventId`) REFERENCES `Event` (`eventId`),
	FOREIGN KEY (`raceTimeTypeId`) REFERENCES `RaceTimeType` (`raceTimeTypeId`),
	FOREIGN KEY (`squadId`) REFERENCES `Squad` (`squadId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



-- Track & Field
CREATE TABLE `RelayResult` (
	`competitorId1` VARCHAR(15) NOT NULL,
	`competitorId2` VARCHAR(15) NOT NULL,
	`competitorId3` VARCHAR(15) NOT NULL,
	`competitorId4` VARCHAR(15) NOT NULL,
	`eventId` TINYINT,
	`time` TIME(2) NOT NULL,
    `raceTimeTypeId` VARCHAR(1) NOT NULL DEFAULT "",
	`year` YEAR NOT NULL,
	`squadId` TINYINT NOT NULL,
	
	PRIMARY KEY (`competitorId1`,`competitorId2`,`competitorId3`,`competitorId4`,`eventId`),
	FOREIGN KEY (`competitorId1`) REFERENCES `Competitor` (`competitorId`),
	FOREIGN KEY (`competitorId2`) REFERENCES `Competitor` (`competitorId`),
	FOREIGN KEY (`competitorId3`) REFERENCES `Competitor` (`competitorId`),
	FOREIGN KEY (`competitorId4`) REFERENCES `Competitor` (`competitorId`),
	FOREIGN KEY (`eventId`) REFERENCES `Event` (`eventId`),
	FOREIGN KEY (`raceTimeTypeId`) REFERENCES `RaceTimeType` (`raceTimeTypeId`),
	FOREIGN KEY (`squadId`) REFERENCES `Squad` (`squadId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



COMMIT;
