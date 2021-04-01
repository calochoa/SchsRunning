DROP DATABASE IF EXISTS `quickies`;

-- CREATING DATABASE
CREATE DATABASE IF NOT EXISTS `quickies`
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci
;


USE `quickies`;

DROP TABLE IF EXISTS `WorkoutOfTheDay`;
DROP TABLE IF EXISTS `QuickieOfTheDay`;
DROP TABLE IF EXISTS `OfTheDay`;
DROP TABLE IF EXISTS `QuickieWorkouts`;
DROP TABLE IF EXISTS `Quickies`;
DROP TABLE IF EXISTS `QuickieTypes`;
DROP TABLE IF EXISTS `Exercises`;
DROP TABLE IF EXISTS `Videos`;
DROP TABLE IF EXISTS `ExerciseTypes`;
DROP TABLE IF EXISTS `BodySplits`;



CREATE TABLE IF NOT EXISTS `BodySplits` (
    `bsId` VARCHAR(6) UNIQUE NOT NULL,
    `bsName` VARCHAR(255),
    `bsDescription` VARCHAR(255),
    `order` INT,
    
	PRIMARY KEY (`bsId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



CREATE TABLE IF NOT EXISTS `ExerciseTypes` (
    `etId` VARCHAR(6) UNIQUE NOT NULL,
    `etName` VARCHAR(255),
    `etDescription` VARCHAR(255),
    `order` INT,
    
	PRIMARY KEY (`etId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



CREATE TABLE IF NOT EXISTS `Videos` (
    `vId` VARCHAR(7) UNIQUE NOT NULL,
    `youtubeId` VARCHAR(12) DEFAULT NULL,
    
	PRIMARY KEY (`vId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



CREATE TABLE IF NOT EXISTS `Exercises` (
    `eId` VARCHAR(7) UNIQUE NOT NULL,
    `eName` VARCHAR(255),
    `eLevel` INT,
    `vId` VARCHAR(7),
    `bsId` VARCHAR(6),
    `etId` VARCHAR(6),
    
	PRIMARY KEY (`eId`),
    FOREIGN KEY (`vId`) REFERENCES `Videos` (`vId`),
	FOREIGN KEY (`bsId`) REFERENCES `BodySplits` (`bsId`),
	FOREIGN KEY (`etId`) REFERENCES `ExerciseTypes` (`etId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



CREATE TABLE IF NOT EXISTS `QuickieTypes` (
    `qtId` VARCHAR(6) UNIQUE NOT NULL,
    `qtName` VARCHAR(255),
    `qtDescription` VARCHAR(255),
    `order` INT,
    
	PRIMARY KEY (`qtId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



CREATE TABLE IF NOT EXISTS `Quickies` (
    `qId` VARCHAR(6) UNIQUE NOT NULL,
    `qtId` VARCHAR(6),
    `qDifficulty` INT,
    `bsId` VARCHAR(6),
    `qName` VARCHAR(255),
    `reps1` INT,
    `eId1` VARCHAR(7),
    `reps2` INT,
    `eId2` VARCHAR(7),
    `reps3` INT,
    `eId3` VARCHAR(7),
    `reps4` INT,
    `eId4` VARCHAR(7),
    
	PRIMARY KEY (`qId`),
	FOREIGN KEY (`qtId`) REFERENCES `QuickieTypes` (`qtId`),
	FOREIGN KEY (`bsId`) REFERENCES `BodySplits` (`bsId`),
	FOREIGN KEY (`eId1`) REFERENCES `Exercises` (`eId`),
	FOREIGN KEY (`eId2`) REFERENCES `Exercises` (`eId`),
	FOREIGN KEY (`eId3`) REFERENCES `Exercises` (`eId`),
	FOREIGN KEY (`eId4`) REFERENCES `Exercises` (`eId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



CREATE TABLE IF NOT EXISTS `QuickieWorkouts` (
    `wId` VARCHAR(5),
    `wName` VARCHAR(11),
    `wDifficulty` INT,
    `bsId` VARCHAR(6),
    `qIds` VARCHAR(255),
    
	PRIMARY KEY (`wId`),
	FOREIGN KEY (`bsId`) REFERENCES `BodySplits` (`bsId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;



/*
 * Will stop here because I don't know if I want to include these type of features online... save for mobile?
*/



CREATE TABLE IF NOT EXISTS `OfTheDay` (
    `otdId` VARCHAR(7) UNIQUE NOT NULL,
    `otdName` VARCHAR(255),
    `otdAbbr` VARCHAR(15),
    `order` INT,
    
	PRIMARY KEY (`otdId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



CREATE TABLE IF NOT EXISTS `QuickieOfTheDay` (
    `otdId` VARCHAR(7) UNIQUE NOT NULL,
    `qotd_0_0` VARCHAR(6),
    `qotd_1_0` VARCHAR(6),
    `qotd_2_0` VARCHAR(6),
    `qotd_3_0` VARCHAR(6),
    `qotd_4_0` VARCHAR(6),
    `qotd_5_0` VARCHAR(6),
    `qotd_6_0` VARCHAR(6),
    `qotd_0_1` VARCHAR(6),
    `qotd_1_1` VARCHAR(6),
    `qotd_2_1` VARCHAR(6),
    `qotd_3_1` VARCHAR(6),
    `qotd_4_1` VARCHAR(6),
    `qotd_5_1` VARCHAR(6),
    `qotd_6_1` VARCHAR(6),
    `order` INT,
    
	PRIMARY KEY (`otdId`),
	FOREIGN KEY (`otdId`) REFERENCES `OfTheDay` (`otdId`),
	FOREIGN KEY (`qotd_0_0`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_1_0`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_2_0`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_3_0`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_4_0`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_5_0`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_6_0`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_0_1`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_1_1`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_2_1`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_3_1`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_4_1`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_5_1`) REFERENCES `Quickies` (`qId`),
	FOREIGN KEY (`qotd_6_1`) REFERENCES `Quickies` (`qId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



CREATE TABLE IF NOT EXISTS `WorkoutOfTheDay` (
    `otdId` VARCHAR(7) UNIQUE NOT NULL,
    `wotd_0` VARCHAR(5),
    `wotd_1` VARCHAR(5),
    `wotd_2` VARCHAR(5),
    `wotd_3` VARCHAR(5),
    `wotd_4` VARCHAR(5),
    `wotd_5` VARCHAR(5),
    `wotd_6` VARCHAR(5),
    `order` INT,
    
	PRIMARY KEY (`otdId`),
	FOREIGN KEY (`otdId`) REFERENCES `OfTheDay` (`otdId`),
	FOREIGN KEY (`wotd_0`) REFERENCES `Workouts` (`wId`),
	FOREIGN KEY (`wotd_1`) REFERENCES `Workouts` (`wId`),
	FOREIGN KEY (`wotd_2`) REFERENCES `Workouts` (`wId`),
	FOREIGN KEY (`wotd_3`) REFERENCES `Workouts` (`wId`),
	FOREIGN KEY (`wotd_4`) REFERENCES `Workouts` (`wId`),
	FOREIGN KEY (`wotd_5`) REFERENCES `Workouts` (`wId`),
	FOREIGN KEY (`wotd_6`) REFERENCES `Workouts` (`wId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



COMMIT;
