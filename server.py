from flask import Flask, render_template, Response, url_for
from datetime import datetime
import json
import time
import audioEngine
import lineCodes
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def generateData(function):
    for item in audioEngine.generateAudioChunks(RATE=8000):
        x, y = function(np.array(item))
        for i in y:
            json_data = json.dumps(
                {'key': int(i), 'value': int(i)})
            yield f"data:{json_data}\n\n"
            time.sleep(0.08)


@app.route('/unipolar')
def unipolarData():
    return Response(generateData(lineCodes.unipolar),  mimetype='text/event-stream')

@app.route('/bipolar')
def bipolarData():
    return Response(generateData(lineCodes.bipolar),  mimetype='text/event-stream')

@app.route('/RZ')
def RZData():
    return Response(generateData(lineCodes.RZ),  mimetype='text/event-stream')

@app.route('/NRZ-I')
def NRZ_IData():
    return Response(generateData(lineCodes.NRZ_I),  mimetype='text/event-stream')

@app.route('/NRZ-L')
def NRZ_LData():
    return Response(generateData(lineCodes.NRZ_L),  mimetype='text/event-stream')

@app.route('/manchester')
def manchesterData():
    return Response(generateData(lineCodes.manchester),  mimetype='text/event-stream')

@app.route('/differential-manchester')
def differentialManchesterData():
    return Response(generateData(lineCodes.differential_manchester),  mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)
