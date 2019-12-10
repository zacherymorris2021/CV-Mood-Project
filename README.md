# Mood Detection: Linking Extracted Mood From Images to Spotify Songs
Because of the large trained model file, it was not possible to deploy the application through heroku. Infact it was not possible to even upload the file into Github. Therefore, if you are interested in trying ou the application, please follow the following steps to clone the repo, download the trained model and to run the application locally.

## Installation and Setup

### Step 1: Getting Started
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

## How to use the application
Step 1: Enter you spotipy username

Step 2: Once entered, you will be navigated to spotify authentication page. Login and allow access. This will take a bit of time, once done, the authentication page will say that the site cannot be reached and the link should start with localhost:5000/predict, like in the image down below. 

![Image of the authentication page after done](https://i.imgur.com/lNQ92fC.png)

Copy the link of that page  and go to terminal. which will currently look like this:
![Image of the terminal in the process](https://i.imgur.com/WtXFZ5q.png)

Paste that link into the terminal and authentication should be verified. You should be naviageted to the image uploading page in the applications. Where you can upload a image (only .jpg files) and get the perdiction as well as the created playlist.

An video example of how our application can be run can be found here:
https://drive.google.com/file/d/1sIGKgccc-2uN2_Fb_bpiz2alvLoWc1DG/view?usp=sharing


