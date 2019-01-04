# Item Catalog Project

## About the Project
This is the second project of Udacity's Full Stack Web Developer Nanodegree.
The project aims to create a web application which lets users view and/or
manage the catalog. Depending on authorization, a user will be able to view the
catalog, the items of each category, the item description, and make changes such
as add, edit, and delete a certain item or category.

## How the Tool is Created
The web application is written with Python and Flask and also uses SQLAlchemy
for database functionalities. HTML and CSS are used for creating and styling the
web pages. JavaScript and AJAX are applied to implement API calls.

## How to Run the Web Application
### Programs
- **Python**

The application is written in Python programming language. To execute the
file you'll need to have Python installed on your computer.
(Download [here](https://www.python.org/downloads/).)

- **VirtualBox** (download [here](https://www.virtualbox.org/)) and **Vagrant** (download [here](https://www.vagrantup.com/))

The project should be executed in a virtual environment.

### Run the Web Application
Steps:
1. Fork this repo to your account.
2. Clone all the files to your local machine.
3. Run `python db_setup.py` to create the database on your machine.
4. Run `python db_init.py` to initialize the database with some dummy data created for you.
5. Run `python app.py` to bring up the web application.
6. In your web browser, type `http://localhost:8000` to see the web application in action. 
