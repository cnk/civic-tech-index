A React + Wagtail app based on https://www.accordbox.com/blog/react-wagtail-course/

# Getting Started

1. Install Docker (including docker-compose)
2. Clone this repository
3. Copy `.env/.dev-sample.example` to `.env/.dev-sample` and change the SQL_PASSWORD and SECRET_KEY
4. Run `docker-compose build`
5. Run `docker-compose up`. If everything starts up successfully, you
will probably want to Crtl-c to exit and then start the containers in
the background with `docker-compose up -d`; then you can view the logs
using `docker-compose logs -f`

This should give you 4 containers:

1. **cti-db** - the PostgresDatabase (with a persistant volume named
   `react_wagtail_postgres_data` for the data and available inside the
   cluster's private network on port 5432.

2. **cti-web** - the Django/Wagtail application. This will be available in
   your browser as `http://localhost:8000`. It also has a persistant
   volume for the media directory: `react_wagtail_media`. The Wagtail admin
   can be found at `http://localhost:8000/admin/` and the Django admin at
   `http://localhost:8000/django-admin/`. You will need to create a superuser
   to access either of those. Inside cti-web, run `./manage.py createsuperuser`

3. **cti-frontend** - the NodeJS container that builds the ReactApp for
   you when you change files. This will be available in your browser
   as `http://localhost:3000`. It also has a persistant volume that is
   shares with the storybook container for the node_modules:
   `react_wagtail_node_modules`

4. **cti-storybook** - the container that runs our StoryBook site -
   available in your browser as `http://localhost:6006`. This is
   probably the most interesting part - at least until I get all the
   peices working together.

