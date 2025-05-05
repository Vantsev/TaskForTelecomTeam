FROM ubuntu:22.04 AS build

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    bash \
    && rm -rf /var/lib/apt/lists/*

COPY ScriptLog.py /usr/src/app/

RUN pip3 install requests

WORKDIR /usr/src/app

RUN chmod +x /usr/src/app/ScriptLog.py

CMD ["/usr/bin/python3", "ScriptLog.py"]
