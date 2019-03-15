__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


track_season_seo_app = Blueprint(
    'track_season_seo_app', __name__, template_folder='template', url_prefix='/santa-clara-high-track-and-field/season'
)    


@track_season_seo_app.route('/<year>',methods=['GET'])
def trackSeasonDNE(year=None):
    return render_template('error.html', error='No data for {0} season'.format(year))

@track_season_seo_app.route('/<int:year>',methods=['GET'])
def trackSeasons(year):
    return render_template('track/season/season.html', yr=year, coachTypeIds="3,4,5,6,7,8")

