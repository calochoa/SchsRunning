USE `quickies`;



DROP PROCEDURE IF EXISTS `GetAllExercises`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetAllExercises`()
BEGIN

SELECT `eId`, `eName`, `eLevel`, `bsName`, `etName`, `youtubeId`
FROM `Exercises` 
	LEFT JOIN `BodySplits` ON (`Exercises`.`bsId`= `BodySplits`.`bsId`) 
	LEFT JOIN `ExerciseTypes` ON (`Exercises`.`etId`= `ExerciseTypes`.`etId`)
	LEFT JOIN `Videos` ON (`Exercises`.`vId`= `Videos`.`vId`)
WHERE `youtubeId` IS NOT NULL
ORDER BY `eLevel`, `eName`;


END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetExercises`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetExercises`(
	IN `inputLevels` VARCHAR(15),
	IN `inputBodySplitId` VARCHAR(70)
)
BEGIN

SELECT `eId`, `eName`, `eLevel`, `bsName`, `etName`, `youtubeId`
FROM `Exercises` 
	LEFT JOIN `BodySplits` ON (`Exercises`.`bsId`= `BodySplits`.`bsId`) 
	LEFT JOIN `ExerciseTypes` ON (`Exercises`.`etId`= `ExerciseTypes`.`etId`)
	LEFT JOIN `Videos` ON (`Exercises`.`vId`= `Videos`.`vId`)
WHERE `youtubeId` IS NOT NULL AND FIND_IN_SET(`eLevel`, `inputLevels`) 
	AND FIND_IN_SET(`Exercises`.`bsId`, `inputBodySplitId`) 
ORDER BY `eLevel`, `eName`;


END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetAllQuickies`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetAllQuickies`()
BEGIN

SELECT `qId`, `qName`, `qDifficulty`, `qtName`, `bsName`, 
    `reps1`, `e1`.`eName` AS `eName1`, `v1`.`youtubeId` AS `youtubeId1`,
    `reps2`, `e2`.`eName` AS `eName2`, `v2`.`youtubeId` AS `youtubeId2`,
    `reps3`, `e3`.`eName` AS `eName3`, `v3`.`youtubeId` AS `youtubeId3`,
	`reps4`, `e4`.`eName` AS `eName4`, `v4`.`youtubeId` AS `youtubeId4`
FROM `Quickies` 
	LEFT JOIN `BodySplits` ON (`Quickies`.`bsId`= `BodySplits`.`bsId`) 
	LEFT JOIN `QuickieTypes` ON (`Quickies`.`qtId`= `QuickieTypes`.`qtId`)
    LEFT JOIN `Exercises` AS `e1` ON (`eId1`=`e1`.`eId`)
	LEFT JOIN `Videos` AS `v1` ON (`e1`.`vId`= `v1`.`vId`)
    LEFT JOIN `Exercises` AS `e2` ON (`eId2`=`e2`.`eId`)
	LEFT JOIN `Videos` AS `v2` ON (`e2`.`vId`= `v2`.`vId`)
    LEFT JOIN `Exercises` AS `e3` ON (`eId3`=`e3`.`eId`)
	LEFT JOIN `Videos` AS `v3` ON (`e3`.`vId`= `v3`.`vId`)
    LEFT JOIN `Exercises` AS `e4` ON (`eId4`=`e4`.`eId`)
	LEFT JOIN `Videos` AS `v4` ON (`e4`.`vId`= `v4`.`vId`)
WHERE `qDifficulty` NOT IN (0,6)
ORDER BY `qDifficulty`, `qName`;

END //
DELIMITER ;



DROP PROCEDURE IF EXISTS `GetQuickies`;

SET NAMES utf8mb4;
SET collation_connection = 'utf8mb4_unicode_ci';

DELIMITER //
CREATE PROCEDURE `GetQuickies`(
	IN `inputDifficulties` VARCHAR(15),
	IN `inputBodySplitIds` VARCHAR(70)
)
BEGIN

SELECT `qId`, `qName`, `qDifficulty`, `qtName`, `bsName`, 
    `reps1`, `e1`.`eName` AS `eName1`, `v1`.`youtubeId` AS `youtubeId1`,
    `reps2`, `e2`.`eName` AS `eName2`, `v2`.`youtubeId` AS `youtubeId2`,
    `reps3`, `e3`.`eName` AS `eName3`, `v3`.`youtubeId` AS `youtubeId3`,
	`reps4`, `e4`.`eName` AS `eName4`, `v4`.`youtubeId` AS `youtubeId4`
FROM `Quickies` 
	LEFT JOIN `BodySplits` ON (`Quickies`.`bsId`= `BodySplits`.`bsId`) 
	LEFT JOIN `QuickieTypes` ON (`Quickies`.`qtId`= `QuickieTypes`.`qtId`)
    LEFT JOIN `Exercises` AS `e1` ON (`eId1`=`e1`.`eId`)
	LEFT JOIN `Videos` AS `v1` ON (`e1`.`vId`= `v1`.`vId`)
    LEFT JOIN `Exercises` AS `e2` ON (`eId2`=`e2`.`eId`)
	LEFT JOIN `Videos` AS `v2` ON (`e2`.`vId`= `v2`.`vId`)
    LEFT JOIN `Exercises` AS `e3` ON (`eId3`=`e3`.`eId`)
	LEFT JOIN `Videos` AS `v3` ON (`e3`.`vId`= `v3`.`vId`)
    LEFT JOIN `Exercises` AS `e4` ON (`eId4`=`e4`.`eId`)
	LEFT JOIN `Videos` AS `v4` ON (`e4`.`vId`= `v4`.`vId`)
WHERE `qDifficulty` NOT IN (0,6) AND FIND_IN_SET(`qDifficulty`, `inputDifficulties`) 
	AND FIND_IN_SET(`Quickies`.`bsId`, `inputBodySplitIds`) 
ORDER BY `qDifficulty`, `qName`;

END //
DELIMITER ;



CALL `GetAllExercises`();
CALL `GetExercises`("1,2,3,4,5,6", "bs0002");
CALL `GetExercises`("1", "bs0001,bs0002,bs0003,bs0004");
CALL `GetExercises`('1,2,3,4,5,6', 'bs0001,bs0002,bs0003,bs0004');
CALL `GetAllQuickies`();
CALL `GetQuickies`("1,2,3,4,5,6", "bs0002");
CALL `GetQuickies`("1", "bs0001,bs0002,bs0003,bs0004");
CALL `GetQuickies`('1,2,3,4,5', 'bs0001,bs0002,bs0003,bs0004');
