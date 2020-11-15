# The Experience of Fast with FastAPI

This repository held any material resource for my presentation in indonesia python conference 2020

<p align="center">
	<img src="https://pbs.twimg.com/media/EmSWlJhU0AEnUls?format=png&name=900x900" width=350/>
</p>

Presentation File : [The Experience of Fast with FastAPI](https://docs.google.com/presentation/d/1V_pZzTRFe94ZccFszXTrBvS8oooRBYbebsMVtdkS33U/edit?usp=sharing)

Reposity tree file :
```
├── src
|   ├── app
|   |   ├── main.py
|   |   ├── routes
|   |   |   ├── piggybank.py
|   |   |   └── root.py
|   |   └── flaskApp
|   |       └── flask_app.py
|   └── exercise
|       ├── helloWorld.py
|       ├── typing-validation.py
|       ├── async.py
|       ├── ws.py
|       ├── measurements.json
|       └── templates
|           └── index.htm
├── payload
|   └── PiggyBank.txt
├── Dockerfile
├── Pipfile
└── Pipfile.lock
```

## Requirements to install

- pipenv (if you already have `pip` just install pipenv with `pip install pipenv`)
- docker ( to build )

## How to Run

1. go to the `src/exercise` if you want to run every single code I preset and run this command
(don't use `pipenv run` if you already install the uvicorn and fastapi)
```
pipenv run uvicorn typing-validation:app
```

2. if you want to run a whole code I preset, you can go to `src/app` and run this command
```
pipenv run uvicorn main:app
```


