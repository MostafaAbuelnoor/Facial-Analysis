from deepface import DeepFace
import pandas as pd


############################### Face recognition
#df = DeepFace.find(img_path = 'target/will.jpg', db_path = 'photos')
#print(df.head())
##dfs = DeepFace.find(img_path = ["img1.jpg", "img2.jpg"], db_path = "C:/workspace/my_db")


################################ face recognition with different models

models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "Dlib"]
for model in models:
   result = DeepFace.verify("target/will.jpg", "photos/will2.jpg", model_name = "DeepID")
   df = DeepFace.find(img_path = "target/will.jpg", db_path = "photos", model_name = model)
   print(result)
   print(df.head())




############################### Face analysis

# obj = DeepFace.analyze("jackie.jpg", actions = ['age', 'gender', 'race', 'emotion'])
# #objs = DeepFace.analyze(["img1.jpg", "img2.jpg", "img3.jpg"]) #analyzing multiple faces same time
# print(obj["age"]," years old ",obj["dominant_race"]," ",obj["dominant_emotion"]," ", obj["gender"])


############################### Face verification
# result  = DeepFace.verify("will.jpg", "cropped.jpg")
# #results = DeepFace.verify([['img1.jpg', 'img2.jpg'], ['img1.jpg', 'img3.jpg']])
# print("Is verified: ", result["verified"])



############################### Real time face analysis
# DeepFace.stream("database")

