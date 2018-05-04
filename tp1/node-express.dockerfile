FROM node:8.11.1
RUN apt-get update && apt-get install -yq vim
RUN mkdir app
WORKDIR /app
COPY js/package.json .
RUN ls && npm i && ls
