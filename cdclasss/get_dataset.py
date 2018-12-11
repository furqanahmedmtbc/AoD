import numpy as np
from os import listdir
from skimage import io
from scipy.misc import imresize
from keras.preprocessing.image import array_to_img, img_to_array, load_img

train_dir = r"C:\Users\furqanahmed\Documents\ML Training\CatDog classifier\Data\Training" 
test_dir = r"C:\Users\furqanahmed\Documents\ML Training\CatDog classifier\Data\Test"
data_path = r"C:\Users\furqanahmed\Documents\ML Training\CatDog classifier\Data\Training\Converted"

def get_img(mdata_path):
    img_size=64
    img=io.imread(mdata_path, as_grey=True)
    img=imresize(img, (img_size, img_size, 3))
    return img

def get_dataset(dataset_path=data_path):
    try:
        X=np.load(dataset_path + '/npy_train_data/X.npy')
        Y=np.load(dataset_path + '/npy_train_data/Y.npy')
        print('Dataset successfully fetched! Samples made!')
    except:
         labels = listdir(dataset_path)
         print('Categories:\n', labels)
         len_datas=0
         for label in labels:
             len_datas += len(listdir(dataset_path+'/'+label))
         
         X=np.zeros((len_datas, 64,64),dtype='float64')
         Y=np.zeros(len_datas)
         count_data=0
         count_categori=[-1,'']
         
         for label in labels:
                datas_path = dataset_path+'/'+label
                
                for data in listdir(datas_path):
                    #img= get_img(datas_path+'/'+data)
                    img=io.imread(datas_path+'/'+data)
                    X[count_data]= img
                    
                    if label != count_categori[1]:
                        count_categori[0]=1
                        count_categori[1]=label
                        
                    Y[count_data]= count_categori[0]
                    count_data+=1
                    
                    print('Reading data entry: ' + str(count_data))
            
            
         import keras
         Y= keras.utils.to_categorical(Y)
         import os
         if not os.path.exists(dataset_path + '/npy_train_data/'):
             os.makedirs(dataset_path + '/npy_train_data/')
         np.save(dataset_path + '/npy_train_data/X.npy', X)
         np.save(dataset_path + '/npy_train_data/Y.npy', Y)
        
    from sklearn.model_selection import train_test_split
    X=X[:100]
    Y=Y[:100]
    nX, nX_test, nY, nY_test = train_test_split(X,Y, test_size=0.1, random_state=42)
    print('Dataset successfully fetched! Samples made!')
    print(nX.shape)
    print(nX_test.shape)
    print(nY.shape)
    print(nY_test.shape)
    print(len(nY[0]))
    return nX,nX_test, nY, nY_test

    
 
if __name__ == '__main__':
    get_dataset(data_path)   
    
    
    
    