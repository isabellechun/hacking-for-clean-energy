# hacking-for-clean-energy

## Run the django app
```
django-admin startproject verdigris
python manage.py startapp eli

python manage.py runserver 0.0.0.0:8080

# Ping the server
curl -X GET localhost:8080/ping

# Post the input data to trigger a job
curl -X POST localhost:8080/eli -v
```

## Notes
Rate limit: 30 queries/sec