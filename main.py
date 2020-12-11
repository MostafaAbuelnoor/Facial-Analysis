import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' ##This is used to suppress the warnings given by tensorflow
import tensorflow as tf
#Comment the above lines if there's an error and the code isn't working as expected

from deepface import DeepFace
import pandas as pd

# Add photos to the photos folder in order to analyse them or do facial recognition on them

def main():
    faceRecognise("photos/will.jpg", "photos")
    faceAnalysis("photos/mostafa.jpg")
    faceVerify("photos/jackie.jpg", "photos/angelina.jpg")
    faceStream("photos")



############################### Face recognition
# This function looks at a photo (Argument 1) and sees if the person is in another photo in a database (Argument 2)
def faceRecognise(pic, database):
    df = DeepFace.find(img_path = pic, db_path = database) #Storing the results in a panda dataframe to be analysed
    print(df.head())
  
############################### Face analysis
# This function analyzes the face in the picture(Argument) and gives out the estimated age, gender, race and emotion
def faceAnalysis(pic):
    obj = DeepFace.analyze(pic, actions = ['age', 'gender', 'race', 'emotion']) # Analysing the picture and storing the results to be printed later
    print("Age: ",obj["age"])
    print("Race: ", obj["dominant_race"]) 
    print("Emotion: ", obj["dominant_emotion"]) 
    print("Gender: ", obj["gender"])


############################### Face verification
# This function returns whether or not two pictures(Both arguments) contain the same person
def faceVerify(pic1, pic2):
    result  = DeepFace.verify(pic1, pic2) # Comparing the two pictures
    print("Same person: ", result["verified"])


############################### Real time face analysis
# This function will give a real time analysis (Age, gender, emotion) of your face by opening the 
# webcamera and compares it to pictures in the database specified in the argument
# Note: My webcamera is not working properly so I am not sure if this works as intended or not.  
def faceStream(database):
    DeepFace.stream(database)


if __name__ == "__main__":
    main()
