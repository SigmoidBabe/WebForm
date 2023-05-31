from flask import Flask, render_template, request, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length


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

class MedicalForm(FlaskForm):
    Nama = StringField('Nama', validators=[InputRequired(),
                                             Length(min=5, max=30)])
    Jenis_Kelamin = StringField('Jenis Kelamin', validators=[InputRequired()])
    Usia = IntegerField('Usia', validators=[InputRequired()])
    RestECG = IntegerField('RestECG', validators=[InputRequired()])
    Slope = IntegerField('Slope', validators=[InputRequired()])
    Chol = IntegerField('Chol', validators=[InputRequired()])
    Thalach = IntegerField('Thalach', validators=[InputRequired()])

