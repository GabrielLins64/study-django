<h2> Study on Django </h2>

Repository for study on Django and Django REST Framework

---

<h3>Index</h3>

- [Django main commands](#django-main-commands)
  - [Creating a project](#creating-a-project)
  - [Running the development server](#running-the-development-server)
  - [Create an app](#create-an-app)
  - [Create migrations](#create-migrations)
  - [Applying the migrations](#applying-the-migrations)
  - [Django shell](#django-shell)
  - [Creating a superuser for Admin](#creating-a-superuser-for-admin)
  - [Executing tests](#executing-tests)
- [Checkpoints](#checkpoints)
  - [Django](#django)
  - [Django REST Framework](#django-rest-framework)
- [References](#references)

---

## Django main commands

### Creating a project

After installing Django, type:

```shell
$ django-admin startproject <project_name>
```

### Running the development server

```shell
$ python manage.py runserver <(optional)host:port>
```

### Create an app

```shell
$ python manage.py startapp <app_name>
```

### Create migrations

After defining your models, execute:

```shell
$ python manage.py makemigrations <app_name>
```

### Applying the migrations

```shell
$ python manage.py migrate
```

### Django shell

```shell
$ python manage.py shell
```

### Creating a superuser for Admin

```shell
$ python manage.py createsuperuser
```

### Executing tests

```shell
$ python manage.py test <app_name>
```

---

## Checkpoints

### Django

https://docs.djangoproject.com/en/4.1/intro/reusable-apps/

### Django REST Framework

https://www.django-rest-framework.org/tutorial/1-serialization/

## References

[1] https://www.djangoproject.com/

[2] https://www.django-rest-framework.org/
