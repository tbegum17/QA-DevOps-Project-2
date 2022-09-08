# QA DevOps Project 2: Book Date Generator
## Author - Tasnim Begum
## Project Objective
- Create an application that has four microservices which interact with one another to make objects using some defined logic.
- The application will be a books generator to show the different books that are going to be released as well as a date for them to be released.

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
<p>
<img src = "https://user-images.githubusercontent.com/60227889/189104266-7ab659e6-399d-4be2-835e-d246ea26d64c.png" widith="1000">

<p>
Additionally, a database will be created for the sole purpose of saving all of the data that the application is going to be making and show the history of the last 5 books that have been presented within the application. The Entity Diagram for the database can be seen below:
<p>
<img src = "https://user-images.githubusercontent.com/60227889/189088573-9be4e457-b55f-42cd-bff3-8e3ee17a0a20.png" widith="1000">

<p>


## Risk Assessment
Once there was an overall idea for what the application will be, a risk assessement table was created to illustrate the various risks that can occur throughout the duration of the project. This was made to ensure that any risks that were to occur during the project were reduced and able to resolve any risks that were to occur in the project.
<p> 
<img src = "https://user-images.githubusercontent.com/60227889/188701716-70aeb133-a8b2-473a-b822-540364b56c2f.png" widith="1000">


## Trello Board
In order to track the progress of the project, this was completed with the use of Trello. On this a Kanban Board was created to show the different tasks that needed to be completed for the project and - tasks that are being completed at the moment or any outstanding tasks. The tasks that have not been completed are highlighted in red and the tasks completed are in green. 
<p>
<img src = "https://user-images.githubusercontent.com/60227889/188703647-ad01a508-dbd8-4ada-9b2e-d9c2531a4ab3.png" widith="1000">


## Application
This is the application that was created for this project showing the four microservices made. On this users can essentially go onto the page and find out information about a particular book. The information that is being shown for this generator is the name of the book, the author of the book and the date that it will be released. 
<p>
<img src = "https://user-images.githubusercontent.com/60227889/188863642-880b0434-a73b-4c67-bb25-2901696c6c60.png" widith="1000">

<p>
In addition to these four services on the application, NGINX was made that is being used for the reverse proxy. The NGINX service listens to port 80 on the machine and essentially directs traffic from port 80 on the host to port 5000 on the front end container where the app is being accessed. Moreover, docker swarm has been used in running the application through using a swarmmaster and swarmworker VM. This was created and currently running with the use of Ansible.  



## Jenkins Pipeline
For this application, an Jenkins Pipeline was produced to get the docker images pushed within the background of the application as well produces the docker images that are required in order for the application to run. This pipeline was also made to complete unit testing for the application and - you can see on the image below that the testing completed was done rapidly.
<p>
<img src = "https://user-images.githubusercontent.com/60227889/188913067-4e83c7df-e2d0-432d-8b5c-e10cdffb7aa6.png"

<p>
	
## Testing
Testing was completed to help indicate whether the application was functioning and completing the relevant procedures it was required to do. Testing was completed for all four microservices and - the methods that were used to complete these tests were unit and mock testing. 

### Front End
![image](https://user-images.githubusercontent.com/60227889/189110873-622f2c7a-ea94-44b4-9b5a-0aaab106d54e.png)



### Books
![image](https://user-images.githubusercontent.com/60227889/188916492-ce806b75-a5a2-480c-b036-d07172c3648d.png)


### Author
![image](https://user-images.githubusercontent.com/60227889/188917205-b5ef58fc-ba21-4b8f-8378-82d2f593b34b.png)


### Date
![image](https://user-images.githubusercontent.com/60227889/188917258-a58a917a-410f-421f-97e8-bfd0b0935e7f.png)





