import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://root@127.0.0.1:3309/CTI_db_test'
TAXII_ROOT = 'http://127.0.0.1/taxii'
ATTACHMENTS_PATH_IN = '/var/tmp/files_in'
"""Files received by the service are saved under this path"""


DEBUG = True
SECRET_KEY = 'random string from CSRF'


# administrator list
ADMINS = ['list@mails.com']

# content bindings
CB_EVENTS_JSON_10 = 'urn:events.cert.europa.eu:json:1.0'