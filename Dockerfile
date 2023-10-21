FROM python:3-alpine
WORKDIR /usr/src/app
COPY . .
RUN pip install .
ENTRYPOINT [ "wafw00f" ]
