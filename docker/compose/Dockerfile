FROM alpine:3.13.4
LABEL maintainer="Nicolas Bayle"

RUN apk add --no-cache --virtual build-dependencies \
    python3-dev python3 bash py3-pip \
    && pip3 install pymongo