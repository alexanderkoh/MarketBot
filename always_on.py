from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return 'Hello. The Crypto Bot is running'

def run():
  app.run(host='0.0.0.0', port=8000)

def always_on():
  t = Thread(target=run)
  t.start()