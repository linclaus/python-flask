FROM python:3.6-slim
ENV LANG=en_US.UTF-8

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt && \
	rm -rf /tmp/*

COPY . /app

EXPOSE 8080

CMD python manager.py runserver > /var/log/app.log 2>&1

