# anagram-words
Small Flask application to manage words and get the anagrams related. Using an authentication system.

# Dependencies
Python                              3.7

Flask                               1.1.2

Flask-RESTful                       0.3.8

Psycopg2                            2.8.6

Flask-SQLAlchemy                    2.4.4

Flask-Migrate                       2.7.0

Flask-Script                        2.0.6

Flask-HTTPAuth                      4.2.0

Gunicorn                            20.0.4

# Installation
It's docker based so, all you need is internet connection, a database already configured and run the docker-compose.yml.

In the case you already have a database instance, you can run only DockerFile.

# Configuration
Inside the docker-compose.yml (or DockerFile, if you are using it) you have the following variables who you must to modify:

LOG_LEVEL -> Values allowed: ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

ANAGRAM_DB_USER -> Postgres database username

ANAGRAM_DB_PASS -> Postgres database password

ANAGRAM_DB_HOST -> Postgres database host

ANAGRAM_DB_PORT -> Postgres database port

ANAGRAM_DB_NAME -> Postgres database name

ANAGRAM_SECRET_KEY -> Secret key to secure JWT authentication

**Important:** You need to grant all access to user in database provided

# Executing
**Using docker-compose:**

Open a command line into the folder where docker-compose.yml is present.

Execute the following command to build the docker-compose:

`docker-compose build`

Execute the following command to run the docker-compose:

`docker-compose up`

**Using Dockerfile:**

Open a command line into the folder where Dockerfile is present.

Execute the following command to build our container:

`docker build -t anagramwords .`

After the success build, run following command to run our application:

`docker run -p 5000:5000 --name anagrams anagramwords`

# API Reference

***Register - Sign up***

Method: POST

URL: _/signup_

Body: `{
    "username": "your_username",
    "password": "your_password"
}`

Response: `{"token": "jwt_token"}`


***Authentication***

Method: POST

URL: _/login_

Body: `{
    "username": "your_username",
    "password": "your_password"
}`

Response: `{"token": "jwt_token"}`

***Get all anagram matches***

Method: GET

URL: _/anagram/< word >_

Headers: `{
    "Authorization": "Bearer jwt_token"
}`

Response: 
`[
    {
        'word': "string",
        'anagram': "string"
    },    
]`

***Add new word***

Method: PUT

URL: _/anagram/< word >_

Headers: `{
    "Authorization": "Bearer jwt_token"
}`

Response: 
`{
    'word': "string",
    'anagram': "string"
}`

***Delete word***

Method: DELETE

URL: _/anagram/< word >_

Headers: `{
    "Authorization": "Bearer jwt_token"
}`

Response:
`string message`
