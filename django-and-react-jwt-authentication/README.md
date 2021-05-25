# Django & React JWT Authentication

This is an authentication system using React, Redux and Django with the Django Rest Framework

This project is for study and learn.

# Running

In the **frontend** folder, run:

```bash
npm install
```

this will install the required frontend packages

```bash
npm run build
```

this will make a build folder and copy it into the backend folder

In the **backend** folder, run:

```bash
pyenv shell 3.8.5
pyenv virtualenv djangoreactauth
pyenv activate djangoreactauth
pip install -r requirements.txt
```

Create .env file with environments variables, see .env.sample for details

## Preparations for Dev

Frontend install packages:

```bash
sudo apt-get install npm
sudo npm i -g npx
sudo npm i -g create-react-app
```

Frontend create app:

```bash
sudo npx create-react-app frontend
```

```bash
npm install --save axios react-router-dom redux redux-devtools-extension react-redux redux-thunk
```



Backend install packages:

```bash
pip install -r backend/requirements.txt
```

Backend create app:

```bash
django-admin startproject auth_system
cd auth_system
python manage.py startapp accounts
```
