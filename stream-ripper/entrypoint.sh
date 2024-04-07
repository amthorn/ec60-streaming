#!/bin/bash

echo "Ripping..."

FFMPEG_CMD='ffmpeg -y -i - -c:v copy -c:a aac -ar 44100 -ac 1 -f flv'
echo "FFMPEG CMD: $FFMPEG_CMD"

echo "IP ADDRESS: $1"
echo "NAME: $2"

curl -k --ignore-content-length --output - -u "${BASIC_AUTH_STRING}" https://"$1":19443/https/stream/mixed | ${FFMPEG_CMD} rtmp://rtmp_server/live/"$2"