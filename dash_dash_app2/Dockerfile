# Use python, version 3.6 as the base image.
# We won't install debian packages, so just use the slim variant.
FROM python:3.6-slim

# Install required python packages
# Note: This way of formating the instruction allows to easily
# add/remove/comment packages

RUN mkdir -p /work
WORKDIR /work


COPY requirements.txt /work/requirements.txt



RUN pip install -r requirements.txt





ADD displaydata.csv  /work/displaydata.csv
ADD display.py /work/display.py 
ADD displayAll.py /work/displayAll.py 
ADD assets/GUI.css /work/assets/GUI.css
ADD loader.py /work/loader.py 

## change it to display.py to run secind script
CMD [ "python", "./displayAll.py" ]


# Declare port 8888
EXPOSE 8050
