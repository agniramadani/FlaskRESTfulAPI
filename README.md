# FlaskRESTfulAPI

This is a car dealerships RESTful API created with Flask.

## Getting Started

### Installing
A step by step series of examples that tell you how to get a development env running

In order to run the API on you computer you must have Python 3.8, Flask and one database application (PostgreSQL, MySQL...) installed.

Download Python:  ``` https://www.python.org/downloads/  ``` <br />
Download Flask:  ``` https://flask.palletsprojects.com/en/1.1.x/installation/  ``` <br />
Download PostgreSQL: ``` https://www.postgresql.org/download/ ``` <br />

After you have installed a database application on your computer, the next step is to create a database ex: FlaskAppDatabase

Clone the RESTful API on you machine from this link: ``` https://github.com/agniramadani/Flask-RestAPI.git ```

#### Set up virtual environment and run the project

For windows:

```bash
$ python -m venv venv               # Create virtual environment
$ venv\Scripts\activate             # Activate virtual environment
$ pip install -r requirements.txt   # Install pip dependencies
$ python app.py                     # Run the project     
```


### Create all the tables on the database
- Open the project in any editor, open the terminal and go to FlaskProject\api\model and run: <br />
 ``` python Model.py db init  ``` <br />
 ``` python Model.py db migrate ``` <br />
 ``` python Model.py db upgrade ``` <br />
- After you run these commands go and check if you have all the tables created on your database <br />

- If you want to restore the database from a higher version to lower <br />
``` python Model.py db downgrade  ``` <br />
- For help run <br />
``` python Model.py db --help  ``` <br />


## How to use the API

As the project is a RESTful API I will use a software development tool (Postman) to interact with the API. <br />
Download Postman:  ``` https://www.postman.com/downloads/  ``` <br />


### Administrator endpoints

- Create Administrator ``` http://localhost:5000/api/administrator ``` [Method POST]  <br />
 ``` 
 {
   "name": "newAdmin",
   "super_admin": true
 }
 ``` 

- Read All Administrators ``` http://localhost:5000/api/administrator ``` [Method GET]  <br />

- Read Administrator By Id ``` http://localhost:5000/api/administrator/id ``` [Method GET]  <br />

- Update Administrator By Id ``` http://localhost:5000/api/administrator/id ``` [Method PUT]  <br />
```
{
   "name": "newName",
   "super_admin": false
}
``` 

- Delete Administrator By Id ``` http://localhost:5000/api/administrator/id ``` [Method DELETE]  <br />


### Seller endpoints

- Create Seller ``` http://localhost:5000/api/seller ``` [Method POST]  <br />
 ``` 
 {
   "name": "newSeller",
   "phone_number": "+389 70 111 222"
 }
 ``` 

- Read All Sellers ``` http://localhost:5000/api/seller ``` [Method GET]  <br />

- Read Seller By Id ``` http://localhost:5000/api/seller/id ``` [Method GET]  <br />

- Update Seller By Id ``` http://localhost:5000/api/seller/id ``` [Method PUT]  <br />
```
{
   "name": "newName",
   "phone_number": "+389 70 888 333"
}
``` 

- Seller id is a foreign key on the Car table, if you delete the seller all the cars with this seller id will be deleted likewise <br />
- Delete Seller By Id ``` http://localhost:5000/api/seller/id ``` [Method DELETE]  <br />


### Car endpoints

- Create Car ``` http://localhost:5000/api/car ``` [Method POST]  <br />
 ``` 
{
   "seller_id": 1,
   "make": "Mercedes-Benz",
   "model": "GT",
   "first_registration": 2020,
   "price": 127900,
   "fuel": "Gasoline"
}
 ``` 

- Read All Cars ``` http://localhost:5000/api/car ``` [Method GET]  <br />

- Read Car By Id ``` http://localhost:500/api/car/id ``` [Method GET]  <br />

- Update Car By Id ``` http://localhost:5000/api/car/id ``` [Method PUT]  <br />
```
{
   "make": "newMake",
   "model": "newModel",
   "first_registration": 2020,
   "price": 127900,
   "fuel": "Gasoline"
}
``` 

- Delete Car By Id ``` http://localhost:5000/api/car/id ``` [Method DELETE]  <br />


## Contributor
  
 * [Agni Ramadani](https://github.com/agniramadani)
