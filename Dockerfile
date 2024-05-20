# start by pulling the python image
FROM python:3.11

# switch working directory
RUN mkdir /app

WORKDIR /app


# copy every content from the local file to the image
COPY . .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt
# configure the container to run in an executed manner

CMD ["python","upload.py" ]