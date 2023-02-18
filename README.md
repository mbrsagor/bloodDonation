## FastAPI Blog App
> The project is basically fast api basic core concept to develop microservice based backend web application.

The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed the apps on Windows, you should have little problem getting up and running.

#### Setup:
- python3.10
- Fast API

###### Instructions:

```bash
git clone https://github.com/mbrsagor/fastapiApp.git
cd fastapiApp
virtualenv sagor --python=python3.10
pip install -r requirements.txt
```

#### Simple example of fast API
```python

@app.get('/details/{pk}')
async def details_api(pk: str):
    return {"data": {"Hello": pk}}
```
