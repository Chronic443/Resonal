### To run the application and deploy the code you will need python3.9 and virtualenv
### To get the project files you will require git

### The code is intended to run within a virtual environment it does not need to but strongly recommended. 
### To run the code follow the instructions bellow that assume you have python3.9
### Just go over to where you would like to create the project and run the following
```sh 
virtualenv -p <PATH_TO_PYTHON_3.9>  <YOUR_VENV_NAME>
source virtualenv_name/bin/activate

git clone https://github.com/Creator69/Resonal.git
pip install -r requirements.txt

export FLASK_APP=main.py
export FLASK_ENV=development
flask run
```
