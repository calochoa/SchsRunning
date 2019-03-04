__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


class Utils(object):

    def __init__(self):
        pass

    @staticmethod
    def formatTime(time):
        timeStr = str(time)[:9]
        if timeStr.startswith('0:'):
            timeStr = timeStr[2:]
        if timeStr.startswith('0'):
            timeStr = timeStr[1:]
        return timeStr

    @staticmethod
    def formatDistance(distance):
        distanceStr = str(distance)
        if distanceStr.endswith('.00'):
            distanceStr = distanceStr[:-3]
        elif distanceStr.endswith('0'):
        	distanceStr = distanceStr[:-1]
        return distanceStr
    
    @staticmethod
    def getTimeDiff(time_1, time_2):
        time_1_sec = Utils.getSecondsFromTime(time_1)
        time_2_sec = Utils.getSecondsFromTime(time_2)
        return time_2_sec - time_1_sec

    @staticmethod
    def getSecondsFromTime(time):
        time_parts = time.split(':')
        return (int(time_parts[0]) * 60) + float(time_parts[1])

    @staticmethod
    def convertTeamTime(team_time_min,team_time_sec):
        time_min = team_time_min
        time_sec = team_time_sec
        if team_time_sec >= 60:
            extra_min = team_time_sec / 60
            time_sec = (extra_min - int(extra_min)) * 60
            time_min += int(extra_min)
        return Utils.formatTeamTime(time_min,time_sec)

    @staticmethod
    def getTeamAvgIndTime(team_time):
        time_parts = team_time.split(':')
        if len(time_parts) == 2:
            time_min = int(time_parts[0])
            time_sec = float(time_parts[1]) + (time_min * 60)
            avg_time = time_sec / 5 / 60
            avg_time_min = int(avg_time)
            avg_time_sec = (avg_time - avg_time_min) * 60
            return Utils.formatTeamTime(avg_time_min,avg_time_sec)

    @staticmethod
    def formatTeamTime(team_time_min,team_time_sec):
        min_str = str(team_time_min)
        sec_str = ('0' if team_time_sec < 10 else '') + str(round(team_time_sec,1))
        if sec_str.endswith('.0'):
           sec_str = sec_str[:-2]
        return min_str + ':' + sec_str

    @staticmethod
    def formatTrackTime(time):
        timeStr = str(time)[:10]
        if timeStr.startswith('0:'):
            timeStr = timeStr[2:]
        if timeStr.startswith('00:'):
            timeStr = timeStr[3:]
        if timeStr.startswith('0'):
            timeStr = timeStr[1:]
        if '.' in timeStr and timeStr.endswith('0'):
            timeStr = timeStr[:-1]
        if '.' not in timeStr:
            timeStr += '.0'
        return timeStr

