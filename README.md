# Directory Brute Forcing :sparkles: 

### Author: 

__Name__: Dinasoa RATSIMBA

__Reference__: STD21028

__Email__: hei.dinasoa@gmail.com

### Description: 

_Directory Brute Forcing with flask_

This project aims to implement a directory brute forcing method on a Flask web server. Directory brute forcing is a technique used to discover hidden directories and files on a web server by attempting to guess their names.

The brute forcing process will be carried out by sending a series of HTTP GET requests with different paths to test based on wordlist. By analyzing the server responses, we will be able to determine which directories or files exist on the server and which are hidden directories or files.

### Installation: 

* PREREQUISITES: 
> Python (any version)

If you dont have python yet you can install it [here](https://www.python.org/downloads/)

After you have cloned the projects, these are the steps that should be done to execute this project locally: 

* Create a virtual environment: 
```code
    python -m venv venv
```
* Activate it
```code
    source venv/bin/activate
```
* Then install the required package: 
```code
    pip install -r requirments.txt
```

### How to run the project? 
Everything has alread been set up, you just have to run these commands to start the project

* Run the flask server first: 

```code
    flask --app pathtrav.py run
```

* Run the directory brute forcing: 
```code
    python main.py
```

### Project structure

```
project
│   README.md
│   main.py
│   pathtrav.py
│   requirements.txt
└───config
│   │  config.py (contains the base URL)
└───wordlist
    │   dir_list.txt
└───templates
    │   index.html
```
