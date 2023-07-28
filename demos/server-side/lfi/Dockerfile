FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip

# Copy files over
WORKDIR /app
COPY . .
RUN python3 -m pip install flask urllib3

EXPOSE 5000

ENTRYPOINT [ "python3", "client/app.py" ]
