# Real estate Agency website

The site is under development, so only a page with a list of apartments and an admin panel for filling the database is available.

## Launch

- Download the code
- Install dependencies with the command `pip install -r requirements.txt`
- Create a database file and immediately apply all migrations with the command `python3 manage.py migrate`
- Start the server with the command `python3 manage.py runserver`

## Environment variables

Some of the project settings are taken from the environment variables. To identify them, create a file `.env` near to the `manage.py` and write the data there in this format: `VARIABLE=value`.

3 variables are available:
- `DEBUG` — debag mode. Set _**True**_ to see debugging information in case of an error.
- `SECRET_KEY` — the secret key of the project
- `ALLOWED_HOSTS` — [Django documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE` — a single-line address to the database, for example: `sqlite:///db.sqlite3`. More information in [documentation](https://github.com/jacobian/dj-database-url).

    This makes it easy to switch between databases: PostgreSQL, MySQL, SQLite — no difference, you just need to substitute the desired address.

## Project goal

The code is written for educational purposes — this is a lesson in a course on Python and web development on the site [Devman](https://dvmn.org).
