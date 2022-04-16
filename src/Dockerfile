FROM python:3.7-slim

RUN python -m pip install rasa==3.0.8 && \
    pip install -U pip setuptools wheel && \
    pip install -U spacy==3.1.3 && \
    python3 -m spacy download ro_core_news_md && \
    python3 -m spacy link ro_core_news_md ro && \
    pip install firebase_admin

COPY . /app

WORKDIR /app

RUN rasa train

USER 1001

ENTRYPOINT ["rasa"]

CMD ["run", "-m", "app/models", "--enable-api", "--port", "5005"]
