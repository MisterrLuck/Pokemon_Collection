# Pokemon Collection Tracker
This is a simple web app used to keep track of your pokemon card collection.
It is built in python using Flask

## Setup

```bash
git pull https://github.com/MisterrLuck/Pokemon_Collection.git
cd Pokemon_Collection # This might be wrong idrk
python -m venv .venv
pip install -r requirements.txt
cd src/
```
To run the app on only the host computer, run
`flask run`
To run the app on the local network, run
`flask run --host=0.0.0.0`

This will output an ip address in which the program is running. Just navigate to the URL in your web browser
