# QA DevOps Project 2: Books Date Generator
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

## Trello Board

## Application

## Jenkins Pipeline

## Testing






