FROM rasa/rasa-sdk:3.5.0

# Change back to root user to install dependencies
USER root

RUN pip install openai

# Switch back to non-root to run code
USER 1001