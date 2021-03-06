import os
import json
from keras.models import Sequential
from keras.layers import Dense, Dropout, MaxPooling2D, Activation, Flatten, Conv2D

def save_model(model):
    if not os.path.exists('Data/Model/'):
        os.makedirs('Data/Model/')
        model_json=model.to_json()
        with open('Data/Model/model.json', 'w') as model_file:
            #model_file.write(model_json)
            json.dump(model_json,model_file)
        model.save_weights('Data/Model/weights.h5')
        print('Model and weights saved!')
        return
    
def get_model(num_classes=2):
    model = Sequential()
    
    model.add(Conv2D(32,(3,3), input_shape=(64,64,1)))
    model.add(Activation('relu'))
    
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32,(3,3)))
    model.add(Activation('relu'))
    
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes))
    model.add(Activation('sigmoid'))
    
    model.compile(loss='binary_crossentropy', optimizer='adadelta', metrics=['accuracy'])
   
    print('Model made!')
    return model

if __name__ == '__main__':
    save_model(get_model())
    
    
    
    
    


