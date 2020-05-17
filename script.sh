#!/bin/bash

TOKEN=1085187414:AAGoY-iUZ43A1Ya8b4ortxbS2a_utuOZYz8
CHAT_ID=374545615
MESSAGE="Hello World"
URL="https://api.telegram.org/bot$TOKEN/sendMessage"

curl -s -X POST $URL -d chat_id=$CHAT_ID -d text="$MESSAGE"
