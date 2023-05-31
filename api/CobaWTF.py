from flask import Flask, render_template, redirect, url_for
from courseform import CourseForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


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

if __name__ == '__main__':
    app.run()