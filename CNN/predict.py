import tensorflow
import numpy as np  
from tensorflow.keras.preprocessing import image
# from keras.preprocessing.image import ImageDataGenerator



# datagen = ImageDataGenerator(rescale=1/255)

model = tensorflow.keras.models.load_model("./model.h5")
img = image.load_img("./542.png", target_size=(75, 75))
img = image.img_to_array(img)
img = np.array([img])
result = model.predict(img)


if np.argmax(result) == 0:
    result = "withmask"
else:
    result = "withoutmask"


print(result)