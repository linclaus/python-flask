# -*- encoding: utf-8 -*-
from celery import Celery, Task
import time

app = Celery('tasks', broker='redis://localhost:6379/0')  # 配置好celery的backend和broker


class MyTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('task done: {0}'.format(retval))
        return super(MyTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task fail, reason: {0}'.format(exc))
        return super(MyTask, self).on_failure(exc, task_id, args, kwargs, einfo)


@app.task(base=MyTask)  # 普通函数装饰为 celery task
def add(x, y):
    print((x, y))
    time.sleep(5)
    return x + y


@app.task(bind=True)
def test(self):
    print(self.request.__dict__)
