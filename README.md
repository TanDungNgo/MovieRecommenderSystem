# Movie Recommendation System

## How to run

<br />

> Step 1: Clone the repository
```shell
$ git clone https://github.com/TanDungNgo/MovieRecommenderSystem.git
```

> Step 2: Change directory
```shell
$ cd MovieRecommenderSystem
```
> Step 3: Create and activate virtual environment
```shell
# Create
$ python -m venv env 
# Activate
$ source env/bin/activate
```
>Step 4: Install the dependencies
```shell
$ pip install -r requirements.txt
```
> Step 5: Migrate the database
```shell
$ python manage.py migrate
```
> Step 6: Run the server
```shell
$ python manage.py runserver
```

The server will run http://127.0.0.1:8000/