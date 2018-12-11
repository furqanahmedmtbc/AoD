import numpy as np
from os import listdir
from skimage import io
from scipy.misc import imresize
import scipy.misc
import os
#from keras.preprocessing.image import array_to_img, img_to_array, load_img

train_dir = r"C:\Users\furqanahmed\Documents\ML Training\CatDog classifier\Data\Training" 
test_dir = r"C:\Users\furqanahmed\Documents\ML Training\CatDog classifier\Data\Test"
data_path = r"C:\Users\furqanahmed\Documents\ML Training\CatDog classifier\Data"


def get_img(mdata_path):
    img_size=64
    img=io.imread(mdata_path, as_grey=True)
    img=imresize(img, (img_size, img_size, 3))
    return img



#def get_dataset(dataset_path=train_dir):
def get_dataset(dataset_path=test_dir):    
         labels = listdir(dataset_path)
         print('Categories:\n', labels)
         len_datas=0
         for label in labels:
             len_datas += len(listdir(dataset_path+'/'+label))
         
             if not os.path.exists(dataset_path + '/Converted/' + label):
                 os.makedirs(dataset_path + '/Converted/' + label)
          
                 
#         X=np.zeros((len_datas, 64,64,3),dtype='float64')
#         Y=np.zeros(len_datas)
         
         
         for label in labels:
             datas_path = dataset_path+'/'+label
             
             count_data=0
             count_categori=[-1,'']
             
             
                 
             
             for data in listdir(datas_path):
                 try:
                    img= get_img(datas_path+'/'+data)
                    #             X[count_data]= img
                    resize_path = dataset_path + '/Converted/'
                    fname=resize_path + str(label) +'/'+ str(count_data+1) + str('.jpg')
                    fname=str(fname)
                
                    print(fname)
                 
                 
                
                 
                    scipy.misc.toimage(img, cmin=0.0, cmax=...).save(fname)

                    if label != count_categori[1]:
                        count_categori[0]=1
                        count_categori[1]=label
                 
                    count_data+=1
        
                    print(str('Reading data entry: ')+ str(count_data))
                
                 except:
                      count_data+=1
             
                      print("Error reading this data entry!")
                     
         return
         
if __name__ == '__main__':
    get_dataset(test_dir)          
            
            
            
            
