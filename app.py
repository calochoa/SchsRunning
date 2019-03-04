
__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"


from flask import Flask, render_template

from bin.apps.cross_country_app import cross_country_app
from bin.apps.cross_country_db_app import cross_country_db_app
from bin.apps.shared_db_app import shared_db_app
from bin.apps.track_and_field_app import track_and_field_app
from bin.apps.track_and_field_db_app import track_and_field_db_app
from bin.apps.workouts_app import workouts_app


app = Flask(__name__)
app.register_blueprint(cross_country_app)
app.register_blueprint(cross_country_db_app)
app.register_blueprint(shared_db_app)
app.register_blueprint(track_and_field_app)
app.register_blueprint(track_and_field_db_app)
app.register_blueprint(workouts_app)

app.config.update(
    PROPAGATE_EXCEPTIONS = True
)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/relatedSites',methods=['GET'])
def relatedSites():
    return render_template('relatedSites.html')


if __name__ == "__main__":
    app.run()
    # https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql-part-3--cms-23120

