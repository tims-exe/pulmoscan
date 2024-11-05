from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from rest_framework.decorators import api_view
from rest_framework.response import Response
from PIL import Image


#model1 = load_model('./models/model1.keras')

# Create your views here.

def preprocess_image(img_file, target_size=(150, 150)):
    # Open the image file using PIL
    img = Image.open(img_file)  # Use PIL to open the image
    img = img.resize(target_size)  # Resize the image to the target size
    img_array = image.img_to_array(img)  # Convert image to numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array / 255.0  # Normalize pixel values to [0, 1]
    return img_array

def testmodel1(request):
    model1 = load_model('./models/model1.keras')
    test_image_path = "./models/m2.jpg"

    test_image = preprocess_image(test_image_path)
    predictions = model1.predict(test_image)  

    class_names = ['Normal', 'Malignant']
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_class_index]

    return HttpResponse(f"Prediction: {predicted_class}")



def testmodel2(request):
    model2 = joblib.load('./models/model2.pkl')
    test = {
        "GENDER":1,
        "AGE":69,
        "SMOKING":1,
        "YELLOW_FINGERS":2,
        "ANXIETY":2,
        "PEER_PRESSURE":1,
        "CHRONIC_DISEASE":1,
        "FATIGUE":2,
        "ALLERGY":1,
        "WHEEZING":2,
        "ALCOHOL_CONSUMING":2,
        "COUGHING":2,
        "SHORTNESS_OF_BREATH":2,
        "SWALLOWING_DIFFICULTY":2,
        "CHEST_PAIN":2,
    }

    test_df = pd.DataFrame([test])
    test_df['GENDER'] = test_df['GENDER'].map({'M': 1, 'F': 0})

    prediction = model2.predict(test_df)

    if prediction[0] == 1:
        return HttpResponse(f"Lung Cancer : Yes")
    else :
        return HttpResponse(f"Lung Cancer : No")
    
@api_view(['POST'])
def model1(request):
    try:
        model1 = load_model('./models/model1.keras')
        
        image_file = request.FILES['image_upload']

        test_image = preprocess_image(image_file)

        predictions = model1.predict(test_image)  

        class_names = ['Normal', 'Malignant']
        predicted_class_index = np.argmax(predictions[0])
        predicted_class = class_names[predicted_class_index]

        return Response({"prediction": predicted_class})
    except KeyError:
        return Response({"error": "Image file not found in the request"}, status=400)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['POST'])
def model2(request):

    # YES : 2
    # NO : 1
    
    model2 = joblib.load('./models/model2.pkl')
    data = request.data

    test_df = pd.DataFrame([data])
    test_df["GENDER"] = test_df["GENDER"].map({'M': 1, 'F': 0})

    prediction = model2.predict(test_df)

    if prediction[0] == 1:
        return Response({"prediction": "Yes"})
    else :
        return Response({"prediction": "No"})









'''
{
    "GENDER": 1,
    "AGE": 69,
    "SMOKING": 1,
    "YELLOW_FINGERS": 2,
    "ANXIETY": 2,
    "PEER_PRESSURE": 1,
    "CHRONIC_DISEASE": 1,
    "FATIGUE": 2,
    "ALLERGY": 1,
    "WHEEZING": 2,
    "ALCOHOL_CONSUMING": 2,
    "COUGHING": 2,
    "SHORTNESS_OF_BREATH": 2,
    "SWALLOWING_DIFFICULTY": 2,
    "CHEST_PAIN": 2
}

{
    "GENDER": 1,
    "AGE": 69,
    "SMOKING": 1,
    "YELLOW_FINGERS": 1,
    "ANXIETY": 1,
    "PEER_PRESSURE": 1,
    "CHRONIC_DISEASE": 1,
    "FATIGUE": 1,
    "ALLERGY": 1,
    "WHEEZING": 1,
    "ALCOHOL_CONSUMING": 1,
    "COUGHING": 1,
    "SHORTNESS_OF_BREATH": 1,
    "SWALLOWING_DIFFICULTY": 1,
    "CHEST_PAIN": 1
}
'''





























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