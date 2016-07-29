### Example setup of Multi-site wagtail

This repo contains an example implementation of Wagtail, demonstrating its multi-site capabilities.

####Setup

* Setup virtual environment of choice
* `git clone https://github.com/chrxr/multi-site-wagtail.git`
* `cd multi-site-wagtail`
* `pip install -r requirements.txt`

This implementation is equipped with a SQLite database with a superuser already created, so you should just be able to start it up.

* `./manage.py runserver`
* Navigate to http://localhost:8000/admin
* Login with username: admin, password: admin
* Admin users for each of the 3 individual site have also been set up with username: site-n-admin (e.g. site-1-admin), password: admin

This example implementation includes 3 sites. You can see these at the subdomains:

* http://localhost:8000
* http://site2.localhost:8000
* http://site3.localhost:8000

To do:

* [x] Build templates
* [x] Footer, social media and branding settings
* [x] Implement settings in templates
* [x] Create sites
* [x] Create groups and users with limited permissions
* [ ] Custom templates for specific sites
* [ ] Site specific search
