FROM node:12.9.0-alpine

ENV HOME="/app" \
    LANG=C.UTF-8 \
    TZ=Asia/Tokyo 

WORKDIR ${HOME}

RUN apk update && \
    apk add git && \
    apk add --no-cache curl && \
    curl -o- -L https://yarnpkg.com/install.sh | sh

ENV PATH $HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH
ENV CHOKIDAR_USEPOLLING=true

RUN yarn global add @vue/cli \
    yarn install

ENV HOST 0.0.0.0
EXPOSE 3000