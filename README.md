# [Argon Dashboard Flask](https://www.creative-tim.com/product/argon-dashboard-flask) [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&logo=twitter)](https://twitter.com/home?status=Material%20Dashboard,%20a%20free%20Material%20Bootstrap%204%20Admin%20Template%20%E2%9D%A4%EF%B8%8F%20https%3A//bit.ly/2Lyat1Y%20%23bootstrap%20%23material%20%23design%20%23developers%20%23freebie%20%20via%20%40CreativeTim)

 ![version](https://img.shields.io/badge/version-1.0.1-blue.svg) [![GitHub issues open](https://img.shields.io/github/issues/creativetimofficial/argon-dashboard-flask.svg?maxAge=2592000)](https://github.com/creativetimofficial/argon-dashboard-flask/issues?q=is%3Aopen+is%3Aissue) [![GitHub issues closed](https://img.shields.io/github/issues-closed-raw/creativetimofficial/argon-dashboard-flask.svg?maxAge=2592000)](https://github.com/creativetimofficial/argon-dashboard-flask/issues?q=is%3Aissue+is%3Aclosed) [![Join the chat at https://gitter.im/NIT-dgp/General](https://badges.gitter.im/NIT-dgp/General.svg)](https://gitter.im/creative-tim-general/Lobby) [![Chat](https://img.shields.io/badge/chat-on%20discord-7289da.svg)](https://discord.gg/E4aHAQy)

![Argon Dashboard Flask - Admin Dashboard coded in Django.](https://github.com/creativetimofficial/argon-dashboard-flask/blob/master/media/argon-dashboard-flask-intro.gif)

<br />

> Free product - **Flask Dashboard** starter project - Features:

- Up-to-date [dependencies](./requirements.txt): **Flask 2.0.1**
- [SCSS compilation](#recompile-css) via **Gulp**
- UI Kit: **Argon Dashboard** (Free Version) provided by **[Creative-Tim](https://www.creative-tim.com/)**
- Flask Codebase - provided by **[AppSeed](https://appseed.us/)**
- SQLite, PostgreSQL, SQLAlchemy ORM
- Alembic (DB schema migrations)
- Modular design with **Blueprints**
- Session-Based authentication (via **flask_login**)
- Forms validation
- Deployment scripts: Docker, Gunicorn / Nginx, Heroku

<br />

## Table of Contents

* [Demo](#demo)
* [Docker Support](#docker-support)
* [Quick Start](#quick-start)
* [Documentation](#documentation)
* [File Structure](#file-structure)
* [Browser Support](#browser-support)
* [Resources](#resources)
* [Reporting Issues](#reporting-issues)
* [Technical Support or Questions](#technical-support-or-questions)
* [Licensing](#licensing)
* [Useful Links](#useful-links)

<br />

## Demo

> To authenticate use the default credentials ***test / pass*** or create a new user on the [registration page](https://www.creative-tim.com/live/argon-dashboard-flask).

- **Argon Dashboard Flask** [Login Page](https://www.creative-tim.com/live/argon-dashboard-flask)

<br />

## Quick start

> UNZIP the sources or clone the private repository. After getting the code, open a terminal and navigate to the working directory, with product source code.

```bash
$ # Get the code
$ git clone https://github.com/creativetimofficial/argon-dashboard-flask.git
$ cd argon-dashboard-flask
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Database
$ pip3 install -r requirements.txt
$
$ # OR with PostgreSQL connector
$ # pip install -r requirements-pgsql.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## Documentation
The documentation for the **Argon Dashboard Flask** is hosted at our [website](https://demos.creative-tim.com/argon-dashboard-flask/docs/1.0/getting-started/getting-started-flask.html).

<br />

## File Structure
Within the download you'll find the following directories and files:

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- routes.py                 # Define app routes
   |    |    |-- markov.py
   |    |    |-- markov_frequency.py
   |    |    |-- markov_execute_file.py
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- routes.py                 # Define authentication routes  
   |    |    |-- models.py                 # Defines models  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |    |    |-- includes/                 # HTML chunks and components
   |    |    |    |-- navigation.html      # Top menu component
   |    |    |    |-- sidebar.html         # Sidebar component
   |    |    |    |-- footer.html          # App Footer
   |    |    |    |-- scripts.html         # Scripts common to all pages
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |         |-- index.html            # Index page
   |    |         |-- 404-page.html         # 404 page
   |    |         |-- *.html                # All other pages
   |    |    
   |  config.py                             # Set up the app
   |    __init__.py                         # Initialize the app
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |-- requirements-mysql.txt               # Production modules  - Mysql DMBS
   |-- requirements-pqsql.txt               # Production modules  - PostgreSql DMBS
   |
   |-- Dockerfile                           # Deployment
   |-- docker-compose.yml                   # Deployment
   |-- gunicorn-cfg.py                      # Deployment   
   |-- nginx                                # Deployment
   |    |-- appseed-app.conf                # Deployment 
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- run.py                               # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- `run.py` loads the `.env` file
- Initialize the app using the specified profile: *Debug* or *Production*
  - If env.DEBUG is set to *True* the SQLite storage is used
  - If env.DEBUG is set to *False* the specified DB driver is used (MySql, PostgreSQL)
- Call the app factory method `create_app` defined in app/__init__.py
- Redirect the guest users to Login page
- Unlock the pages served by *home* blueprint for authenticated users

<br />



- Copyright 2019 - present [Creative Tim](https://www.creative-tim.com/)
- Licensed under [Creative Tim EULA](https://www.creative-tim.com/license)

