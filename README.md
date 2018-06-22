# newtown-website
The source code of Newtown Trade's website.

## Setup
Please note that this project was designed with **Python 3**. Python 2 may work, but it has not been tested.
Before forking this repo, please make sure you have a working instance of Python 3, pip, and an Algolia app.

1. `git clone` the repo

2. `pip install virtualenv` for a virtual environment.

3. `cd` into the repo, and `pip install -r requirements.txt` to get all dependencies. (includes touhou)

4. Run `python manage.py migrate` to generate database tables.

5. In your `~/.bashrc` have the following environment variables:

* `DEV="true"`
* `ALGOLIAAPI` set to your Algolia App's API
* `ALGOLIAAPP` set to your Algolia APP's app ID

6. Run `python manage.py runserver` to start the test server. Note that as of `v0.6`, fixtures have not been immplemented. As such, you'll need to manually add test data to ensure all parts of site load properly. 

7. After you have test data that sastisfies you, run `python manage.py algolia_applysettings` and `python manage.py algolia_reindex` to sync your Algolia app with Django's databases.

If anything goes wrong, please flag it in Issues.
