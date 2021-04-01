__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


class QuickieWorkout(object):

    MYSQL_KEY_WORKOUT_ID = "wId"
    MYSQL_KEY_WORKOUT_NAME = "wName"
    MYSQL_KEY_WORKOUT_DIFFICULTY = "wDifficulty"
    MYSQL_KEY_BODY_SPLIT_NAME = "bsName"
    MYSQL_KEY_QUICKIE_IDS = "qids"

    JSON_KEY_WORKOUT_ID = "WorkoutId"
    JSON_KEY_WORKOUT_NAME = "WorkoutName"
    JSON_KEY_WORKOUT_LEVEL = "WorkoutLevel"
    JSON_KEY_BODY_SPLIT = "BodySplit"
    JSON_KEY_QUICKIES = "Quickies"
    JSON_KEY_ALL = "All"

    def __init__(self, db_row, all_workouts=False):
        self.workout_id = str(db_row.get(self.MYSQL_KEY_WORKOUT_ID))
        self.workout_name = str(db_row.get(self.MYSQL_KEY_WORKOUT_NAME)).title()
        self.workout_difficulty = db_row.get(self.MYSQL_KEY_WORKOUT_DIFFICULTY)
        self.body_split_name = str(db_row.get(self.MYSQL_KEY_BODY_SPLIT_NAME))
        self.quickie_ids = db_row.get(self.MYSQL_KEY_QUICKIE_IDS)
        self.quickie_json_list = None
        self.all_workouts = all_workouts

    def set_quickie_json_list(self, quickie_json_dict):
        if quickie_json_dict:
            quickie_id_list = [quickie_id.strip() for quickie_id in self.quickie_ids.split(',')]
            self.quickie_json_list = [quickie_json_dict.get(qid) for qid in quickie_id_list]

    def get_json(self):
        return {
            self.JSON_KEY_WORKOUT_ID: self.workout_id,
            self.JSON_KEY_WORKOUT_NAME: self.workout_name,
            self.JSON_KEY_WORKOUT_LEVEL: self.workout_difficulty,
            self.JSON_KEY_BODY_SPLIT: self.body_split_name,
            self.JSON_KEY_QUICKIES: self.quickie_json_list,
            self.JSON_KEY_ALL: self.all_workouts,
        }
