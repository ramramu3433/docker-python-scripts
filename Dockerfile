FROM python:2
MAINTAINER janakiraman
RUN mkdir /code
ADD test.py /code
ENTRYPOINT ["python","/code/test.py"]

