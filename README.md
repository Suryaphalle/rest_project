# rest_project sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Suryaphalle/rest_project.git
$ cd rest_project
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```

## To get continues reading of devices we need to run bacjground-tasks
Open new terminal and activate same virtual environment from project directory to run following command: 
```sh
(env)$ python manage.py process_tasks
```
## To login and get JWT token 
And navigate to `http://127.0.0.1:8000/rest-auth/login/`.


## Credntials.
I have used sqlite3 database
Username: admin
Password: admin
email: admin@admin.com

## endpoints
To get list and create device
`http://127.0.0.1:8000/devices/`

To edit device
`http://127.0.0.1:8000/devices/<int:pk>/`

To send_update to particuler device of perticular sensor
`http://127.0.0.1:8000/send_update/`

To get data of particuler device of perticular sensor
`http://127.0.0.1:8000/get_data/`
