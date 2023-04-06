#!/bin/bash

# Check if first parameter requires cleanup
if [ ! -z "$1" ] && [ "$1" = "cleanup" ]; then
    ./cleanup.sh
fi

# Check if OpenAI token is set
if [ ! -f ".env" ]; then
    echo "Please enter your OpenAI token: "
    read openai_token
    echo OPENAI_API_KEY = \"$openai_token\" > .env
fi

# Check if there is a venv
if [ -d "venv" ]; then
    source venv/bin/activate
else
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    pip install -r rasa/requirements.txt
fi

# Check if rasa is untrained
if [ ! -d "rasa/models" ]; then
    cd rasa
    if ! ./train.sh; then
        echo "Rasa training failed"
        exit 1
    fi
    cd ..
fi

# Start the docker containers
docker-compose up