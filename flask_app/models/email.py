from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
    # create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# model the class after the user table from our database
class Email:
    def __init__(self, data):
        self.id = data['id']
        self.address = data['address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def submit_email(cls,data):
        query = "INSERT INTO emails (address, created_at, updated_at) VALUES (%(address)s, NOW(), NOW());"
        return connectToMySQL('email_schema').query_db(query,data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_schema').query_db(query)
        #empty list to add instances to
        emails = []
        #iterate results and create instances of emails with the clsmethod
        for email in results:
            emails.append(cls(email))
        return emails


    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['address']): #okay they had 'email' in the original which makes most sense
            flash("Invalid email address!")
            is_valid = False
        return is_valid