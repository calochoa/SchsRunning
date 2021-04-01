__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from bin.cache import cache as mc_cache


KEY_DELIM = '[#]'


class Utils(object):

    def __init__(self):
        pass

    @staticmethod
    def cache_get(cache_key):
        try:
            # cache is disabled..
            return None
            #return mc_cache.get(cache_key)
        except Exception as e:
            logging.exception(e)
            return None

    @staticmethod
    def cache_set(cache_key, cache_value):
        try:
            # cache is disabled..
            pass
            #mc_cache.set(cache_key, cache_value)
        except Exception as e:
            logging.exception(e)
        
    @staticmethod
    def formatTime(time):
        time_str = str(time)[:9]
        if time_str.startswith('0:'):
            time_str = time_str[2:]
        if time_str.startswith('0'):
            time_str = time_str[1:]
        return time_str

    @staticmethod
    def formatDistance(distance):
        distance_str = str(distance)
        if distance_str.endswith('.00'):
            distance_str = distance_str[:-3]
        elif distance_str.endswith('0'):
        	distance_str = distance_str[:-1]
        return distance_str
    
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
    def format_track_time(time):
        time_str = str(time)
        if time_str.startswith('00:'):
            time_str = str(time)[1:11]
        else:
            time_str = str(time)[:10]

        if time_str.startswith('0:'):
            time_str = time_str[2:]
        if time_str.startswith('00:'):
            time_str = time_str[3:]
        if time_str.startswith('0'):
            time_str = time_str[1:]
        if '.' in time_str and time_str.endswith('0'):
            time_str = time_str[:-1]
        if '.' not in time_str:
            time_str += '.0'
        # time is a minute+, so we want to keep it in seconds IF its under 90 seconds
        if time_str.startswith('1:'):
            seconds = float(time_str[2:])
            if seconds < 30:
                time_str = str(seconds + 60)
        return time_str

    @staticmethod
    def get_cache_key_one(name, param_1):
        return '{0}{1}'.format(name, param_1)

    @staticmethod
    def get_cache_key_two(name, param_1, param_2):
        return '{0}{2}{1}{3}'.format(name, KEY_DELIM, param_1, param_2)

    @staticmethod
    def get_cache_key_three(name, param_1, param_2, param_3):
        return '{0}{2}{1}{3}{1}{4}'.format(name, KEY_DELIM, param_1, param_2, param_3)

    @staticmethod
    def get_cache_key_four(name, param_1, param_2, param_3, param_4):
        return '{0}{2}{1}{3}{1}{4}{1}{5}'.format(name, KEY_DELIM, param_1, param_2, param_3, param_4)
