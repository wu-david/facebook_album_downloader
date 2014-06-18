#!/bin/bash

if [ -f 'AUTH_TOKEN' ]; then
    TOKEN=$(cat AUTH_TOKEN)
    rm -f 'AUTH_TOKEN'
else
    echo "AUTH_TOKEN file does not exist."
    echo "Request access token at https://developers.facebook.com/tools/explorer"
    echo "Copy token and run:"
    echo "echo \"{ACCESS_TOKEN}\" >> AUTH_TOKEN"
    exit 1
fi

#echo $TOKEN

if [ -n "$1" ]; then
    mkdir -p "$1"
    PHOTOS_DIR=$1
else
    mkdir -p "photos"
    PHOTOS_DIR="$(pwd)/photos"
fi
echo "Saving photos to $PHOTOS_DIR"

#ALBUMS_GET="https://graph.facebook.com/me/albums?access_token=$TOKEN"

#echo "$ALBUMS_GET"
if [ -f 'helper.py' ]; then
    ./helper.py $TOKEN $PHOTOS_DIR
fi

exit 0
