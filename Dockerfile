# pull official base image
FROM python:3.10

# set work directory
WORKDIR /usr/src/app/

# copy requirements.txt
COPY requirements.txt requirements.txt

# install dependencies
RUN pip install --upgrade pip==22.1.2 && pip install -r requirements.txt

# copy project
COPY . .
