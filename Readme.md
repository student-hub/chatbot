# Polly Chatbot

## Introduction
 
    Polly is a multilingual chatbot that will interact with students at the at the Faculty of Automatic Control and Computer Science (POLITEHNICA University of Bucharest). It will answer both their frequently asked questions and various common problems in a student's life, such as "When does my course start and end?". Students will be able to chat with Polly through the ACS-UPB app.

## Setup

    // run the setup script
    ./setup.sh

## Train Polly
    ### RO
    cd src/
    rasa train

    ### EN
    cd srcEN/
    rasa train

## Chat with Polly

    // run the action server
    rasa run actions
    rasa shell