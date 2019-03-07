__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


xc_videos_seo_app = Blueprint(
    'xc_videos_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-cross-country/videos'
)    


@xc_videos_seo_app.route('/crystal-springs-alumni-race/',methods=['GET'])
def getXcCrystalSpringsAlumniRace():
    return render_template('xc/videos/videosCsAlumniRace.html')

