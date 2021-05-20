# final_project_epam

## Flask REST API
....

## Installation
### Clone the repo:<br>

$ git clone https://github.com/SparklingAcidity/final_project_epam<br>
$ cd final_project_epam<br>


### Create virtualenv:<br>
$ virtualenv venv<br>
$ source venv/bin/activate<br>
$ poetry install<br>


### Run the sample server:<br>
$ poetry run app<br>


### Run tests:<br>
$ poetry run pytest<br>

### API from the command line:
$ curl -X GET http://127.0.0.1:5000/api/folder<br>
$ curl -X GET http://127.0.0.1:5000/api/word/питон
![Screenshot](https://github.com/SparklingAcidity/final_project_epam/blob/for_testing/image/Снимок%20экрана%202021-05-20%20в%2010.30.39.png)

### API from the browser:
You can also work on the API directly in your browser, by opening http://127.0.0.1:5000/ , and make GET API requests.

### API from Postman
You can use desktop app Postman fot rest requests.<br>
Run final_project_epam in command line:<br>
$ poetry run app<br>
Than use Postman:<br>
![Screenshot](https://github.com/SparklingAcidity/final_project_epam/blob/for_testing/image/Снимок%20экрана%202021-05-20%20в%2010.30.15.png)
