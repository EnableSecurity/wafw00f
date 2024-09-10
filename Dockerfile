FROM python:3.8-alpine
WORKDIR /usr/src/app
COPY . .
RUN python setup.py install
ENTRYPOINT [ "wafw00f" ]
