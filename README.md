# django-poll-app


This django-poll-app allows public users to view and create polls. It supports the following functionality:

- Users can view list of polls and their voting results by breakdown of choice.
- Users can delete a poll question upon confirmation.
- Users can create new poll questions and add choices to select from.


## Tech Stack

### Back-end:
1. Python3
2. Django
3. SQLite (database)

### Front-end:
1. HTML
2. CSS
3. BootStrap

## Dependencies (please install)
- python3 (version 3.8.5) 
- pip   (version 21.0.1)
- django (version 3.1.7)
- Once pip is installed please run the following command in terminal 
  (inside project folder: Django_Project/mysite, run following command to install remaining dependencies found in the requirements.txt file)
  ```bash
  pip install -r requirements.txt
  ```

## Setup

Once project is downloaded go to project folder (Django_Project/mysite folder) and run the following commands in terminal:

```bash
python3 manage.py migrate    #this command sets up the database models, schema
python3 manage.py shell < resetDB.py   #this commands runs the file resetDB.py which is used to populate initial seed data to the database, and clear any other data
python3 manage.py runserver   #this command runs the server on port 8000
```
- Go to Browser and type the following into address bar to open app: *http://localhost:8000/polls*   

## Supported Endpoints

 ![Supported Endpoints](https://github.com/SameerKhan-Dev/django-poll-app/blob/main/mysite/polls/static/images/Url_paths.png?raw=true "Supported Endpoints")

## Future Improvements

This section higlights areas where I would like to improve the app in the future.

- Improve new question creation - add dynamic UI for adding & removing choices
- Have timers for polls - to control duration of how long polls will be open / available for (i.e 1 day etc.)
- Add categories for polls (sports, weather etc.) and allows users to filter the list of polls by category
- CSS styling, improve consistency and formatting
- Make app responsive across different screen sizes
- Add Extensive Error handling (some examples below)
    - when user accesses specific poll endpoints directly through address bar: it should give error 404 if specific poll does not exist, and redirect to index page
    - proper handling for endpoints that do not exist
    - if error occurs when saving question, choices or votes to database, give server error 500 and error message to the user
- Testing: Add unit tests / integration tests for all available views


## Screenshots of the App

### Available Polls - Index Page
![Available Polls - Index Page](https://github.com/SameerKhan-Dev/django-poll-app/blob/main/mysite/polls/static/images/django-app-index-page.png?raw=true? "Available Polls - Index Page")
### Poll Station Page
![Poll Station Page](https://github.com/SameerKhan-Dev/django-poll-app/blob/main/mysite/polls/static/images/django-app-poll-station.png?raw=true? "Poll Station Page")
### Poll Results Page
![Poll Results Page](https://github.com/SameerKhan-Dev/django-poll-app/blob/main/mysite/polls/static/images/django-app-poll-results.png?raw=true? "Poll Results Page")
### Delete Poll Page
![Delete Poll Page](https://github.com/SameerKhan-Dev/django-poll-app/blob/main/mysite/polls/static/images/django-app-delete-page.png?raw=true? "Delete Poll Page")
