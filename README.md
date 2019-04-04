# Doorbot-MCU

## Introduction
Doorbot micro-controller is the backend part of the doorbot project. It uses a camera and opencv to determine if a person is in a frame or not. You are required to use Firebase as the database and serverless backend, Ionic for the frontend and AngularFire to bootstrap the entire project. 

## Getting Started

## Run and Deploy
- To build and run the client side, `ionic serve -l` will do the trick. Visit [Ionic](ionicframework.com) for more information 
- To run the server side, `node index.js` will do the trick.
	- Sometimes you might want the program to run headlessly i.e without a terminal window open, `nohup node index.js & ` will give you that functionality. `nohup` keeps the terminal running even after logout and `&` just makes the job persistent in the background.
- To deploy the Firebase Cloud Functions, in the functions folder, run `firebase deploy --only functions`

## Features
- [ ] Detect motion and take image
- [ ] Enable/Disable Surveillance
- [ ] Enable/Disable Dark Hours (for lighting)
- [ ] Get properties of objects in image

## Coming Soon
- [ ] Object Analytics
	- [ ] Frequency of room entry
	- [ ] Object last location  

## Contributors
Tobi Akerele [@tobidae](https://tobiak.com) (contact@tobiak.com)
 
