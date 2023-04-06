FROM rasa/rasa:3.5.3-full

# Change back to root user to install dependencies
USER root

RUN python -m spacy download ro_core_news_lg

# Switch back to non-root to run code
USER 1001