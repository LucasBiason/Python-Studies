# API for Recipe Book Apps (Study Case)

Training: Django Rest and TDD 

-- Install and run:

```
docker build .
docker-compose build
docker-compose run app sh -c "python manage.py createsuperuser"
docker-compose up
```

Now you can open: http://0.0.0.0:8000/admin/
and log with super user created.


-- Others commands:
```
docker-compose run app sh -c "python manage.py test"  // Testing the app
docker-compose run app sh -c "python manage.py runserver 0.0.0.0:8000"
```

