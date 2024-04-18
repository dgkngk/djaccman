FROM ubuntu:latest
LABEL authors="doguk"

ENTRYPOINT ["top", "-b"]