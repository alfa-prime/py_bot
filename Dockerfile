FROM python:3.9.7-slim

WORKDIR /usr/src/py-bot/


COPY . .
RUN pip install --upgrade pip; \
    pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["main.py"]