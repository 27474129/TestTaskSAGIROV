from celery import Celery


app = Celery("celery_", broker="redis://redis:6379", include=['celery_.tasks', ...])


app.autodiscover_tasks("celery_.celery_", force=True)


