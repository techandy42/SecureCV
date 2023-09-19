# Face Detection Authenticator

- A face detection authenticator system built using OpenCV and Tkinter.

> Sign-up/Login

![Sign-up/Login](./pictures/signup_login_page.PNG)

> Train (takes 5~10s)

![Train](./pictures/train_page.PNG)

> Wait for Authentication (takes <1s)

![Wait for Authentication](./pictures/waiting_authentication_page.PNG)

> Authentication Successful

![Authentication Successful](./pictures/authentication_page.PNG)

> Guide

- Sign-up and login.
- Train the model. OpenCV will take 100 photos of you. The trained model is stored under `validator_models/` folder.
- Authenticate. OpenCV will take a photo of you then the program will run the face detection model, if the confidence level is below 100% (lower number means higher confidence), then the user will be authenticated. If not, the authentication will be rejected.
- The photos are not stored, however the weights of the trained models will be stored locally.
