from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pickle

from sklearn import cluster

app = Flask(__name__, static_url_path='/static')

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/classification', methods=['GET', 'POST'])
def classification_page():
    if request.method == 'POST':
        epoch = float(request.form.get('epoch'))
        axis = float(request.form.get('axis'))
        eccentricity = float(request.form.get('eccentricity'))
        inclination = float(request.form.get('inclination'))
        argument = float(request.form.get('argument'))
        longitude = float(request.form.get('longitude'))
        anomoly = float(request.form.get('anomoly'))
        perihelion = float(request.form.get('perihelion'))
        aphelion = float(request.form.get('aphelion'))
        period = float(request.form.get('period'))
        intersection = float(request.form.get('intersection'))
        reference = float(request.form.get('reference'))
        magnitude = float(request.form.get('magnitude'))
        data = [epoch, axis, eccentricity, inclination, argument, longitude, anomoly, perihelion, aphelion, period, intersection, reference, magnitude]
        model_file = '../models/AsteroidClassification.pkl'
        classification_model = pickle.load(open(model_file, 'rb'))

        prediction = classification_model.predict([data])
        object_mapping = ['Amor Asteroid', 'Amor Asteroid (Hazard)', 'Apohele Asteroid',
                          'Apohele Asteroid (Hazard)', 'Apollo Asteroid',
                          'Apollo Asteroid (Hazard)', 'Aten Asteroid',
                          'Aten Asteroid (Hazard)']

        classification = object_mapping[int(prediction[0])]
        return render_template('classification.html', res= True, classification = classification)

    return render_template('classification.html')

@app.route('/impacts', methods=['GET', 'POST'])
def impacts_page():
    if request.method == 'POST':
        start = float(request.form.get('start'))
        end = float(request.form.get('end'))
        probability = float(request.form.get('probability'))
        velocity = float(request.form.get('velocity'))
        magnitude = float(request.form.get('magnitude'))
        diameter = float(request.form.get('diameter'))
        cpalermo = float(request.form.get('cpalermo'))
        mpalermo = float(request.form.get('mpalermo'))
        torino = float(request.form.get('torino'))
        data = [start, end, probability, velocity, magnitude, diameter, cpalermo, mpalermo, torino]
        model_file = '../models/AsteroidImpactsElasticNet.pkl'
        impact_model = pickle.load(open(model_file, 'rb'))

        polynominal_converter = pickle.load(open('../models/polynominal_converter.pkl', 'rb'))
        data = polynominal_converter.transform([np.array(data)])
        best_features = [ 0,  9, 36, 15, 48,  6, 23, 37, 12,  3, 20,  1, 34, 49, 41, 18, 33, 21, 10, 39, 16,  4, 51, 45,  7, 46, 35, 24, 40]
        data = data[0][best_features]
        scaler = pickle.load(open('../models/AsteroidImpactsScaler.pkl', 'rb'))
        X = scaler.transform([data])

        prediction = impact_model.predict(X)
        return render_template('impacts.html', res = True, prediction = prediction[0])

    return render_template('impacts.html')

@app.route('/clustering', methods=['GET', 'POST'])
def clustering_page():
    if request.method == 'POST':
        start = float(request.form.get('start'))
        end = float(request.form.get('end'))
        impacts = float(request.form.get('impacts'))
        probability = float(request.form.get('probability'))
        velocity = float(request.form.get('velocity'))
        magnitude = float(request.form.get('magnitude'))
        diameter = float(request.form.get('diameter'))
        cpalermo = float(request.form.get('cpalermo'))
        mpalermo = float(request.form.get('mpalermo'))
        torino = float(request.form.get('torino'))
        data = [start, end, impacts, probability, velocity, magnitude, diameter, cpalermo, mpalermo, torino]
        model_file = '../models/AsteroidClustering.pkl'
        clustering_model = pickle.load(open(model_file, 'rb'))

        cluster_impact_mapping = {2:5, 5:4, 0:3, 4:2, 3:1, 1:0}
        prediction = clustering_model.predict([data])
        cluster_impact = cluster_impact_mapping[prediction[0]]
        return render_template('clustering.html', res = True, cluster = cluster_impact)

    return render_template('clustering.html')

@app.route('/visualization')
def visualization_page():
    return render_template('visualization.html')