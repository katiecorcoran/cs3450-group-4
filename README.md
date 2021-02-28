# CS 3450 project Group 4 Parking Genie

## Organization and Name Scheme:
- All documentation will be in the docs/ directory
- Project is still in the planning stages; our team will decide on an official naming scheme once development progresses further.

## Version-Control:
- Each team member will fork this repository to make changes. Once their changes are complete, they will create a pull request for the rest of the team to review. When the pull request is approved, they will merge their changes into master.
- All changes will be pushed to this repository.
- All releases are tagged with their release number.

## Tool Stack:
We will develop our website using Django.
### Setup Instructions
- Clone this repository:<br>
<code> git clone https://github.com/katiecorcoran/cs3450-group-4.git </code>
- Navigate to the "src" directory and create a new virtual environment: (if you don't have pip installed already, you probably need to install Python on your machine)<br>
<code> pipenv install django~=3.1.0 </code>

## Build Instructions:
- If you have not set up the virtual environment already, follow the setup instructions above.
- Activate the virtual environment:<br>
<code> pipenv shell </code>
- Navigate into the outter 'parkinggenie' directory
- Start the project:<br>
<code> python manage.py runserver </code>
- The project will run at http://localhost:8000.

## Unit Testing:
We will use the built-in testing framework provided by Django.

## System Testing:
We will write testing procedures to run for each release.
