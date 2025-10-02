import os
from flask import Flask
from threading import Thread

app = Flask("keep_alive")

@app.route("/")
def home():
  return "OK"

def run():
  port = int(os.environ.get("PORT", 5000))  # Render provides PORT
  app.run(host="0.0.0.0", port=port)

def start():
  t = Thread(target=run)
  t.daemon = True
  t.start()
