from flask import Flask, render_template, Response, url_for
from datetime import datetime
import random
import json
import time
import audioEngine
import matplotlib.pyplot as plt
import lineCodes

app = Flask(__name__)
random.seed()

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/test')
# def randomChart():
#     def makeRandom():
#         while(True):
#             binData = [random.randint(0, 1) for i in range(255)]
#             for item in binData:
#                 json_data = json.dumps(
#                     {'key': item, 'value': item})
#                 yield f"data:{json_data}\n\n"
#                 time.sleep(0.08)
#     return Response(makeRandom(),  mimetype='text/event-stream')


@app.route('/test')
def randomChart():
    def makeRandom():
        for item in audioEngine.generateAudioChunks(RATE=8000):
            for i in item:
                json_data = json.dumps(
                    {'key': int(i), 'value': int(i)})
                yield f"data:{json_data}\n\n"
                time.sleep(0.08)
    return Response(makeRandom(),  mimetype='text/event-stream')


# @app.route('/test')
# def randomChart():
#     def makeRandom():
#         for item in audioEngine.generateAudioChunks(RATE=8000):
#             for i in item:
#                 json_data = json.dumps(
#                     {'key': int(i), 'value': int(i)})
#                 yield f"data:{json_data}\n\n"
#                 time.sleep(0.08)
#     return Response(makeRandom(),  mimetype='text/event-stream')



if __name__ == '__main__':
    app.run(debug=True)
