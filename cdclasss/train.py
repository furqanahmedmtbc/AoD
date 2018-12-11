import os
from keras.callbacks import ModelCheckpoint, TensorBoard
import numpy as np
import gc

gc.collect()

def train_my_model(model, X, X_test, Y, Y_test):
    checkpoints=[]
    if not os.path.exists('Data/Checkpoints/'):
        os.makedirs('Data/Checkpoints/')
    checkpoints.append(ModelCheckpoint('Data/Checkpoints/best_weights.h5', monitor='val_loss', verbose=0, save_best_only=True, save_weights_only=True, mode='auto', period=1))
    checkpoints.append(TensorBoard(log_dir='Data/Checkpoints/./logs', histogram_freq=0, write_graph=True, write_images=False, embeddings_freq=0, embeddings_layer_names=None, embeddings_metadata=None))
    
    
    
    from keras.preprocessing.image import ImageDataGenerator
    generated_data= ImageDataGenerator(featurewise_center=False, featurewise_std_normalization=False, samplewise_std_normalization=False, zca_whitening=False, rotation_range=0, width_shift_range=.1, height_shift_range= .1, horizontal_flip=True, vertical_flip=False)
    generated_data.fit(X)
    print(X.shape)
    print(Y.shape)
    print(X_test.shape)
    print(Y_test.shape)
    model.fit_generator(generated_data.flow(X,Y, batch_size=10), steps_per_epoch=X.shape[0], epochs=1, validation_data=(X_test, Y_test), callbacks=checkpoints)
    
    return model

def main():
    from get_dataset import get_dataset
    X, X_test, Y, Y_test = get_dataset()
    #print('Step 1 done')
    #print(X.shape)
    #print(X_test.shape)
    #print(Y.shape)
    #print(Y_test.shape)
    X=X.reshape(X.shape[0],X.shape[1],X.shape[2],1)
    X_test=X_test.reshape(X_test.shape[0],X_test.shape[1],X_test.shape[2],1)
    #X=X.reshape(1,X.shape[0],X.shape[1],X.shape[2])
    #Y=Y.reshape(Y.shape[0],1,1,1)
    #Y=Y.reshape(Y.shape[0],1)
    
    #print(X.shape)
    #print(Y.shape)
    
    from makensave_model import get_model
    model = get_model(len(Y[0]))
    
    print('Step 2 done')
    model = train_my_model(model, X, X_test, Y, Y_test)
    
    
    from makensave_model import save_model
    save_model(model)
    
    print('Step 3 done')
    return model

if __name__ == '__main__':
    main()