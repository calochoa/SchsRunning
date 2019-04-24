__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Blueprint, render_template


xc_course_results_seo_app = Blueprint(
    'xc_course_results_seo_app', __name__, template_folder='templates', url_prefix='/santa-clara-high-cross-country/course-results'
)    


@xc_course_results_seo_app.route('/top-individual-dropdown-menus',methods=['GET'])
def xc_top_individual_dropdown_menus():
    return render_template('xc/course-results/top-individual-dropdown-menus.html')

@xc_course_results_seo_app.route('/top-team-dropdown-menus',methods=['GET'])
def xc_top_team_dropdown_menus():
    return render_template('xc/course-results/top-team-dropdown-menus.html')


@xc_course_results_seo_app.route('/top-team')
def top_team_home():
    return render_template('xc/course-results/top-team.html')

@xc_course_results_seo_app.route('/top-individual')
def top_individual_home():
    return render_template('xc/course-results/top-individual.html')

@xc_course_results_seo_app.route('/top-25-all-time-boys-crystal-springs')
def top25BoysCrystalSprings():
    return render_template('xc/course-results/topCourseResults.html', cId=1, gId=2, limit=25, grade=0)

@xc_course_results_seo_app.route('/top-25-senior-boys-crystal-springs')
def top25SeniorBoysCrystalSprings():
    return render_template('xc/course-results/topCourseResults.html', cId=1, gId=2, limit=25, grade=12)

@xc_course_results_seo_app.route('/top-25-junior-boys-crystal-springs')
def top25JuniorBoysCrystalSprings():
    return render_template('xc/course-results/topCourseResults.html', cId=1, gId=2, limit=25, grade=11)

@xc_course_results_seo_app.route('/top-25-sophomore-boys-crystal-springs')
def top25SophomoreBoysCrystalSprings():
    return render_template('xc/course-results/topCourseResults.html', cId=1, gId=2, limit=25, grade=10)

@xc_course_results_seo_app.route('/top-25-freshman-boys-crystal-springs')
def top25FreshmanBoysCrystalSprings():
    return render_template('xc/course-results/topCourseResults.html', cId=1, gId=2, limit=25, grade=9)

@xc_course_results_seo_app.route('/top-25-all-time-girls-crystal-springs')
def top25GirlsCrystalSprings():
    return render_template('xc/course-results/topCourseResults.html', cId=1, gId=3, limit=25, grade=0)

@xc_course_results_seo_app.route('/top-25-senior-girls-crystal-springs')
def top25SeniorGirlsCrystalSprings():
    return render_template('xc/course-results/topCourseResults.html', cId=1, gId=3, limit=25, grade=12)

@xc_course_results_seo_app.route('/top-25-junior-girls-crystal-springs')
def top25JuniorGirlsCrystalSprings():
    return render_template('xc/course-results/topCourseResults.html', cId=1, gId=3, limit=25, grade=11)

@xc_course_results_seo_app.route('/top-25-sophomore-girls-crystal-springs')
def top25SophomoreGirlsCrystalSprings():
    return render_template('xc/course-results/topCourseResults.html', cId=1, gId=3, limit=25, grade=10)

@xc_course_results_seo_app.route('/top-25-freshman-girls-crystal-springs')
def top25FreshmanGirlsCrystalSprings():
    return render_template('xc/course-results/topCourseResults.html', cId=1, gId=3, limit=25, grade=9)



@xc_course_results_seo_app.route('/top-25-all-time-boys-toro-park')
def top25BoysToroPark():
    return render_template('xc/course-results/topCourseResults.html', cId=2, gId=2, limit=25, grade=0)

@xc_course_results_seo_app.route('/top-25-senior-boys-toro-park')
def top25SeniorBoysToroPark():
    return render_template('xc/course-results/topCourseResults.html', cId=2, gId=2, limit=25, grade=12)

@xc_course_results_seo_app.route('/top-25-junior-boys-toro-park')
def top25JuniorBoysToroPark():
    return render_template('xc/course-results/topCourseResults.html', cId=2, gId=2, limit=25, grade=11)

@xc_course_results_seo_app.route('/top-25-sophomore-boys-toro-park')
def top25SophomoreBoysToroPark():
    return render_template('xc/course-results/topCourseResults.html', cId=2, gId=2, limit=25, grade=10)

@xc_course_results_seo_app.route('/top-25-freshman-boys-toro-park')
def top25FreshmanBoysToroPark():
    return render_template('xc/course-results/topCourseResults.html', cId=2, gId=2, limit=25, grade=9)

@xc_course_results_seo_app.route('/top-25-all-time-girls-toro-park')
def top25GirlsToroPark():
    return render_template('xc/course-results/topCourseResults.html', cId=2, gId=3, limit=25, grade=0)

@xc_course_results_seo_app.route('/top-25-senior-girls-toro-park')
def top25SeniorGirlsToroPark():
    return render_template('xc/course-results/topCourseResults.html', cId=2, gId=3, limit=25, grade=12)

