# Component name
Generates SQL scripts for warnings

## How it works
Fire up the component, fill in the boxes and install 

## Setup
Make vitual environment:
```bash
python3 -m virtualenv env
source env/Scripts/activate
```


To install, run the following command:
```bash
pip install virtualenv
virtualenv .env
source .env/Scripts/activate
pip install -r requirements.txt
```

## Run the server locally

```bash
python3 app.py
```

## Routes

This serves on http://localhost:9988

[Homepage link](http://localhost:9988/)

[Also homepage, but redirected with post link](http://localhost:9988/handle_data)

### Intellij setup
Project uses python 3
Having followed the setup steps above, set the SDK for your project to be ```.env/Scripts/python.exe```

## Test
```bash
behave
```

## Test with coverage
```bash
coverage run --source='utils,app.py' -m behave
coverage html
cd htmlcov
python3 -m http.server 8888
```

[Coverage Report](http://localhost:8888/)



## Output data
The service is expected to return the following data:
```bash
fakewarnings.sql
```