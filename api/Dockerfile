FROM python:3.10-alpine

RUN pip3 install --upgrade pip

COPY /requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./ /app
WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]
