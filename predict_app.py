import base64
import numpy as np
import io
from PIL import Image
import torch
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
from flask import request, render_template, url_for, redirect
from flask import jsonify
from flask import Flask

import spotipy
import spotipy.util as util

app = Flask(__name__)
from moodtape_functions import authenticate_spotify, aggregate_top_artists, aggregate_top_tracks, select_tracks, create_playlist
client_id = "a03c795040e94889be87f6a0f24cdd9b"
client_secret = "c7f07543201e4beebe0d6c0676300c20"
redirect_uri = "https://localhost:5000/predict"
scope = 'user-library-read user-top-read playlist-modify-public user-follow-read'


def get_model():
    global model_emotion
    model_emotion = torch.load("vgg_emotion.pt")
    print(" * Model Loaded")

preprocessFn = transforms.Compose(
    [transforms.Resize(256), 
     transforms.CenterCrop(224), 
     transforms.ToTensor(), 
     transforms.Normalize(mean = [0.485, 0.456, 0.406], 
                          std = [0.229, 0.224, 0.225])])
imagenetClasses = {0:"amusement",1:"anger",2:"excitement",3:"sadness"}
print("* Loading torch model ...")
get_model()


@app.route('/', methods=['GET', 'POST']) 
def login():
    global spotify_auth 
    global top_artists
    global top_tracks
    if request.method == 'POST':
        username = request.form['username']
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
        spotify_auth = authenticate_spotify(token)
        top_artists = aggregate_top_artists(spotify_auth)
        top_tracks = aggregate_top_tracks(spotify_auth, top_artists)
        return redirect(url_for('predict'))
    else:
        return render_template('username.html') 

   

@app.route('/predict')
def my_form():
    return render_template('predict.html')

@app.route("/predict", methods=['POST'])
def predict():
    print('predict was clicked!')
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    print('after image is opened')
    processed_image = preprocessFn(image).unsqueeze(0)
    predictions = model_emotion(processed_image)
    probs, indices = (-F.softmax(predictions, dim = 1).data).sort()
    probs = (-probs).numpy()[0][:10]; indices = indices.numpy()[0][:10]
    preds = [imagenetClasses[idx] + ': ' + str(prob) for (prob, idx) in zip(probs, indices)]
    mood = getMoodScore(preds)
    selected_tracks = select_tracks(spotify_auth, top_tracks, mood)
    playlist = create_playlist(spotify_auth, selected_tracks, mood)
    response = {
        'prediction': preds,
        'playlist': playlist
    }
    return jsonify(response)


def getMoodScore(preds):
    predKeyValue= preds[0].split(": ")
    mood = predKeyValue[0]
    score = float(predKeyValue[1])
    moodVal = 0
    energyVal = 0
    if mood == "excitement":
        moodVal = 0.75 + 0.25*score
        energyVal = 0.8
    if mood == "amusement":
        moodVal = 0.5 + 0.25*score
        energyVal = 0.5
    if mood == "anger":
        moodVal = 0.5 - 0.25*score
        energyVal = 0.8
    if mood == "sadness":
        moodVal = 0.25 - 0.25*score
        energyVal = 0.5
    print("mood:", moodVal)
    return moodVal
   

