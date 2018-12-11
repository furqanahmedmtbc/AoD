from keras.models import model_from_json
import os
import numpy as np
from skimage import io

model_dir=r"C:\Users\furqanahmed\Documents\ML Training\CatDog classifier\Data\Model"
test_dir=r"C:\Users\furqanahmed\Documents\ML Training\CatDog classifier\Data\Test\Converted\Cat\92.jpg"

json_file = open(model_dir + '\model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights(model_dir + "\weights.h5")

model.compile(loss='binary_crossentropy', optimizer='adadelta', metrics=['accuracy'])
   
print(model.summary())

X=np.zeros((64,64),dtype='float64')
print(X)
#X=X.reshape(X.shape[0],X.shape[1],X.shape[2],1)
X=X.reshape(1,X.shape[0],X.shape[1],1)

print(X.shape)

img=io.imread(test_dir, as_grey=True)
print(X[0])
print(img)
X= img
print(X.shape)
X=X.reshape(1,X.shape[0],X.shape[1],1)
print(X.shape)

S = model.predict(X)
print(S)


