FROM python:3.7 as pipenv

RUN mkdir /pipenv
WORKDIR /pipenv
COPY Pipfile Pipfile.lock /pipenv/
RUN pip install pipenv
RUN pipenv lock --requirements > /pipenv/requirements.txt

FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY --from=pipenv /pipenv/requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code/

CMD ["/code/start.sh"]
