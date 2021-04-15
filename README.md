# CS 3450 project Group 4 Parking Genie

## Organization and Name Scheme:
- All documentation will be in the docs/ directory
- Out team will follow the Django directory organization and naming scheme.
- Each template will be named according to the corresponding route.

## Version-Control:
- Each team member will fork this repository to make changes. Once their changes are complete, they will create a pull request for the rest of the team to review. When the pull request is approved, they will merge their changes into master.
- All changes will be pushed to this repository.
- All releases are tagged with their release number.

## Tool Stack:
We will develop our website using Django. Using Django will simplify our application's database interactions and organization.

## Setup Instructions
- Clone this repository:<br>
<code> git clone https://github.com/katiecorcoran/cs3450-group-4.git </code>
- Navigate to the "src" directory and create a new virtual environment: (if you don't have pip installed already, you probably need to install Python on your machine)<br>
<code> pipenv shell </code><br>
<code> pip install -r requirements.txt </code>

## Build Instructions:
- If you have not set up the virtual environment already, follow the setup instructions above.
- Activate the virtual environment:<br>
<code> pipenv shell </code>
- Navigate into the outter 'parkinggenie' directory
- Start the project:<br>
<code> python manage.py runserver </code>
- The project will run at http://localhost:8000.

## Unit Testing:
We used the built-in testing framework provided by Django to write unit tests for our application. All unit tests can be found in "src/testing". There are two files: one for testing models, and one for testing views. These unit tests verify that all models can be successfully instantiated, all views render correctly, and all post operations successfully create the required model. To run the tests, follow the build instructions above, and replace the final command with <code>python manage.py test</code>.

## System Testing:
Testing procedures can be found in "docs/Parking-Genie-System-Test-Steps". These test steps verify user interface operations. Test 1 verifies creating a user, test 2 verifies adding a lot, and tests 3 and 4 verify the parking space reservation process.

## Sprint Planning
All sprint docs can be found in "docs/planning"
