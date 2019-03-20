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
FROM `Exercises` NATURAL JOIN `BodySplits` NATURAL JOIN `Videos`
	 LEFT JOIN `ExerciseTypes` ON (`Exercises`.`etId`= `ExerciseTypes`.`etId`)
WHERE `youtubeId` IS NOT NULL AND FIND_IN_SET(`eLevel`, `inputLevels`) 
	AND FIND_IN_SET(`bsId`, `inputBodySplitId`) 
ORDER BY `eLevel`, `eName`;


END //
DELIMITER ;


CALL `GetAllExercises`();
CALL `GetExercises`("1,2,3,4,5,6", "bs0002");
CALL `GetExercises`("1", "bs0001,bs0002,bs0003,bs0004");