@xc_course_results_seo_app.route('/top-25-junior-girls-toro-park')
def top25JuniorGirlsToroPark():
    return render_template('xc/course-results/topCourseResults.html', cId=2, gId=3, limit=25, grade=11)

@xc_course_results_seo_app.route('/top-25-sophomore-girls-toro-park')
def top25SophomoreGirlsToroPark():
    return render_template('xc/course-results/topCourseResults.html', cId=2, gId=3, limit=25, grade=10)

@xc_course_results_seo_app.route('/top-25-freshman-girls-toro-park')
def top25FreshmanGirlsToroPark():
    return render_template('xc/course-results/topCourseResults.html', cId=2, gId=3, limit=25, grade=9)



@xc_course_results_seo_app.route('/top-25-all-time-boys-central-park')
def top25BoysCentralPark():
    return render_template('xc/course-results/topCourseResults.html', cId=6, gId=2, limit=25, grade=0)

@xc_course_results_seo_app.route('/top-25-senior-boys-central-park')
def top25SeniorBoysCentralPark():
    return render_template('xc/course-results/topCourseResults.html', cId=6, gId=2, limit=25, grade=12)

@xc_course_results_seo_app.route('/top-25-junior-boys-central-park')
def top25JuniorBoysCentralPark():
    return render_template('xc/course-results/topCourseResults.html', cId=6, gId=2, limit=25, grade=11)

@xc_course_results_seo_app.route('/top-25-sophomore-boys-central-park')
def top25SophomoreBoysCentralPark():
    return render_template('xc/course-results/topCourseResults.html', cId=6, gId=2, limit=25, grade=10)

@xc_course_results_seo_app.route('/top-25-freshman-boys-central-park')
def top25FreshmanBoysCentralPark():
    return render_template('xc/course-results/topCourseResults.html', cId=6, gId=2, limit=25, grade=9)

@xc_course_results_seo_app.route('/top-25-all-time-girls-central-park')
def top25GirlsCentralPark():
    return render_template('xc/course-results/topCourseResults.html', cId=6, gId=3, limit=25, grade=0)

@xc_course_results_seo_app.route('/top-25-senior-girls-central-park')
def top25SeniorGirlsCentralPark():
    return render_template('xc/course-results/topCourseResults.html', cId=6, gId=3, limit=25, grade=12)

@xc_course_results_seo_app.route('/top-25-junior-girls-central-park')
def top25JuniorGirlsCentralPark():
    return render_template('xc/course-results/topCourseResults.html', cId=6, gId=3, limit=25, grade=11)

@xc_course_results_seo_app.route('/top-25-sophomore-girls-central-park')
def top25SophomoreGirlsCentralPark():
    return render_template('xc/course-results/topCourseResults.html', cId=6, gId=3, limit=25, grade=10)

@xc_course_results_seo_app.route('/top-25-freshman-girls-central-park')
def top25FreshmanGirlsCentralPark():
    return render_template('xc/course-results/topCourseResults.html', cId=6, gId=3, limit=25, grade=9)



@xc_course_results_seo_app.route('/top-25-all-time-boys-baylands-park')
def top25BoysBaylandsPark():
    return render_template('xc/course-results/topCourseResults.html', cId=4, gId=2, limit=25, grade=0)

@xc_course_results_seo_app.route('/top-25-senior-boys-baylands-park')
def top25SeniorBoysBaylandsPark():
    return render_template('xc/course-results/topCourseResults.html', cId=4, gId=2, limit=25, grade=12)

@xc_course_results_seo_app.route('/top-25-junior-boys-baylands-park')
def top25JuniorBoysBaylandsPark():
    return render_template('xc/course-results/topCourseResults.html', cId=4, gId=2, limit=25, grade=11)

@xc_course_results_seo_app.route('/top-25-sophomore-boys-baylands-park')
def top25SophomoreBoysBaylandsPark():
    return render_template('xc/course-results/topCourseResults.html', cId=4, gId=2, limit=25, grade=10)

@xc_course_results_seo_app.route('/top-25-freshman-boys-baylands-park')
def top25FreshmanBoysBaylandsPark():
    return render_template('xc/course-results/topCourseResults.html', cId=4, gId=2, limit=25, grade=9)

@xc_course_results_seo_app.route('/top-25-all-time-girls-baylands-park')
def top25GirlsBaylandsPark():
    return render_template('xc/course-results/topCourseResults.html', cId=4, gId=3, limit=25, grade=0)

@xc_course_results_seo_app.route('/top-25-senior-girls-baylands-park')
def top25SeniorGirlsBaylandsPark():
    return render_template('xc/course-results/topCourseResults.html', cId=4, gId=3, limit=25, grade=12)

@xc_course_results_seo_app.route('/top-25-junior-girls-baylands-park')
def top25JuniorGirlsBaylandsPark():
    return render_template('xc/course-results/topCourseResults.html', cId=4, gId=3, limit=25, grade=11)

