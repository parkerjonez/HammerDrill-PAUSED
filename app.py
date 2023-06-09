from flask import Flask
import logging
from watchtower import CloudWatchLogHandler

app = Flask(__name__)

@app.route('/')
def hello_world():
    app.logger.info("Hello world endpoint was hit")
    return 'Hello, World!'

if __name__ == "__main__":
    # Configure the Watchtower log handler to send logs to CloudWatch
    handler = CloudWatchLogHandler()
    # Create a Logger with the name of your application, and attach the CloudWatch handler
    log = logging.getLogger('hammer-drill')
    log.setLevel(logging.INFO)
    log.addHandler(handler)
    
    app.logger.addHandler(handler)
    app.run(debug=True)
