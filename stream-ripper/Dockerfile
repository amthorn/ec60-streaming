FROM jrottenberg/ffmpeg:4.4-alpine

RUN apk add curl
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["sh", "/entrypoint.sh"]