@xc_course_results_seo_app.route('/top-25-sophomore-girls-baylands-park')
def top25SophomoreGirlsBaylandsPark():
    return render_template('xc/course-results/topCourseResults.html', cId=4, gId=3, limit=25, grade=10)

@xc_course_results_seo_app.route('/top-25-freshman-girls-baylands-park')
def top25FreshmanGirlsBaylandsPark():
    return render_template('xc/course-results/topCourseResults.html', cId=4, gId=3, limit=25, grade=9)



@xc_course_results_seo_app.route('/top-25-all-time-boys-lynbrook-high-school')
def top25BoysLynbrookHighSchool():
    return render_template('xc/course-results/topCourseResults.html', cId=25, gId=2, limit=25, grade=0)

@xc_course_results_seo_app.route('/top-25-senior-boys-lynbrook-high-school')
def top25SeniorBoysLynbrookHighSchool():
    return render_template('xc/course-results/topCourseResults.html', cId=25, gId=2, limit=25, grade=12)

@xc_course_results_seo_app.route('/top-25-junior-boys-lynbrook-high-school')
def top25JuniorBoysLynbrookHighSchool():
    return render_template('xc/course-results/topCourseResults.html', cId=25, gId=2, limit=25, grade=11)

@xc_course_results_seo_app.route('/top-25-sophomore-boys-lynbrook-high-school')
def top25SophomoreBoysLynbrookHighSchool():
    return render_template('xc/course-results/topCourseResults.html', cId=25, gId=2, limit=25, grade=10)

@xc_course_results_seo_app.route('/top-25-freshman-boys-lynbrook-high-school')
def top25FreshmanBoysLynbrookHighSchool():
    return render_template('xc/course-results/topCourseResults.html', cId=25, gId=2, limit=25, grade=9)

@xc_course_results_seo_app.route('/top-25-all-time-girls-lynbrook-high-school')
def top25GirlsLynbrookHighSchool():
    return render_template('xc/course-results/topCourseResults.html', cId=25, gId=3, limit=25, grade=0)

@xc_course_results_seo_app.route('/top-25-senior-girls-lynbrook-high-school')
def top25SeniorGirlsLynbrookHighSchool():
    return render_template('xc/course-results/topCourseResults.html', cId=25, gId=3, limit=25, grade=12)

@xc_course_results_seo_app.route('/top-25-junior-girls-lynbrook-high-school')
def top25JuniorGirlsLynbrookHighSchool():
    return render_template('xc/course-results/topCourseResults.html', cId=25, gId=3, limit=25, grade=11)

@xc_course_results_seo_app.route('/top-25-sophomore-girls-lynbrook-high-school')
def top25SophomoreGirlsLynbrookHighSchool():
    return render_template('xc/course-results/topCourseResults.html', cId=25, gId=3, limit=25, grade=10)

@xc_course_results_seo_app.route('/top-25-freshman-girls-lynbrook-high-school')
def top25FreshmanGirlsLynbrookHighSchool():
    return render_template('xc/course-results/topCourseResults.html', cId=25, gId=3, limit=25, grade=9)



@xc_course_results_seo_app.route('/top-15-all-time-team-girls-crystal-springs')
def top15TeamGirlsCrystalSprings():
    return render_template('xc/course-results/teamCourseResults.html', cId=1, gId=3, limit=15)

@xc_course_results_seo_app.route('/top-15-all-time-team-boys-crystal-springs')
def top15TeamBoysCrystalSprings():
    return render_template('xc/course-results/teamCourseResults.html', cId=1, gId=2, limit=15)

@xc_course_results_seo_app.route('/top-15-all-time-team-girls-toro-park')
def top15TeamGirlsToroPark():
    return render_template('xc/course-results/teamCourseResults.html', cId=2, gId=3, limit=15)

@xc_course_results_seo_app.route('/top-15-all-time-team-boys-toro-park')
def top15TeamBoysToroPark():
    return render_template('xc/course-results/teamCourseResults.html', cId=2, gId=2, limit=15)

@xc_course_results_seo_app.route('/top-15-all-time-team-girls-central-park')
def top15TeamGirlsCentralPark():
    return render_template('xc/course-results/teamCourseResults.html', cId=6, gId=3, limit=15)

@xc_course_results_seo_app.route('/top-15-all-time-team-boys-central-park')
def top15TeamBoysCentralPark():
    return render_template('xc/course-results/teamCourseResults.html', cId=6, gId=2, limit=15)

@xc_course_results_seo_app.route('/top-15-all-time-team-girls-baylands-park')
def top15TeamGirlsBaylandsPark():
    return render_template('xc/course-results/teamCourseResults.html', cId=4, gId=3, limit=15)

@xc_course_results_seo_app.route('/top-15-all-time-team-boys-baylands-park')
def top15TeamBoysBaylandsPark():
    return render_template('xc/course-results/teamCourseResults.html', cId=4, gId=2, limit=15)

