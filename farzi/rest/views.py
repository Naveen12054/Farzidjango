
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .models import FurniturePrediction
import os
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.inception_v3 import preprocess_input
import numpy as np
from tensorflow import keras

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((376, 339))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def predict(image_path):
    preprocessed_image = preprocess_image(image_path)
    prediction = model.predict(preprocessed_image)
    return prediction

def seminar2(request):
    predicted_label = None
    latest_prediction = None

    if request.method == 'POST' and request.FILES['image']:
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        image_path = os.path.join('media', filename)

        prediction = predict(image_path)

        class_labels = {0: 'Bed', 1: 'Chair', 2: 'Sofa', 3: 'Swivel chair', 4: 'Table'}
        predicted_class = np.argmax(prediction)
        predicted_label = class_labels[predicted_class]

        FurniturePrediction.objects.create(image=filename, prediction=predicted_label)
        latest_prediction = FurniturePrediction.objects.latest('id')

    return render(request, 'seminar2.html', {'predicted_label': predicted_label, 'latest_prediction': latest_prediction})

model = keras.models.load_model('models/furniture_model.h5')

def result(request):
    # Retrieve the latest prediction from the database
    latest_prediction = FurniturePrediction.objects.latest('id')
    print("hai")
    print(latest_prediction)

    context = {
        'image_path': latest_prediction.image,
        'prediction': latest_prediction.prediction,
    }

    return render(request, 'result.html', context)