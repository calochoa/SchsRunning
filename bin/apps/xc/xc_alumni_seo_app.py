__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


xc_alumni_seo_app = Blueprint(
    'xc_alumni_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-cross-country/crystal-springs-alumni-race'
)    


@xc_alumni_seo_app.route('/',methods=['GET'])
def xc_crystal_springs_alumni_race_home():
    return render_template('xc/alumni/crystal-springs-alumni-race.html')
