FROM python:3.10

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY server.py /server.py
COPY templates /templates

ENTRYPOINT ["python"]
CMD ["/server.py"]