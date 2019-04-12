__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


track_season_seo_app = Blueprint(
    'track_season_seo_app', __name__, template_folder='template', url_prefix='/santa-clara-high-track-and-field/season'
)    


@track_season_seo_app.route('/<int:year>',methods=['GET'])
def track_seasons(year):
	return render_template('track/season/season.html', yr=year, coachTypeIds='3,4,5,6,7,8,9')

@track_season_seo_app.route('/',methods=['GET'])
def track_season_page_not_found():
	return render_template('error.html', error='Page not found')	

@track_season_seo_app.route('/dropdown-menu/',methods=['GET'])
def dropdown_menu():
    return render_template('track/season/season-dropdown-menu.html')

