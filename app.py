
__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Flask, render_template

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

# workout related apps
from bin.apps.workouts.workouts_app import workouts_app
from bin.apps.workouts.workouts_db_app import workouts_db_app
from bin.apps.workouts.bodyweight_exercises_seo_app import bodyweight_exercises_seo_app
from bin.apps.workouts.quickies_seo_app import quickies_seo_app


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

app.register_blueprint(shared_db_app)

app.register_blueprint(track_app)
app.register_blueprint(track_db_app)
app.register_blueprint(track_hall_of_fame_seo_app)
app.register_blueprint(track_season_seo_app)
app.register_blueprint(track_results_seo_app)
app.register_blueprint(track_competitors_seo_app)
app.register_blueprint(track_athletes_seo_app)
app.register_blueprint(track_coaches_seo_app)

app.register_blueprint(workouts_app)
app.register_blueprint(workouts_db_app)
app.register_blueprint(bodyweight_exercises_seo_app)
app.register_blueprint(quickies_seo_app)

app.config.update(
    PROPAGATE_EXCEPTIONS = True
)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/related-sites',methods=['GET'])
@app.route('/relatedSites',methods=['GET'])
def relatedSites():
    return render_template('relatedSites.html')


if __name__ == "__main__":
    app.run()
    # https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql-part-3--cms-23120

