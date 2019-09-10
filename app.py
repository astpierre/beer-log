from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from time import strftime
from data import getBrewReviews
import boto3
import uuid

app = Flask(__name__, template_folder='templates')

class BrewForm(Form):
    name = TextField('Beer:')
    btype = TextField('Type:')
    abv = TextField('ABV:')
    rating = TextField('Rating:')
    location = TextField('Location:')


def getTime():
    time = strftime("%Y-%m-%dT%H:%M")
    return time


def addReview(revObj):
    client = boto3.client('dynamodb')
    response = client.put_item(
            TableName='BrewReviews',
            Item={
                'revid': {
                    'S': str(uuid.uuid4()),
                },
                'rating': {
                    'N': revObj['rating'],
                },
                'name': {
                    'S': revObj['name'],
                },
                'type': {
                    'S': revObj['btype'],
                },
                'location': {
                    'S': revObj['location'],
                },
                'abv': {
                    'S': revObj['abv'],
                },
            },
        )


@app.route('/')
def index():
    brew_reviews = getBrewReviews()
    return render_template('home.html', brew_reviews=brew_reviews)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/add', methods=['GET', 'POST'])
def addBrew():
    form = BrewForm(request.form)
    if request.method == 'POST':
        beer_time = getTime()
        beer_name = request.form['name']
        beer_type = request.form['btype']
        beer_abv = request.form['abv']
        beer_rating = request.form['rating']
        beer_location = request.form['location']
        revObj = {
                "name": request.form['name'],
                "abv": request.form['abv'],
                "rating": request.form['rating'],
                "btype": request.form['btype'],
                "location": request.form['location'],
                }

        addReview(revObj)
        return redirect(url_for('index'))

    return render_template('add.html', form=form)


if __name__=='__main__':
    app.run(debug=False)
