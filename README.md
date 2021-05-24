# final_project_epam

## Flask REST API
REST API application scans a folder with all subfolders and text files and provides aggregate statistics for certain indicators.<br>

### Basic functionality:<br>
1.Web REST API<br>
2.For a start application scans DIR (base directory) with all subfolders and text files<br>
3.Information for REST API:<br>
  -List of folders and files<br>
	-Count of files<br>
	-Names_of files<br>
	-The most common word<br>
	-The rarest word<br>
	-Average length of words<br>
	-Count of vowels/consonants/syllables<br>
4.For each file or word you can use RESR API request: 	/api/file/readable-file-id 
5.You can use this app English and Russian words


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
$ curl -X GET "http://127.0.0.1:3000/api/file/1.txt"<br>
$ curl -X GET "http://127.0.0.1:3000/api/word/hello"


### API from the browser:
You can also work on the API directly in your browser with Swagger
http://127.0.0.1:3000/apidocs
![Screenshot](https://github.com/SparklingAcidity/final_project_epam/blob/for_testing/image/Снимок%20экрана%202021-05-20%20в%2020.27.29.png)
![Screenshot](https://github.com/SparklingAcidity/final_project_epam/blob/for_testing/image/Снимок%20экрана%202021-05-20%20в%2020.26.45.png)
![Screenshot](https://github.com/SparklingAcidity/final_project_epam/blob/for_testing/image/Снимок%20экрана%202021-05-20%20в%2020.27.22.png)

### API from Postman
You can use desktop app Postman fot rest requests.<br>
Run final_project_epam in command line:<br>
$ poetry run app<br>
Than use Postman for GET requests for folder and files inside and GET, POST, DELETE for words:<br>
![Screenshot](https://github.com/SparklingAcidity/final_project_epam/blob/for_testing/image/Снимок%20экрана%202021-05-20%20в%2010.30.15.png)
