# Dampingi REST API

This is a bare-bones of a Dampingi application providing a REST
API to a Dampingi Mobile Application.

The entire application is already deployed to GCP using Compute Engine >>> http://35.240.180.156/api/v1/

Here is instruction to run dampingi-backend in local

## Migrate Database

    python manage.py makemigrations
    python manage.py migrate

## Run the app

    python manage.py runserver

# REST API

The REST API to the dampingi app is described below. (wait for image to load)

![alt text](https://user-images.githubusercontent.com/43607241/120653690-238fa400-c4ab-11eb-9619-f97dafc5674b.jpg)

![alt text](https://user-images.githubusercontent.com/43607241/120653705-268a9480-c4ab-11eb-803c-7b9b120285f3.jpg)

# NOTES

## You can try our API by using this user : 

*username* = sandi123

*password* = sandi123

or u can register your own id to this link http://35.240.180.156/api/v1/jwtauth/register/

dont forget to update ur profile and add emergency contact to use our feature. Be sure to always put ur authorization token to call the API(except Register and login)


## dont forget to attach "/" in the end of the url

example : http://35.240.180.156/api/v1/token/ >> work
          
           http://35.240.180.156/api/v1/token >> won't work
