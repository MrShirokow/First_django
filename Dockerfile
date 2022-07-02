# pull official base image
FROM python:3.10-alpine

# copy project
COPY . /usr/src/app/

# set work directory
WORKDIR /usr/src/app/

# install dependencies
RUN pip install --upgrade pip==22.1.2 && pip install -r requirements.txt

# runserver
# ENTRYPOINT ["python", "manage.py", "runserver"]
