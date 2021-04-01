__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


class Exercise(object):

    MYSQL_KEY_EXERCISE_ID = "eId"
    MYSQL_KEY_EXERCISE_NAME = "eName"
    MYSQL_KEY_EXERCISE_LEVEL = "eLevel"
    MYSQL_KEY_BODY_SPLIT_NAME = "bsName"
    MYSQL_KEY_EXERCISE_TYPE_NAME = "etName"
    MYSQL_KEY_YOU_TUBE_ID = "youtubeId"

    JSON_KEY_EXERCISE_ID = "ExerciseId"
    JSON_KEY_EXERCISE_NAME = "ExerciseName"
    JSON_KEY_EXERCISE_LEVEL = "ExerciseLevel"
    JSON_KEY_BODY_SPLIT = "BodySplit"
    JSON_KEY_EXERCISE_TYPE = "ExerciseType"
    JSON_KEY_YOU_TUBE_ID = "YouTubeId"
    JSON_KEY_ALL = "All"

    def __init__(self, db_row, all_exercises=False, exercise_name=None, you_tube_id=None):
        self.exercise_id = str(db_row.get(self.MYSQL_KEY_EXERCISE_ID))
        self.exercise_name = str(self.__get_valid_value(exercise_name, db_row, self.MYSQL_KEY_EXERCISE_NAME)).title()
        self.exercise_level = db_row.get(self.MYSQL_KEY_EXERCISE_LEVEL)
        self.body_split_name = str(db_row.get(self.MYSQL_KEY_BODY_SPLIT_NAME))
        self.exercise_type_name = str(db_row.get(self.MYSQL_KEY_EXERCISE_TYPE_NAME))
        self.you_tube_id = str(self.__get_valid_value(you_tube_id, db_row, self.MYSQL_KEY_YOU_TUBE_ID))
        self.all_exercises = all_exercises

    def __get_valid_value(self, value, db_row, key):
        return value if value else db_row.get(key)

    def get_json(self):
        return {
            self.JSON_KEY_EXERCISE_ID: self.exercise_id,
            self.JSON_KEY_EXERCISE_NAME: self.exercise_name,
            self.JSON_KEY_EXERCISE_LEVEL: self.exercise_level,
            self.JSON_KEY_BODY_SPLIT: self.body_split_name,
            self.JSON_KEY_EXERCISE_TYPE: self.exercise_type_name,
            self.JSON_KEY_YOU_TUBE_ID: self.you_tube_id,
            self.JSON_KEY_ALL: self.all_exercises,
        }
        