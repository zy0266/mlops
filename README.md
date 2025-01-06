********This project is made to practice machine learning work flow on a diamonds dataset.


********structure 


## enviornment control
> conda enviornment 
bash
conda env list #see all thoes env
conda activate name #activate before run 
conda deactivate #
This section I use too env 
>file
requirements.yml  # including env name 
requirements.txt  #generate auto
requirements.in   #only thoes needed
you could create same env from thoes file ,remenber update it when you install more package 


## model Train 
env nyc-taxi
[NOTEBOOK](.\Final_project\MAIN.ipynb)
The first step of this project. In this section, we load data from kaggele API.Then clean,encode,split data.
Test different models and find the best performance one.

## track with mlflow
env nyc-taxi
[NOTEBOOK](.\Final_project\MAIN.ipynb)
>bash mlflow ui
experiments run metrics tags
choose the best model set a new experiment

## save model 
save dv and model together to [local_models](.\Final_project\web_service\local_models)


## web service use fast api
env nyc-taxi
[web_service](.\Final_project\web_service)
>bash uvicorn main:app --reload

## package it use docker
env nyc-taxi
Dockerfile.app
>bash docker build -t my-image .
>      docker run -it my-image
docker run -it -p 8000:8000 my-fastapi-app

## use work flow to control
env new-env
>prefect server start




