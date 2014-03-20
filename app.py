from bottle import get, response, run
import requests

from os import environ

@get('/event-attendance')
def get_event_attendance(event_id='331218348435'):
  foauth_user = environ.get('FOAUTH_USER')
  foauth_password = environ.get('FOAUTH_PASS')

  r = requests.get('https://foauth.org/graph.facebook.com/%s/attending' % event_id, 
      auth=requests.auth.HTTPBasicAuth(foauth_user, foauth_password))

  if r.status_code == 200:
    event_attendees = r.json().get('data', [])
    print len(event_attendees)
    return {'number_of_event_attendees': len(event_attendees), 'event_id': event_id}

run(host='0.0.0.0', port=environ.get('PORT', 8081), reloader=True)
