from celery import Celery

app = Celery("task")
app.config_from_object("celeryconfig")
app.conf.imports = "newapp2.tasks"
app.autodiscover_tasks()
