FROM alpine:3.5

RUN apk add --update \
	python \
	python-dev \
	openssl-dev \
	libffi-dev \
	build-base \
	vim \
	netcat-openbsd \
	curl \
	&& rm -rf /var/cache/apk/*

RUN curl -sS https://bootstrap.pypa.io/get-pip.py|python
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . /app
WORKDIR /app
RUN ln -s /usr/lib/python2.7 /app/lib
RUN mkdir /app/logs
CMD . /app/run.sh


