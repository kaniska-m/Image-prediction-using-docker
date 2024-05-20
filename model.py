import tensorflow as tf
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg19 import preprocess_input
from keras.applications.vgg19 import decode_predictions
import numpy as np

model = tf.keras.models.load_model('./weights/best_model.h5', compile=False)

def process_image(image):
    '''
    Make an image ready-to-use by VGG19
    '''
    image = img_to_array(image)

    # convert the image pixels to a numpy array
    X_testing_dl = []
    image_dl = img_to_array(image)
    print(len(image_dl),len(image_dl[0]))
    X_testing_dl.append(image_dl)
    print(len(X_testing_dl),len(X_testing_dl[0]))
    X_testing_dl = np.array(X_testing_dl)
    print(X_testing_dl.shape)
    print(image_dl)
    print(X_testing_dl)
    return X_testing_dl

def predict_class(image):
    '''
    Predict and render the class of a given image 
    '''
    # predict the probability across all output classes
    yhat = model.predict(image)
    # convert the probabilities to class labels
    #label = decode_predictions(yhat)
    # retrieve the most likely result, e.g. highest probability
    if(yhat[0][0]>yhat[0][1]):
        prob = yhat[0][0]
        prediction = 'cat'
    else:
        prob = yhat[0][1]
        prediction = 'dog'
    percentage = '%.2f%%' % (prob*100)

    return prediction, percentage

if __name__ == '__main__':
    ''' for test'''
    # load an image from file
    image = load_img('../image.jpg', target_size=(224, 224))
    image = process_image(image)
    prediction, percentage = predict_class(image)
    print(prediction, percentage)