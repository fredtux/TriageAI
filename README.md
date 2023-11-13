# (Archived) Triage AI (Archived)

**Disclaimer** : This is for educational purposes only. **DO NOT USE IN PRODUCTION**

### This is a Romanian language triage chatbot

![Screenshot](screenshot.png)

## Credits
- [https://github.com/RasaHQ/rasa](https://github.com/RasaHQ/rasa) for Rasa obviously
- [https://github.com/JiteshGaikwad/Chatbot-Widget](https://github.com/JiteshGaikwad/Chatbot-Widget) for the chatbot widget

## How to use
Run the **start.sh** script. You need to have an OpenAI token in order to run the explanation tasks
```bash
./start.sh
```
After everything is set up, open a browser and navigate to: [http://localhost:8080](http://localhost:8080)

## How to test
Run the **test.sh** script
```bash
./test.sh
```

## Implementation details
### Docker
It uses 3 containers:
- **rasa_actions** for Rasa custom actions
    - the Dockerfile installs _openai_ with pip in order to use the API
    - uses .env file that can be generated from the _start.sh_ script
- **rasa** for the Rasa model
    - the Dockerfile installs _ro_core_news_lg_ language package for spacy
- **webapp** for the Nginx server that serves a static page with the widget

### Start.sh
Can be used with the _cleanup_ parameter to remove old models. It will train Rasa if no models are found, then it will run docker-compose for the _docker-compose.yml_ file.

### Test.sh
Executes docker-compose for the _docker-compose.test.yml_ file that contains 2 containers:
- **rasa_actions** for Rasa custom actions
- **rasa** with the _test_ command

All containers used in the _docker-compose.test.yml_ are used in the production environment as well

### Check stories
In order to check if all the stories result in a color code, run **stories_graph.py** and check for red nodes. All the nodes with a path to the leaves will be in green and all the leaves in blue

```bash
python3 stories_graph.py
```

### OpenAI API
The _start.sh_ script will generate the .env file used by the **rasa_actions** container

**Enjoy!!!**
