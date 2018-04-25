Minicom (Django)
================

Welcome to Minicom! A prototype Intercom service. Inside this directory you'll find a Django project along with a test application that works with it.

## Dependencies
You need [Python 2.7](https://www.python.org/download/releases/2.7/) to start Minicom (Django) on your machine.
If Python is already installed on your machine, you can check than you have the correct version with this command:

```
$ python --version
Python 2.7.11
```

## Installation
The following commands install and use virtualenv (http://www.virtualenv.org/) to avoid installing our dependencies system-wide.

```
pip install virtualenv
cd minicom-django
virtualenv .
source ./bin/activate # or .\Scripts\activate on Windows
pip install -r requirements.txt
./manage.py syncdb
./manage.py runserver
```

This will get you a webserver running at http://127.0.0.1:8000/admin -- this is the admin interface for your test application. Let's get that started now.

Open another terminal window in this directory and run:
```
./testapp
```

It'll run another web server on port 8008. You can view the test app at http://127.0.0.1:8008/


## Sending a message
Open the [test application](http://127.0.0.1:8008) and enter the email address ```alice@example.com``` in the top-right, then click the **Sign in** button.

Nothing happens, don't worry.

Now open the [admin interface](http://127.0.0.1:8000/admin) and you should see your user has been created.

Click on ```alice@example.com``` in the admin interface and send a message. Refresh the test application and that message should appear. Check the admin interface and notice Alice's unread message count has gone back to 0.


## Structure
A quick overview of the application structure:

* **minicom/static/minicom.js** -- This is the embedded Javascript the test application uses to integrate with Minicom.
* **minicom/api.py** -- Everything under ```/api``` is here, used by the admin interface and the embedded Javascript.
* **minicom/admin.py** -- The ```/admin``` interface.
* **testapp-www/** -- The root of the test application website.


## Prototype!
This is a prototype implementation. Quick n' dirty. There's a bunch of stuff you really shouldn't do in a real application here.

Now's a good time to create a ```todo.txt``` and make a note of anything you'd like to fix or think we could improve. We might not ask you to implement any of these but we'd love to talk about them later.


## The Mission
Right now communication is one-way, from site admins to their users. Let's get a conversation going! Allow users to reply to messages from site admins.

Extend models, add new ones, throwaway what you like, keep what you need. We're prototyping here so show some hustle and see what you can accomplish!
