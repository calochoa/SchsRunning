__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


class Squad(object):

    MYSQL_KEY_SQUAD_NAME = "squadName"
    MYSQL_KEY_SQUAD_ID = "squadID"
    MYSQL_KEY_SQUAD_ID_2 = "squadId"

    JSON_KEY_SQUAD = "Squad"
    JSON_KEY_SQUAD_ID = "SquadId"

    def __init__(self, db_row):
        self.squad_name = str(db_row.get(self.MYSQL_KEY_SQUAD_NAME))
        self.squad_id = self.__get_squad_id(db_row)

    def __get_squad_id(self, db_row):
        squad_id = db_row.get(self.MYSQL_KEY_SQUAD_ID)
        if squad_id is None:
            squad_id = db_row.get(self.MYSQL_KEY_SQUAD_ID_2)
        return squad_id

    def get_json(self):
        return {
            self.JSON_KEY_SQUAD: self.squad_name,
            self.JSON_KEY_SQUAD_ID: self.squad_id,
        }
        