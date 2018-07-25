# Component name
Generates SQL scripts for warnings

## How it works
Fire up the component, fill in the boxes and install 

## Setup
To install, run the following command:
```bash
pip install virtualenv
virtualenv .env
source .env/Scripts/activate
pip install -r requirements.txt
```

### Intellij setup
Project uses python 3
Having followed the setup steps above, set the SDK for your project to be ```.env/Scripts/python.exe```

## Test
No tests currently

## Output data
The service is expected to return the following data:
```JSON
fakewarnings.sql
```