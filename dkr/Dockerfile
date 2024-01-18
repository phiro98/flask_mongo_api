FROM python:3.8
COPY . .
RUN ls -a && pip install -r requirements.txt

ENTRYPOINT [ "python", "fmapp.py" ]