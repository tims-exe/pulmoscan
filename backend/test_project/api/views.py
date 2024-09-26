from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Create your views here.

def preprocess_image(img_path, target_size=(150, 150)):
    img = image.load_img(img_path, target_size=target_size)  # Load image with target size
    img_array = image.img_to_array(img)  # Convert image to numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array / 255.0  # Normalize pixel values to [0, 1]
    return img_array

def model1(request):
    model1 = load_model('./models/model1.keras')
    test_image_path = "./models/m2.jpg"

    test_image = preprocess_image(test_image_path)
    predictions = model1.predict(test_image)  

    class_names = ['Normal', 'Malignant']
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_class_index]

    return HttpResponse(f"Prediction: {predicted_class}")



def model2(request):
    model2 = joblib.load('./models/model2.pkl')
    test = {
        'GENDER':1,
        'AGE':69,
        'SMOKING':1,
        'YELLOW_FINGERS':2,
        'ANXIETY':2,
        'PEER_PRESSURE':1,
        'CHRONIC DISEASE':1,
        'FATIGUE':2,
        'ALLERGY':1,
        'WHEEZING':2,
        'ALCOHOL CONSUMING':2,
        'COUGHING':2,
        'SHORTNESS OF BREATH':2,
        'SWALLOWING DIFFICULTY':2,
        'ALLERGY' :1,
       'CHEST PAIN':2,
    }

    test_df = pd.DataFrame([test])
    test_df['GENDER'] = test_df['GENDER'].map({'M': 1, 'F': 0})

    prediction = model2.predict(test_df)

    if prediction[0] == 1:
        return HttpResponse(f"Lung Cancer : Yes")
    else :
        return HttpResponse(f"Lung Cancer : No")














































'''
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def getData(request):   
    test_data = {
        'name': 'abcde',
        'roll_no': 69,
    }
    return Response(test_data)




@api_view(['POST'])
def getInputData(request):
    res_data = {
        'pswd': 'Incorrect Password'
    }
    inputText = {
        's': 1,
        'p': 0,
    }
    if inputText['text'] == 'helloworld':
        res_data['pswd'] = 'Correct Password'
        return Response(res_data)

'''