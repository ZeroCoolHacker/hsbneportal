 ### Getting Started
 First step is to grab a copy of this repository. You will need to make sure you have python installed, preferably
 3.6 or newer as that's the only version it has been tested on. Make sure you also install pip so that you can install
 all of the dependencies.
 
 To install python 3/pip and the requirements run these commands from within this folder:
 ##### Linux (Ubuntu)
 
 ```bash
 sudo apt install python3 python3-pip
 sudo -H pip3 install -r requirements.txt
 ```
 
 ##### Linux (Fedora)
```
sudo dnf install python3 python3-pip
sudo -H pip3 install -r requirements.txt
```
 
 ##### Mac (Tested by nog3 w/python 3.7)
 You will need to install and use virtualenv on Mac in order to get your environment correct as there are conflicts with built in python on OSX.
 
```bash
brew install python3
pip3 install virtualenv
virtualenv venv 
source venv\bin\activate
pip3 install -r requirements.txt
```

You should see (venv) $ at your command prompt, letting you know that you’re running the proper virtualenv install. To deactivate, you can just run the following to come out of the environment.

```bash
deactivate
```

##### Windows
Please add instructions if you use windows.
 
#### Running the dev server
In production, we have an nginx reverse proxy setup. For development however, it's useful to use the built in development server. Navigate to the memberportal folder. (`cd memberportal` on bash) First we need to make sure we have a local sqlite database with the correct migrations applied so run this:

```bash
python3 manage.py migrate
```
 
After running that you should see something like this:
```bash
angular2html
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, portal, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
```

If that completes with no errors run the command below to start the development server.

```bash
python3 manage.py runserver
```

You should see something like this:

```bash
Django version 2.0.7, using settings 'memberportal.settings'
Starting development server at http://127.0.0.1:8000/
```

Take note of the IP and port. In this case, open your favourite browser and go to `http://127.0.0.1:8000/`. You should
be presented with the home page of the web app. If you want to contribute any changes to the portal please see below.

#####NOTE
You will need to re-run the database migration every time the db models change. You may see random database related errors such as column does not exist if you forget to do this. You can do that by running:

```python3 manage.py migrate```

To test all of the features you will need some api keys. Define these as environment variables:
* SENDGRID_API_KEY
* TRELLO_API_KEY
* TRELLO_API_TOKEN
* STRIPE_PUBLIC_KEY
* STRIPE_SECRET_KEY
* XERO_CONSUMER_KEY
* XERO_RSA_FILE (path to the rsa key)
* DISCORD_INTERLOCK_WEBHOOK
* DISCORD_DOOR_WEBHOOK