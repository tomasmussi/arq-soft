FROM node:0.12.14

WORKDIR /var/www/html/frontend

EXPOSE 3000

RUN npm install typings webpack-dev-server rimraf webpack gulp-cli -g

RUN npm install gulp gulp-concat -D

CMD npm install && npm run server:dev:hmr
