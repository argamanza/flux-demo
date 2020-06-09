FROM python:2.7-alpine

LABEL maintainer="tzahi.argaman@develeap.com"
COPY . /app
WORKDIR /app
RUN apk add --no-cache python2
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
