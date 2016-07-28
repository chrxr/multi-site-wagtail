### Example setup of Multi-site wagtail

This repo contains an example implementation of Wagtail, demonstrating its multi-site capabilities.

####Setup

* Setup virtual environment of choice
* Clone repo
* cd multi-site-wagtail
* pip install -r requirements.txt

This implementation is equipped with a sqlite3 database with a superuser already created, so you should just be able to start it up.

* ./manage.py runserver
* Navigate to localhost:8000/admin
* Login with username: admin, password: admin

This example implementation includes 3 sites. You can see these at the subdomains:

* site2.localhost.com
* site3.localhost.com
