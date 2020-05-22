# -*- encoding: utf-8 -*-  
from com.gridsum.celery_test.tasks import add, test

result = add.delay(4, 4)  # 不要直接 add(4, 4)，这里需要用 celery 提供的接口 delay 进行调用
print(result.get())
test.delay()
print('down')
