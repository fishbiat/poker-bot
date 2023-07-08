# Huriahtron 3000

Code for making a Python-based Poker bot, educational purposes only. 

## Using

### Flask

In the main directory run:

```
virtualenv env
source ./env/bin/activate
```

```
pip install -r requirements
```

and 

```
python setup.py install
```

Then run `python wsgi.py` and you should find the page in your web browser at [http://localhost:8080](http://localhost:8080).

# Docker

```
docker build . -t poker
```

```
docker run -p 8080:8080 poker
```

[http://localhost:8080](http://localhost:8080)