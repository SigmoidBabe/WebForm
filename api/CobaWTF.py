from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = '15c1b7efdf870d0315df78598f99ca31e83e33776af579bb'


class CourseForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=10, max=100)])
    description = TextAreaField('Course Description',
                                validators=[InputRequired(),
                                            Length(max=200)])
    price = IntegerField('Price', validators=[InputRequired()])
    level = RadioField('Level',
                       choices=['Beginner', 'Intermediate', 'Advanced'],
                       validators=[InputRequired()])
    available = BooleanField('Available', default='checked')

courses_list = [{
    'title': 'Python 101',
    'description': 'Learn Python basics',
    'price': 34,
    'available': True,
    'level': 'Beginner'
    }]


@app.route('/', methods=('GET', 'POST'))
def page_isi_form():
    form = CourseForm()
    if form.validate_on_submit():
        courses_list.append({'title': form.title.data,
                             'description': form.description.data,
                             'price': form.price.data,
                             'available': form.available.data,
                             'level': form.level.data
                             })
        return redirect(url_for('courses'))
    return render_template('CobaWTF_Form.html', form=form)

@app.route('/courses')
def courses():
    return render_template('List_Course.html', courses_list=courses_list)


