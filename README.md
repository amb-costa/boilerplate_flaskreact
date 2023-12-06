# Boilerplate for React+Flask by amb-costa

* Built from the create-react-app project

```
$ cd rootfolder #where projects are stored
$ npx create-react-app appfolder
```

* Then installed flask, done with pipenv. Make sure to install SQLAlchemy and Admin as well
```
$ cd appfolder
$ python3 -m venv .venv #where .venv is the environment folder
$ cd .venv
$ source bin/activate
$ pipenv install flask
$ pipenv install Flask-SQLAlchemy
$ pipenv install Flask-Admin
```

* Useful commands for proper use:

```
$ npm start     #Runs app in developement mode on http://localhost:3000
$ cd flask
$ python3 app.py    #Runs the main flask file
```

* Keep the [React documentation](https://reactjs.org/) in mind for future work with tests, deployment and PWA
