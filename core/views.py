# Model Imports
import tensorflow
import numpy as np  
from tensorflow.keras.preprocessing import image

#Misc
import numpy as np
from PIL import Image
import tempfile
import cv2
import base64



# Django Imports 
from django.shortcuts import render
from django.conf import settings
from django.template.response import TemplateResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from keras.preprocessing.image import ImageDataGenerator
from django.core.files.storage import FileSystemStorage

    
def index(request):
    message = ""
    try:
        takenImg = request.FILES['image']
        model = tensorflow.keras.models.load_model('core/model.h5')
        with tempfile.NamedTemporaryFile() as temp:
            temp.write(takenImg.read())
            temp.flush()
            
            # Load the image from the temporary file
            img = image.load_img(temp.name, target_size=(75, 75))
            img = image.img_to_array(img)
            img = np.array([img])
            result = model.predict(img)



        if np.argmax(result) == 0:
            result = "withmask"
        else:
            result = "withoutmask"
        context =             {
                "message": message,
                "image": takenImg,
                # "image_url": fss.url(image_path),
                "prediction": result,
            }
        print("================================================================== Conext Prediction", type(context["prediction"]))
        return render(request, "index.html", context)
        
    except MultiValueDictKeyError:
        return render(request, "index.html", context = {"message": "No Image Selected"})
    
    # ====================TEST==============================
    
    
    
# class CustomFileSystemStorage(FileSystemStorage):
#     def get_available_name(self, name, max_length=None):
#         self.delete(name)
#         return name
    
    
# def index(request):
#     message = ""
#     prediction = ""
#     fss = CustomFileSystemStorage()
    
#     try:
#         takenImg = request.FILES['image']
        
#         image = request.FILES['image'].read()
#         image = file_data = base64.b64encode(image).decode("utf-8")
#         model = tensorflow.keras.models.load_model('core/model.h5')
#         print("============================", image)

#         with tempfile.NamedTemporaryFile() as temp:
#             temp.write(takenImg.read())
#             temp.flush()
            
#             # Load the image from the temporary file
#             img = image.load_img(temp.name, target_size=(75, 75))
#             img = image.img_to_array(img)
#             img = np.array([img])
#             result = model.predict(img)



#         if np.argmax(result) == 0:
#             result = "withmask"
#         else:
#             result = "withoutmask"
#         context =             {
#                 "message": message,
#                 "image": takenImg,
#                 "image_url": image,
#                 "prediction": result,
#             }
#         print("================================================================== Conext Prediction", type(context["prediction"]))
#         return render(request, "index.html", context)
        
#     except MultiValueDictKeyError:
#         return render(request, "index.html", context = {"message": "No Image Selected"})
    

        