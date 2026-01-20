from celery import shared_task


@shared_task
def sharedtask1():
    return


@shared_task
def sharedtask2():
    return
