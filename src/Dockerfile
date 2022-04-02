FROM python:3.7-slim

RUN python -m pip install rasa==3.1.0 && \
    pip install -U pip setuptools wheel && \
    pip install -U spacy==3.1.3 && \
    python3 -m spacy download ro_core_news_md && \
    python3 -m spacy link ro_core_news_md ro && \
    pip install firebase_admin

WORKDIR /app
COPY . .

RUN rasa train nlu

USER 1001

ENTRYPOINT ["rasa"]

CMD ["run", "--enable-api", "--port", "5005"]
