# Master_Thesis_ASR

This is my Master Thesis project.

# Installation
Follow these steps to install it on your PC:

1. Copy repositiory:

`git clone https://github.com/MatBar99/Master_Thesis_ASR.git`


2. Install requirements: 

`pip install -r requirements`


3. Download acoustic model (called model)
   
https://drive.google.com/file/d/1se1Rqfmoim99sPr3cI-wDLJFwDyadkZB/view?usp=sharing

4. Download language model (called scorer) 

https://drive.google.com/file/d/19pdnu1KPVDZyZvd07xsnuQpFo-72VOPG/view?usp=drive_link

5. Place them in main folder of this repository

# Usage
This app is simple FastAPI code, which has only one endpoint that can be used to transcript 
audio from list of files.
Endpoint is called `/transcript` and should be loaded from Swagger API.

*To run FastAPI type:*

`uvicorn main:app`

*Go to the address in your browser:*

`http://127.0.0.1:8000`

*Find endpoint `/transcript` and load files you want to transcript*


First loading and transcription may take some time due to initialization of the model...


