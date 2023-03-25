# Arceus
Arceus bot for discord server

## Bot VM setup

### Clone the repo
```
git clone https://github.com/chrizandr/Arceus
```

### Use virtual environment (optional)

```
sudo apt install python3-virtualenv
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
```

### Install requirements
```
sudo apt install python3-pip
pip install -r requirements.txt
```

### Add auth token to your environment
```
echo TOKEN=<your discord app token> > .env
```

### Start bot
```
python main.py
```
