# Image prediction (Cat or Dog)

In this tutorial we will try to walk together through all the building blocks of a Machine/Deep Learning project in production, i.e. a model that people can actually interact with

As a case study, we’ll be creating a web interface for image recognition using the pretrained model.

## DEMO FILE:
https://github.com/kaniska-m/Image-prediction-using-docker/assets/153006677/acd2dbb3-a335-4f3d-b103-13d360b18c15

## Build model : 

I've used use a pretrained (and effective) Convolutional Neural Network model for image classification 


link to model -->  https://huggingface.co/spaces/Sa-m/Dogs-vs-Cats/blob/main/best_model.h5

[model.py](./best_model.py) describe how to load the model, preprocess images in order to be used by that model, and make predictions.

## Create API : Flask


We are also using Flask-Uploads (or Flask-Reuploaded) which allows your application to flexibly and efficiently handle file uploading and serving the uploaded files.

[upload.py](./upload.py) contains the code responsible for running the API. It interacts with the [web page](./templates/upload.html) where the client will upload his image.

## Containerize : Docker

In short, Docker allows us to create reproducible environments. To do so for the API we've just created, we have to :

**1.** The first thing to do, obviously, is to [download and install Docker](https://www.docker.com/products/docker-desktop)

**2.** Create the [requirements.txt](./requirements.txt) in your main directory

**3.** Create a [Dockerfile](./Dockerfile) (without extension) which contains the instructions for building your Docker image

**4.** In a terminal, run the following command to build the Docker image:
  ```
      #docker image build -t flask_docker .
  ```

```
   #docker run -p 5000:5000 -d flask_docker
```

Once this is running, you should be able to view your app running in your browser at
```
http://localhost:5000/upload
```







