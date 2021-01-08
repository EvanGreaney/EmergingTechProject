#Emerging Tech Project 2020 - G00348451

## Project Overview

The goal of this project is to make predictions on a dataset using Machine Learning. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set.

Then create a web service that returns a predicted power value based on the speed value provided

## How To Run the Project

For Running this project, I am using Docker to host the web service on the local host.
To get get Docker you can visit the link below to download

https://www.docker.com/get-started

First you need to clone the repo from this github

Once the Rep has been cloned, open the project in Command Line as seen below

![EmergingTechPorj1](https://user-images.githubusercontent.com/37175022/104034924-6b92ef00-51c9-11eb-81b9-c43ecb3cf10c.PNG)

Then enter this command in to the command prompt : docker build -t windspeedtopower .
After running this command it should appear as below

![EmergingTechPorj2](https://user-images.githubusercontent.com/37175022/104035895-9d588580-51ca-11eb-812d-5be2327b87ea.PNG)

After building to docker we must then run windesppedto power on localhost:5000

This can be done by entering this command to the command prompt: docker run -d -p 5000:5000 windspeedtopower
After running it should appear as seen below

![EmergingTechPorj3](https://user-images.githubusercontent.com/37175022/104036230-0d670b80-51cb-11eb-8a92-7b6fedf70ba4.PNG)

From there you can go to localhost:5000 in Chrome to view the webservice , it should now appear like this.

![EmergingTechPorj4](https://user-images.githubusercontent.com/37175022/104036485-5e76ff80-51cb-11eb-87a3-2e596d001e3e.PNG)
