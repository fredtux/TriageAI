#!/bin/bash

# Remove old models and cache
rm -fr .rasa/cache
rm -fr models

# # Add spacy en and ro
# if [ ! -d "../venv/lib/python3.10/site-packages/en_core_web_lg" ]; then
#     python -m spacy download en_core_web_lg
# fi

if [ ! -d "../venv/lib/python3.10/site-packages/ro_core_news_lg" ]; then
    python -m spacy download ro_core_news_lg
fi

# Train model
rasa train