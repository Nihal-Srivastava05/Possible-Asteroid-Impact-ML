from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/classification', methods=['GET', 'POST'])
def classification_page():
    if request.method == 'POST':
        epoch = request.form.get('epoch')
        axis = request.form.get('axis')
        eccentricity = request.form.get('eccentricity')
        inclination = request.form.get('inclination')
        argument = request.form.get('argument')
        longitude = request.form.get('longitude')
        anomoly = request.form.get('anomoly')
        perihelion = request.form.get('perihelion')
        aphelion = request.form.get('aphelion')
        period = request.form.get('period')
        intersection = request.form.get('intersection')
        reference = request.form.get('reference')
        magnitude = request.form.get('magnitude')
        data = [epoch, axis, eccentricity, inclination, argument, longitude, anomoly, perihelion, aphelion, period, intersection, reference, magnitude]
        

    return render_template('classification.html')

@app.route('/impacts', methods=['GET', 'POST'])
def impacts_page():
    if request.method == 'POST':
        start = request.form.get('start')
        end = request.form.get('end')
        probability = request.form.get('probability')
        velocity = request.form.get('velocity')
        magnitude = request.form.get('magnitude')
        diameter = request.form.get('diameter')
        cpalermo = request.form.get('cpalermo')
        mpalermo = request.form.get('mpalermo')
        torino = request.form.get('torino')
        data = [start, end, probability, velocity, magnitude, diameter, cpalermo, mpalermo, torino]

    return render_template('impacts.html')

@app.route('/clustering', methods=['GET', 'POST'])
def clustering_page():
    if request.method == 'POST':
        start = request.form.get('start')
        end = request.form.get('end')
        impacts = request.form.get('impacts')
        probability = request.form.get('probability')
        velocity = request.form.get('velocity')
        magnitude = request.form.get('magnitude')
        diameter = request.form.get('diameter')
        cpalermo = request.form.get('cpalermo')
        mpalermo = request.form.get('mpalermo')
        torino = request.form.get('torino')
        data = [start, end, impacts, probability, velocity, magnitude, diameter, cpalermo, mpalermo, torino]

    return render_template('clustering.html')

@app.route('/visualization')
def visualization_page():
    return render_template('visualization.html')