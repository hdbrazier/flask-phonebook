#22
from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

#23
@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')