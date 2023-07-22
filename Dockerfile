FROM python:3.11.4-bullseye AS base
WORKDIR /var/www/pypi-clone
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

FROM base AS dev
RUN apt update -y && \
    apt install less tig tree vim -y
RUN git config --global core.editor vim && \
    git config --global core.hooksPath .githooks
RUN mkdir /root/.ssh
RUN pip install -r requirements.dev.txt
CMD [ "flask", "run", "--debug", "--host=0.0.0.0" ]

FROM base AS prod
CMD [ "flask", "run", "--host=0.0.0.0" ]
