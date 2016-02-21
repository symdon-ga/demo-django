FROM ubuntu:latest
MAINTAINER TakesxISximada <sximada@gmail.com>
ENV LANG C.UTF-8

# IIJ mirror
RUN sed -i.bak -e "s%http://archive.ubuntu.com/ubuntu/%http://ftp.iij.ad.jp/pub/linux/ubuntu/archive/%g" /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get install -y software-properties-common  # >= 14.04
RUN apt-add-repository ppa:fkrull/deadsnakes
RUN apt-get update -y

# for python3.5
RUN apt-get install -y git mercurial curl
RUN apt-get install -y python3.5 python3.5-dev python3-pip python-virtualenv  # use python3.5

ENV PROJECT_ROOT /srv/sximada/djangoexample
ENV PYTHONPATH $PROJECT_ROOT/settings

RUN mkdir -p $PROJECT_ROOT
WORKDIR $PROJECT_ROOT
RUN mkdir -p var log etc settings tmp src

RUN curl https://bootstrap.pypa.io/get-pip.py -o tmp/get-pip.py
ADD requirements/develop.txt tmp/requirements.txt
RUN python3.5 -m venv env --without-pip
RUN env/bin/python tmp/get-pip.py
Run if [ -f tmp/requirements.txt ]; then env/bin/pip install -r tmp/requirements.txt; fi

RUN env/bin/pip install ipdb

VOLUME ["$PROJECT_ROOT/src"]
VOLUME ["$PROJECT_ROOT/settings"]
VOLUME ["$PROJECT_ROOT/etc"]

ADD start.sh $PROJECT_ROOT/var/start.sh
EXPOSE 8000
ADD . $PROJECT_ROOT/src
CMD ["/bin/bash" , "$PROJECT_ROOT/var/start.sh"]
