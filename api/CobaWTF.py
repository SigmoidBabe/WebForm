from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/')
def page_isi_form():
    return "BERHASIL UYY"

