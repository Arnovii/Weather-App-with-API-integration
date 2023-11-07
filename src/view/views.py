from flask import render_template
from flask import render_template


def login():
    return render_template('auth/login.html')