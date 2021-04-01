__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

from bin.entities.workouts.exercise import Exercise


class Quickie(object):

    MYSQL_KEY_QUICKIE_ID = "qId"
    MYSQL_KEY_QUICKIE_NAME = "qName"
    MYSQL_KEY_QUICKIE_DIFFICULTY = "qDifficulty"
    MYSQL_KEY_QUICKIE_TYPE_NAME = "qtName"
    MYSQL_KEY_BODY_SPLIT_NAME = "bsName"
    MYSQL_KEY_REPS_1 = "reps1"
    MYSQL_KEY_REPS_2 = "reps2"
    MYSQL_KEY_REPS_3 = "reps3"
    MYSQL_KEY_REPS_4 = "reps4"
    MYSQL_KEY_EXERCISE_NAME_1 = "eName1"
    MYSQL_KEY_EXERCISE_NAME_2 = "eName2"
    MYSQL_KEY_EXERCISE_NAME_3 = "eName3"
    MYSQL_KEY_EXERCISE_NAME_4 = "eName4"
    MYSQL_KEY_YOU_TUBE_ID_1 = "youtubeId1"
    MYSQL_KEY_YOU_TUBE_ID_2 = "youtubeId2"
    MYSQL_KEY_YOU_TUBE_ID_3 = "youtubeId3"
    MYSQL_KEY_YOU_TUBE_ID_4 = "youtubeId4"

    JSON_KEY_QUICKIE_ID = "QuickieId"
    JSON_KEY_QUICKIE_NAME = "QuickieName"
    JSON_KEY_QUICKIE_LEVEL = "QuickieLevel"
    JSON_KEY_QUICKIE_TYPE = "QuickieType"
    JSON_KEY_BODY_SPLIT = "BodySplit"
    JSON_KEY_REPS_1 = "Reps1"
    JSON_KEY_REPS_2 = "Reps2"
    JSON_KEY_REPS_3 = "Reps3"
    JSON_KEY_REPS_4 = "Reps4"
    JSON_KEY_EXERCISE_NAME_1 = "ExerciseName1"
    JSON_KEY_EXERCISE_NAME_2 = "ExerciseName2"
    JSON_KEY_EXERCISE_NAME_3 = "ExerciseName3"
    JSON_KEY_EXERCISE_NAME_4 = "ExerciseName4"
    JSON_KEY_YOU_TUBE_ID_1 = "YouTubeId1"
    JSON_KEY_YOU_TUBE_ID_2 = "YouTubeId2"
    JSON_KEY_YOU_TUBE_ID_3 = "YouTubeId3"
    JSON_KEY_YOU_TUBE_ID_4 = "YouTubeId4"
    JSON_KEY_ALL = "All"

    def __init__(self, db_row, all_quickies=False):
        self.quickie_id = str(db_row.get(self.MYSQL_KEY_QUICKIE_ID))
        self.quickie_name = str(db_row.get(self.MYSQL_KEY_QUICKIE_NAME))
        self.quickie_difficulty = db_row.get(self.MYSQL_KEY_QUICKIE_DIFFICULTY)
        self.quickie_type_name = str(db_row.get(self.MYSQL_KEY_QUICKIE_TYPE_NAME))
        self.body_split_name = str(db_row.get(self.MYSQL_KEY_BODY_SPLIT_NAME))
        self.reps_1 = db_row.get(self.MYSQL_KEY_REPS_1)
        self.reps_2 = db_row.get(self.MYSQL_KEY_REPS_2)
        self.reps_3 = db_row.get(self.MYSQL_KEY_REPS_3)
        self.reps_4 = db_row.get(self.MYSQL_KEY_REPS_4)
        self.exercise_1 = self.__get_exercise(
            db_row, self.MYSQL_KEY_EXERCISE_NAME_1, self.MYSQL_KEY_YOU_TUBE_ID_1
        )
        self.exercise_2 = self.__get_exercise(
            db_row, self.MYSQL_KEY_EXERCISE_NAME_2, self.MYSQL_KEY_YOU_TUBE_ID_2
        )
        self.exercise_3 = self.__get_exercise(
            db_row, self.MYSQL_KEY_EXERCISE_NAME_3, self.MYSQL_KEY_YOU_TUBE_ID_3
        )
        self.exercise_4 = self.__get_exercise(
            db_row, self.MYSQL_KEY_EXERCISE_NAME_4, self.MYSQL_KEY_YOU_TUBE_ID_4
        )
        self.all_quickies = all_quickies

    def __get_exercise(self, db_row, exercise_name_key, you_tube_id_key):
        return Exercise(
            db_row, exercise_name=db_row.get(exercise_name_key), 
            you_tube_id=db_row.get(you_tube_id_key)
        )

    def get_json(self):
        return {
            self.JSON_KEY_QUICKIE_ID: self.quickie_id,
            self.JSON_KEY_QUICKIE_NAME: self.quickie_name,
            self.JSON_KEY_QUICKIE_LEVEL: self.quickie_difficulty,
            self.JSON_KEY_QUICKIE_TYPE: self.quickie_type_name,
            self.JSON_KEY_BODY_SPLIT: self.body_split_name,
            self.JSON_KEY_REPS_1: self.reps_1,
            self.JSON_KEY_REPS_2: self.reps_2,
            self.JSON_KEY_REPS_3: self.reps_3,
            self.JSON_KEY_REPS_4: self.reps_4,
            self.JSON_KEY_EXERCISE_NAME_1: self.exercise_1.exercise_name,
            self.JSON_KEY_EXERCISE_NAME_2: self.exercise_2.exercise_name,
            self.JSON_KEY_EXERCISE_NAME_3: self.exercise_3.exercise_name,
            self.JSON_KEY_EXERCISE_NAME_4: self.exercise_4.exercise_name,
            self.JSON_KEY_YOU_TUBE_ID_1: self.exercise_1.you_tube_id,
            self.JSON_KEY_YOU_TUBE_ID_2: self.exercise_2.you_tube_id,
            self.JSON_KEY_YOU_TUBE_ID_3: self.exercise_3.you_tube_id,
            self.JSON_KEY_YOU_TUBE_ID_4: self.exercise_4.you_tube_id,
            self.JSON_KEY_ALL: self.all_quickies,
        }
