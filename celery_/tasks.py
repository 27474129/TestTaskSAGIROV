from celery_.celery_ import app


@app.task()
def send_hello():
    print("asdasdasadsasdasd")


