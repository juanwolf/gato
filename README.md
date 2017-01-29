# gato

Gato in spanish means cat in english which means chat in french. So yeah
it is the thousands chat applications that you could find in the web.

## How to run it

For the moment, it is quite simple.

### Install the requirements

`pip install -r requirements.txt`

### Use runserver

```
cd gato;
python manage.py runserver
```

## Project organization

```
.
├── gato # The sources of the django project
│   ├── chat  # The source of the chat backend
│   │   ├── apps.py
│   │   ├── consumers.py
│   │   ├── models.py
│   │   ├── routing.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── gato  # Configuration of the project
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
├── README.md
└── requirements.txt
```

For the moment it can be quite confusing, I let the default project structure
made by `django-admin startproject`, in the next commits I will try to change
directories name to be more "intuitive".

## License

This project is licensed under the terms of the MIT license.
