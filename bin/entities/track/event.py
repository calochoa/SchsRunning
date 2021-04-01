__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


class Event(object):

    MYSQL_KEY_EVENT = "event"
    MYSQL_KEY_EVENT_ID = "eventId"
    MYSQL_KEY_EVENT_SUB_TYPE = "eventSubType"
    MYSQL_KEY_EVENT_SUB_TYPE_ID = "eventSubTypeId"

    JSON_KEY_EVENT = "Event"
    JSON_KEY_EVENT_ID = "EventId"
    JSON_KEY_EVENT_SUB_TYPE = "EventSubType"

    def __init__(self, db_row):
        self.event = str(db_row.get(self.MYSQL_KEY_EVENT))
        self.event_id = db_row.get(self.MYSQL_KEY_EVENT_ID)
        self.event_sub_type = str(db_row.get(self.MYSQL_KEY_EVENT_SUB_TYPE))
        self.event_sub_type_id = db_row.get(self.MYSQL_KEY_EVENT_SUB_TYPE_ID)

    def get_json(self):
        return {
            self.JSON_KEY_EVENT: self.event,
            self.JSON_KEY_EVENT_ID: self.event_id,
            self.JSON_KEY_EVENT_SUB_TYPE: self.event_sub_type,
        }
        