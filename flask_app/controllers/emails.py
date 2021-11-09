from flask_app import app
from flask import render_template, redirect, request, session ,flash
from flask_app.models.email import Email

@app.route("/")
def display_form():
    return render_template("index.html")

@app.route('/post', methods = ["POST"])
def post_form():
    if not Email.validate_user(request.form):
    # we redirect to the template with the form.
        return redirect('/')
    Email.submit_email(request.form)
    return redirect('/success')

@app.route('/success')
def all_emails():
    all_emails = Email.get_all()
    return render_template("success.html", all_emails = all_emails)



    # ... do other things
    return redirect('/dashboard')
