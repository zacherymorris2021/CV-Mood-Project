# Mood Detection: Linking Extracted Mood From Images to Spotify Songs
Because of the large trained model file, it was not possible to deploy the application through heroku. Infact it was not possible to even upload the file into Github. Therefore, if you are interested in trying ou the application, please follow the following steps to clone the repo, download the trained model and to run the application locally.


## Step 1: Getting Started
First clone or download the repository following the instruction on github

### Step 2: Downloading the trained model
You can download the trained model (vgg_emotion) from here: https://drive.google.com/file/d/1ir21jKBWa-_a-OOFWawOAtOQi6B-5Ybg/view?usp=sharing

Once downloaded place the file in the CVMoodProject Folder where files such as predict_app.py and moodtape_functions.py reside.

### Step 3: Installing all the dependencies to run the application
In order to install all the dependencies, run the followinf command in terminal whenin the project folder
```
pip3 install -r requirements.txt
```


### Step 4: Tell Flask where to find your application 
For Linux and Mac
```
export FLASK_APP=predict_app.py   
```

For Windows
```
set FLASK_APP=predict_app.py
```

### Step 5: Run the application
Use the following command to run the application
```
flask run --host=0.0.0.0
```


