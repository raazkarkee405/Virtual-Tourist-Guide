# Virtual Tourist Guide 

Virtual Tourist Guide is a chatbot that simply provides the information about Nepal and its different aspects based on the users queries automatically. It is based on tourism domain. 

The chatbot is developed as the final year project. 

## Problem Statement

1. Tourists have to spend a lot of time searching for an appropriate information during the time they plan for travel
2. They  face problems due to scattered data on websites and unable to find user-friendly interfaces.
3. Being in a foreign land, they feel helpless in case  of emergency or a panic situation. 
4. Their travel experience becomes miserable if they don't have anyone to guide them like a friend.
5. There's no assistant to deal with tourists' problems such as medical emergency, accommodation, etc

## Solution 

1. The idea is to develop a travel buddy for the people to make them fall in love with the beauty of Nepal.
2. The travel bot interacts with the users and help them visit the tourist spots of Nepal. The bot can provide information about different places to visit, things to do, culture, history, festival, etc of Nepal.
3. The bot will provide different accommodation and health facility information based on the city user provided. The user can also get more information of the accommodations and health facilty such as address, contact number, email, etc.

## Why chatbots?

### CHATBOTS

1. More user friendly
2. Saves a lot of time
3. Precise information display
4. Much faster process

### APPS

1. Shows what it wants to show to user
2. Takes time to process desired information
3. Data is scattered and more than required
4. Slower than chatbots

### Software Used

1. Technology used:
2. Rasa 
5. Facebook Messenger
6. Facebook developer tools
8. Google Cloud Platform
9. Flask API
10. Docker-compose
11. Pythonanywhere server

## Description

I have built a chatbot called 'Virtual Assistant' capable of understanding and responding to a person's requests. There are two main components in the Rasa stack that helped build this travel assistant — Rasa NLU & Rasa core. Intent classification and entity recognition is handled by Rasa NLU, while Rasa core is the main framework of the stack where it provides dialogue management backed by machine learning.

This repo contains some training data and the main files needed to build an assistant on your local machine. The travel assistant consists of the following files:

1. data/nlu.md contains training examples for the NLU model
2. data/stories.md contains training stories for the Core model
3. config.yml contains the model configuration
4. domain.yml contains the domain of the assistant
5. credentials.yml contains credentials for the Messenger channel
6. actions.py contains actions used by the chatbot such as searching accommodation and health facility 

## Chatbot Architecture

![](/screenshots/rasa.png)

## Screenshots

![](/screenshots/11.jpg)
![](/screenshots/12.jpg)
![](/screenshots/13.jpg)
![](/screenshots/14.jpg)
![](/screenshots/15.jpg)
![](/screenshots/1.jpg)