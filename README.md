# Docker

This project was done for the purpose of exercise.

In our scenario, a team has created an application that allows to use a sentiment analysis algorithm: it allows to predict if a sentence is positive or negative. This API is deployed in a container whose image is for the moment datascientest/fastapi:1.0.0.

The entry points of our API:

/status returns 1 if the API is running
/permissions returns a user's permissions
/v1/sentiment returns the sentiment analysis using an old model
/v2/sentiment returns the sentiment analysis using a new template
The /status entry point simply checks that the API is working. The /permissions entry point allows someone, identified by a username and a password to see which version of the template they have access to. Finally the last two take a sentence as input, check that the user is identified, check that the user has the right to use this template and if so, return the sentiment score: -1 is negative; +1 is positive.

The following tests have been applied:
- Authentication: 
In this first test, we are going to check that the identification logic works well. To do this, we will need to make GET requests on the /permissions entry point. We know that two users exist alice and bob and their passwords are wonderland and builder. We'll try a 3rd test with a password that doesn't work: clementine and mandarine.
The first two requests should return a 200 error code while the third should return a 403 error code.

- Authorization: 
In this second test, we will verify that our user authorization logic is working properly. We know that bob only has access to v1 while alice has access to both versions. For each of the users, we will make a query on the /v1/sentiment and /v2/sentiment entry points: we must then provide the arguments username, password and sentence which contains the sentence to be analyzed.

- Content:
In this last test, we check that the API works as it should. We will test the following sentences with the alice account:
life is beautiful
that sucks


This project includes:
- a docker-compose.yml file that contains the sequence of tests to performed
- the Python files used in the Docker images
- the Dockerfile used to build these images
- a file called setup.sh containing the commands used to build the images and launch the docker-compose
- the result of the logs in a log.txt file
- a docker-compose.yml file that contains the sequence of tests to be performed
