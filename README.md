# Face Analysis using Deepface Framework

This project is a facial recognition python script, I used a framework called [DeepFace](https://pypi.org/project/deepface/#modal-close). 

This script has 4 main functionalities: 
- Facial Recognition 
- Facial Verification 
- Facial Analysis
- Real Time Facial Analysis

Here is a [demo on youtube](https://youtu.be/8b6Qiq11eMI)

## Installation
I used [Python 3.8.6 64 bit version](https://www.python.org/downloads/release/python-386/) for this project. [Tensorflow 2.3.1](https://www.tensorflow.org/install/pip#ubuntu) was also needed for this script to work. Make sure [DeepFace](https://pypi.org/project/deepface/#modal-close) is also installed. 

To download Tensorflow run the following command: 
```bash
$ pip install --upgrade tensorflow
```
To download DeepFace:
```bash
$ pip install deepface
```
## Usage
In order to use the functionality of this script make sure you have the pictures that you want to analyze or compare in **jpg** format in the photos folder of this directory. 
***
### Recognition
If you want to recognize someone from their photo when you have a database of many people, use this function. 

`def faceRecognise(pic, database):`

It takes two arguments: 
1. The path to the target picture you want to get recognized
2. The database of the photos you want the algorithm to find 

This function will return a list of pictures that have the same face as the target picture
***
### Verification 
If you want to verify if two pictures have the same person this function is for you.

`def faceVerify(pic1, pic2):`

This function takes two arguments and they are basically the paths to the 2 pictures of the persons you want to compare. 

This function will return a boolean value of whether or not the two pictures share the same person.
***
### Analysis
If you wish to analyze someone's photo and extract useful information from, use this function. 

`def faceAnalysis(pic):`

This function takes in only one argument; the path to the picture of the photo you want to analyze. 

This function will return 4 predictions about the photo: 
1. Age 
2. Ethnicity
3. Emotion
4. Gender
***
### Real Time Analysis
This function will open your webcamera and analyse the face it sees. 

`def faceStream(database):`

This function takes in one argument which is the database that will compare the face the camera sees to the pictures in the database (can be used for attendance at work or classes for example). 

It also returns the expected age, emotion and gender of the user. 
***
## Potential Problems
If you want to add a picture to the photos database but you already ran the recognition function once, make sure you delete the pkl file generated to update the database with the new data.

Sometimes when you run the analysis functions for the first time some dependencies don't download properly from google drive, and will require you to download the file from the google drive link manually and put it in the correct folder (The link shows up in the terminal if you face the error). 


Please get in touch if you face this error and I will do my best to help you run these useful functions. 