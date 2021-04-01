__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

from bin.utils import Utils


class XcCourse(object):

    MYSQL_KEY_COURSE_ID = "courseid"
    MYSQL_KEY_COURSE_NAME = "coursename"
    MYSQL_KEY_COURSE_DISTANCE = "coursedistance"
    MYSQL_KEY_CITY = "city"
    MYSQL_KEY_STATE = "state"
    MYSQL_KEY_COURSE_TYPE = "coursetype"

    JSON_KEY_COURSE_ID = "CourseId"
    JSON_KEY_COURSE_NAME = "CourseName"
    JSON_KEY_COURSE_DISTANCE = "CourseDistance"
    JSON_KEY_CITY = "City"
    JSON_KEY_STATE = "State"
    JSON_KEY_COURSE_TYPE = "CourseType"

    def __init__(self, db_row):
        self.course_id = db_row.get(self.MYSQL_KEY_COURSE_ID)
        self.course_name = db_row.get(self.MYSQL_KEY_COURSE_NAME)
        self.course_distance = Utils.formatDistance(db_row.get(self.MYSQL_KEY_COURSE_DISTANCE))
        self.city = db_row.get(self.MYSQL_KEY_CITY)
        self.state = db_row.get(self.MYSQL_KEY_STATE)
        self.course_type = db_row.get(self.MYSQL_KEY_COURSE_TYPE)

    def get_json(self):
        return {
            self.JSON_KEY_COURSE_ID: self.course_id,
            self.JSON_KEY_COURSE_NAME: self.course_name,
            self.JSON_KEY_COURSE_DISTANCE: self.course_distance,
            self.JSON_KEY_CITY: self.city,
            self.JSON_KEY_STATE: self.state,
            self.JSON_KEY_COURSE_TYPE: self.course_type,
        }
