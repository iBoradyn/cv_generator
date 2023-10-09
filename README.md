# CV generator
Application designed to create a resume for a programmer in Polish and English


## Required services
- PostrgeSQL
- Gunicorn/runserver
- Redis
- Celery


## Local project configuration
- Create postgresql database
- Create .env file based on .env.example
- `pip install -r requirements.txt` or `pip install -r requirements-dev.txt` for local development
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py collectstatic --noinput`
- Start redis on default port `6379`
  - `redis-server`
- Start gunicorn or runserver on default port `8000`
  - `gunicorn --workers 3 project.wsgi:application`
  - `python manage.py runserver`
- Start celery worker
  - `celery -A project worker -l DEBUG`


## SASS File Watcher config (PyCharm)
Most scss files are imported to `base.scss` which is compiled into `base.css` in css directory.
If the file is not imported into `base.scss`, it will be compiled as a separate file with the same name in the css directory. 
> NOTE: The files are created directly in the `css` directory even if the source files are in a subdirectory.

1. File > Settings > Tools > File Watchers > Add('+') > SCSS
2. Scope: '...' > Add scope('+') > Local
   - Select scss directory and click 'Include Recursively'
   - Click 'Apply' and 'OK'
3. Program: Path to sass
4. Arguments: ```--no-cache --update $FileName$:$ProjectFileDir$/static/css/$FileNameWithoutExtension$.min.css --style compressed```
5. Output paths to refresh: ```../css/$FileNameWithoutExtension$.min.css:../css/$FileNameWithoutExtension$.min.css.map```
6. OK > Apply > OK


## Project structure
```
raspberry_mini_smart_home
│   .env
│   requirements.txt
│   requirements-dev.txt
│   .gitignore
│   README.md
├───apps
│   ├───accounts
│   ├───core
│   └───cv_generator
├───locale
│   └───pl
├───project
│   │   asgi.py
│   │   celery_config.py
│   │   settings.py
│   │   urls.py
│   └   wsgi.py
├───static
│   ├───css
│   ├───js
│   └───scss
└───templates
    │ base.html
    ├───core
    ├───accounts
    ├───cv_generator
    └───_partials
```