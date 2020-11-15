FROM python:3.8-alpine

RUN pip install pipenv uvicorn 

WORKDIR /app
COPY src/app .

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

EXPOSE 8000
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--log-level", "trace", "main:app"]
