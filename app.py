
__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


import os
from flask import Flask, render_template, request
from bin.cache import cache as mc_cache

# cross country related apps
from bin.apps.xc.xc_app import xc_app
from bin.apps.xc.xc_db_app import xc_db_app
from bin.apps.xc.xc_course_results_seo_app import xc_course_results_seo_app
from bin.apps.xc.xc_season_seo_app import xc_season_seo_app
from bin.apps.xc.xc_runners_seo_app import xc_runners_seo_app
from bin.apps.xc.xc_coaches_seo_app import xc_coaches_seo_app
from bin.apps.xc.xc_special_achievements_seo_app import xc_special_achievements_seo_app
from bin.apps.xc.xc_awards_seo_app import xc_awards_seo_app
from bin.apps.xc.xc_photos_seo_app import xc_photos_seo_app
from bin.apps.xc.xc_videos_seo_app import xc_videos_seo_app
from bin.apps.xc.xc_race_results_seo_app import xc_race_results_seo_app
from bin.apps.xc.xc_competitors_seo_app import xc_competitors_seo_app
from bin.apps.xc.xc_alumni_seo_app import xc_alumni_seo_app

# shared related apps
from bin.apps.shared_db_app import shared_db_app

# track and field related apps
from bin.apps.track.track_app import track_app
from bin.apps.track.track_db_app import track_db_app
from bin.apps.track.track_hall_of_fame_seo_app import track_hall_of_fame_seo_app
from bin.apps.track.track_season_seo_app import track_season_seo_app
from bin.apps.track.track_results_seo_app import track_results_seo_app
from bin.apps.track.track_competitors_seo_app import track_competitors_seo_app
from bin.apps.track.track_athletes_seo_app import track_athletes_seo_app
from bin.apps.track.track_coaches_seo_app import track_coaches_seo_app
from bin.apps.track.track_events_seo_app import track_events_seo_app
from bin.apps.track.track_special_achievements_seo_app import track_special_achievements_seo_app

# workout related apps
from bin.apps.workouts.workouts_app import workouts_app
from bin.apps.workouts.workouts_db_app import workouts_db_app
from bin.apps.workouts.bodyweight_exercises_seo_app import bodyweight_exercises_seo_app
from bin.apps.workouts.quickies_seo_app import quickies_seo_app
from bin.apps.workouts.quickie_workouts_seo_app import quickie_workouts_seo_app


app = Flask(__name__)

app.register_blueprint(xc_app)
app.register_blueprint(xc_db_app)
app.register_blueprint(xc_course_results_seo_app)
app.register_blueprint(xc_season_seo_app)
app.register_blueprint(xc_runners_seo_app)
app.register_blueprint(xc_coaches_seo_app)
app.register_blueprint(xc_special_achievements_seo_app)
app.register_blueprint(xc_awards_seo_app)
app.register_blueprint(xc_photos_seo_app)
app.register_blueprint(xc_videos_seo_app)
app.register_blueprint(xc_race_results_seo_app)
app.register_blueprint(xc_competitors_seo_app)
app.register_blueprint(xc_alumni_seo_app)

app.register_blueprint(shared_db_app)

app.register_blueprint(track_app)
app.register_blueprint(track_db_app)
app.register_blueprint(track_hall_of_fame_seo_app)
app.register_blueprint(track_season_seo_app)
app.register_blueprint(track_results_seo_app)
app.register_blueprint(track_competitors_seo_app)
app.register_blueprint(track_athletes_seo_app)
app.register_blueprint(track_coaches_seo_app)
app.register_blueprint(track_events_seo_app)
app.register_blueprint(track_special_achievements_seo_app)

app.register_blueprint(workouts_app)
app.register_blueprint(workouts_db_app)
app.register_blueprint(bodyweight_exercises_seo_app)
app.register_blueprint(quickies_seo_app)
app.register_blueprint(quickie_workouts_seo_app)

app.config.update(
    PROPAGATE_EXCEPTIONS = True
)


cache_servers = os.environ.get('MEMCACHIER_SERVERS')
if cache_servers == None:
    # Fall back to simple in memory cache (development)
    mc_cache.init_app(app, config={'CACHE_TYPE': 'simple'})
else:
    cache_user = os.environ.get('MEMCACHIER_USERNAME') or ''
    cache_pass = os.environ.get('MEMCACHIER_PASSWORD') or ''
    mc_cache.init_app(app,
        config={'CACHE_TYPE': 'saslmemcached',
                'CACHE_MEMCACHED_SERVERS': cache_servers.split(','),
                'CACHE_MEMCACHED_USERNAME': cache_user,
                'CACHE_MEMCACHED_PASSWORD': cache_pass,
                'CACHE_OPTIONS': { 'behaviors': {
                    # Faster IO
                    'tcp_nodelay': True,
                    # Keep connection alive
                    'tcp_keepalive': True,
                    # Timeout for set/get requests
                    'connect_timeout': 2000, # ms
                    'send_timeout': 750 * 1000, # us
                    'receive_timeout': 750 * 1000, # us
                    '_poll_timeout': 2000, # ms
                    # Better failover
                    'ketama': True,
                    'remove_failed': 1,
                    'retry_timeout': 2,
                    'dead_timeout': 30}}})


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/related-sites',methods=['GET'])
@app.route('/relatedSites',methods=['GET'])
def relatedSites():
    return render_template('relatedSites.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error = str(error))


@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error = str(error))


if __name__ == "__main__":
    app.run()
    # https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql-part-3--cms-23120

