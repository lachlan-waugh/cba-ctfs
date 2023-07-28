FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip

# Copy files over
WORKDIR /app
COPY . .
RUN python3 -m pip install flask requests uuid
RUN chmod +x "run.sh"

EXPOSE 5000

ENTRYPOINT [ "./run.sh" ]
