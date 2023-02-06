FROM python:3.11
ADD app.py .
RUN pip install -U Flask
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]