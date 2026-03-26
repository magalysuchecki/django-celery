python -m pip freeze > reqs.txt
chmod +x ./entrypoint.sh
http://0.0.0.0:8080/
docker-compose up -d --build
docker exec -it django /bin/sh
./manage.py shell 

from newapp.tasks import tp0, tp1, tp2, tp3
tp0.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp0.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp0.delay()
tp1.delay()
tp2.delay()
tp3.delay()

from djcelery.celery import t1, t2, t3
t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)
t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)
