FROM python:3.8

WORKDIR /backend-api
ENV PYTHONUNBUFFERED 1

COPY . /backend-api/
COPY ./requirements.txt /backend-api/requirements.txt

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 8000

COPY ./entrypoint.sh /backend-api/entrypoint.sh
COPY ./.env /backend-api/.env

RUN chmod +x /backend-api/entrypoint.sh
RUN chmod +x /backend-api/.env

CMD /backend-api/entrypoint.sh