FROM python:3.8

RUN pip3 install pipenv

ENV PROJECT_DIR /user/src/flaskbookapi

WORKDIR ${PROJECT_DIR}

COPY Pipfile .
COPY Pipfile.lock .
COPY . .

RUN pipenv install --deploy --ignore-pipfile
RUN pipenv install neo4j

EXPOSE 5000

CMD ["pipenv", "run", "python", "api.py"]