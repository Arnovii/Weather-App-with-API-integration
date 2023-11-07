from flask import render_template, request, redirect, url_for


def index():
    return redirect(url_for('login'))

def login():
    if request.method == 'POST':
        print(request.form['usernameLogin'])
        print(request.form['passwordLogin'])
        return "<h1>POST</h1>"
    else: # GET
        return render_template('auth/login.html')
    

