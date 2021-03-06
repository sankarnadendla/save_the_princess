import bottle
from bottle import request
import json, sqlite3
from google.oauth2 import id_token
from google.auth.transport import requests
from beaker.middleware import SessionMiddleware

CLIENT_ID = "237964107198-0q4lgvs8d4nto9ds060779kj03rod9fb.apps.googleusercontent.com"

def validateGoogle():
    dict_data = request.json
    try:
        idinfo = id_token.verify_oauth2_token(dict_data['ID'], requests.Request(), CLIENT_ID)
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
        userid = idinfo['sub']
        #print(idinfo)
        manageUserInfo(str(idinfo['email']))
        return True
    except ValueError:
        return False

def validateFacebook():
    try:
        dict_data = request.json
        #print(str(dict_data['authResponse']['userID']))
        manageUserInfo(str(dict_data['authResponse']['userID']))
        return True
    except ValueError:
        return False

def manageUserInfo(Email):
    level = 'Level1'
    conn = sqlite3.connect('./Database/princess.db')
    c = conn.cursor()
    c.execute("select EmailAddress from User where EmailAddress=?", (Email,))
    result = c.fetchall()
    if(len(result) > 0):
        c.execute("select UserID, EmailAddress, CurrentGameLevel from User where EmailAddress=?", (Email,))
        result = c.fetchall()
        session = bottle.request.environ.get('beaker.session')
        for row in result:
            session['game_user'] = row[1]
        session.save()
    else:
        c.execute("insert into User (EmailAddress,CurrentGameLevel) values (?,?)", (Email, level))
        new_id = c.lastrowid
        conn.commit()
        session = bottle.request.environ.get('beaker.session')
        session['game_user'] = Email
        session.save()
    c.close()