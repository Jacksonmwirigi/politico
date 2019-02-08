

# Politico API's

In this project I am creating  end points that will allow party creation, editing a party, retrieving all the registerd parties and as well as goovernment offices from the politico system. 


Below are the Endpoints that I have been created.

| EndPoints       | Functionality  | HTTP Method  |
| ------------- |:-------------:| -----:|
| api/v1/parties | Create party| POST |
| api/v1/parties | Fetch all parties |GET|
| api/v1/parties/<int:party_id> |Fetch single party |GET|
| api/v1/parties/<int:party_id>/delete |Delete party |DELETE|
| api/v1/parties/<int:party_id>/edit|Edit party |PATCH|
| api/v1/offices |Create office |POST|
| api/v1/offices |Fetch all offices |GET|
| api/v1/offices/<int:office_id> |Fetch single office |GET|
| api/v1/offices/<int:office_id>/delete |Delete office |DELETE|
| api/v1/offices/<int:office_id>/edit |Update office |PATCH|
|
T|**TOOLS TO BE USED IN THE CHALLENGE**
1. Server-Side Framework:[Flask Python Framework](http://flask.pocoo.org/)
2. Linting Library:[Pylint, a Python Linting Library](https://www.pylint.org/)
3. Style Guide:[PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
4. Testing Framework:[PyTest, a Python Testing Framework](https://docs.pytest.org/en/latest/)
5. Testing Endpoints: [PostMan](https://www.getpostman.com/)
6. Testing Framework:[Coverage, a Python Testing Framework](https://coverage.readthedocs.io/en/v4.5.x/)
 
**Other requirements**

		pip install pytest

		pip install coverage

		pip install nose

		pip install flask

		virtualenv

**How to run the application**
 1.On your PC, create a new directory.
 2. Do a git init on the newly created directory/folder
 3. Create virtual environment by typing this in the terminal - virtualenv -p python3 venv(for python 3)
 4. `git clone` this  <code>[repo](https://github.com/Jacksonmwirigi/politico/)</code>
 4. run `pip install -r requirements.txt` on the terminal to install the dependencies
 6. Export the environment variable
 7. Then write this command on your terminal```flask run``` to start and run the server
 8. Then on [postman](https://www.getpostman.com/), use the above url's
 **Heroku Link**

 Navigate to this [link](https://politico-ap1-arrotech.herokuapp.com/) to run the application on heroku


**Author**

     Jackson Mwirigi Ithalii


**Contributors to the project**

     Abraham Ogol.
     Harun Gachanja
     Willies Wanjala
        