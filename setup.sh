#!/bin/bash

# install rasa
# https://rasa.com/docs/rasa/installation/
pip3 install -U pip
pip3 install rasa

# install spaCy
# https://spacy.io/usage
pip install -U pip setuptools wheel
pip install -U spacy

# download the models
python3 -m spacy download en_core_web_md
python3 -m spacy download ro_core_news_md

# link the models
python3 -m spacy link ro_core_news_md ro
python3 -m spacy link en_core_web_md en
