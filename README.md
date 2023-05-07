# Master_Thesis_ASR

This is a beta version of my Master Thesis project.

Python version: 3.8.10

# Installation
Follow these steps to install it on your PC:

1. Copy repositiory:

`git clone https://github.com/MatBar99/Master_Thesis_ASR.git`


2. Install requirements: 

`pip install -r requirements`


3. Download acoustic model (called model)

`python -m wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm`


4. Download language model (called scorer) 

`python -m wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer`


# Usage
This app is simple FastAPI code, which has only one endpoint that can be used to transcript 
audio from list of files.
Endpoint is called `/transcript` and should be loaded from Swagger API.

*To run FastAPI type:*

`uvicorn main:app`

*Go to the address in your browser:*

`http://127.0.0.1:8000`

*Find endpoint `/transcript` and load files you want to transcript*


First loading may take some time due to initialization of the model...


