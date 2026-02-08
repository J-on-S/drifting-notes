#!/bin/bash
read -p "Do you want to read or send a message?" ans
if [ "$ans" = "read" ]; then
	echo "Your song recommendation for the day is this!"
elif [ "$ans" = "send" ]; then
	echo "Put your song for the day here!"
else
	echo "Not an option :( try again?"
fi

