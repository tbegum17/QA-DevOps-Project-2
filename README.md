# QA DevOps Project 2: Book Date Generator
## Author - Tasnim Begum
## Project Objective
- Create an application that has four microservices which interact with one another to make objects using some defined logic.
- The application will be a books generator to show the different books that are going to be released

### Microservice Architecture
- Front-end (Service 1):
	- The service where the user interacts with the application
	- This sends requests to the other services to make different books and shows this to users and storing them in the database
- Book Name API (Service 2): 
   - This service receives HTTP GET requests from service 1 and responds with a randomly selected book name chosen from a list
- Author API (Service 3):
    - This service receives HTTP GET requests from service 1 and gives a response showing the selected date from a list
- Date API (Service 4):
    - This service receives HTTP POST requests from service 1 and shows the randomly selected book name and date as JSON objects. 
    - Service 4 will use the name of book and author to determine the release date of the book.

## Risk Assessment
Once there was an overall idea for what the application will be, a risk assessement table was created to illustrate the various risks that can occur throughout the duration of the project. This was made to ensure that any risks that were to occur during the project were reduced and able to resolve any risks that were to occur in the project.
<p> 
<img src = "https://user-images.githubusercontent.com/60227889/188701716-70aeb133-a8b2-473a-b822-540364b56c2f.png" widith="1000">


## Trello Board
In order to track the progress of the project, this was completed with the use of Trello. On this a Kanban Board was created to show the different tasks that needed to be completed for the project and - tasks that are being completed at the moment or any outstanding tasks. The tasks that have not been completed are highlighted in red and the tasks completed are in green. 
<p>
<img src = "https://user-images.githubusercontent.com/60227889/188703647-ad01a508-dbd8-4ada-9b2e-d9c2531a4ab3.png" widith="1000">


## Application
This is the application that was created for this project. On this users can essentially go onto the page and find out information about a particular book. The information that is being shown for this generator is the name of the book, the author of the book and the date that it will be released.
<p>
<img src = "https://user-images.githubusercontent.com/60227889/188863642-880b0434-a73b-4c67-bb25-2901696c6c60.png" widith="1000">


## Jenkins Pipeline
For this application, an Jenkins Pipeline was produced to get the docker images pushed within the background of the application. This pipeline also produces the docker images that are required in order for the application to run. 
<p>
<img src = "https://user-images.githubusercontent.com/60227889/188704569-e32c317b-7822-4cac-9b9a-ab0bd7db89d0.png" widith="1000">


## Testing






