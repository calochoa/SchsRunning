__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template


track_and_field_app = Blueprint('track_and_field_app', __name__, template_folder='templates')


@track_and_field_app.route('/santa-clara-high-track-and-field')
@track_and_field_app.route('/track')
def main_track():
    return render_template('track/index.html')


@track_and_field_app.route('/topTrackRaceResults')
def topTrackRaceResults():
    return render_template('track/topRaceResults.html', eId = 0, gId = 0, limit = 0)

