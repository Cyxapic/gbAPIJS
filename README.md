# API for GeekBrains JavaScript course

- django
- django rest framework

Start ```pip install -r requirments.txt```

Development needs file in settings -> development.py:
```
    import os

    from .base import BASE_DIR


    DEBUG = True

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
