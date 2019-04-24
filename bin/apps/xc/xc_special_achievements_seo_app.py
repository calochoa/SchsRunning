__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template, redirect


xc_special_achievements_seo_app = Blueprint(
    'xc_special_achievements_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-cross-country/special-achievements'
)    


@xc_special_achievements_seo_app.route('/special-achievements-dropdown-menus',methods=['GET'])
def xc_special_achievements_dropdown_menus():
    return render_template('xc/special-achievements/special-achievements-dropdown-menus.html')


@xc_special_achievements_seo_app.route('/',methods=['GET'])
def xc_special_achievements_home():
    return render_template('xc/special-achievements/special-achievements.html')

@xc_special_achievements_seo_app.route('/all',methods=['GET'])
def xcAllSpecialAchievements():
    return render_template('xc/special-achievements/specialAchievement.html', splAchvId=0, sportId=1)

@xc_special_achievements_seo_app.route('/league-champions',methods=['GET'])
def xcLeagueChampions():
    return render_template('xc/special-achievements/specialAchievement.html', splAchvId=1, sportId=1)

@xc_special_achievements_seo_app.route('/section-champions',methods=['GET'])
def xcSectionChampions():
    return render_template('xc/special-achievements/specialAchievement.html', splAchvId=2, sportId=1)

@xc_special_achievements_seo_app.route('/state-qualifiers',methods=['GET'])
def xcStateQualifiers():
    return render_template('xc/special-achievements/specialAchievement.html', splAchvId=3, sportId=1)

@xc_special_achievements_seo_app.route('/past-crystal-springs-alumni-race-champions',methods=['GET'])
def xcPastCsAlumniRaceChampions():
    return render_template('xc/special-achievements/pastXcAlumniChampions.html')

