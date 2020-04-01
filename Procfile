release: --pythonpath telega_weather_bot_page python manage.py migrate
web: gunicorn --pythonpath telega_weather_bot_page telega_weather_bot_page.wsgi --log-file -
