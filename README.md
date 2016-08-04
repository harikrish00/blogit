# Blogit (Multi User Blog)

# How to Run

Pre-Requisite: Please download google appengine SDK and install on your laptop
Link: https://cloud.google.com/appengine/downloads

1. Clone the repository on your laptop
1. cd into your newly cloned repository directory
1. Issue the following command

`dev_appserver.py .`

this will bring the application on localhost post 8080
4. Go to your browser and type `http://localhost:8080`

# Application Functionality and Navigation

## Anonymous User
* New user can sign up from /blog/signup or click `Sign In` link from main page navigation and `Sign up` link is presented on the login page
* Unauthenticated user can read the blogs

## Authenticated User
* Can create new posts from /blog/newpost or clicking on `New Post` link from main nav which is displayed only for logged in user
* Can edit/delete his/her own posts from the link provided on the post itself
* Can Like others post (But one like per post)
* Can comment on others post (Can comment number of times)
* Can navigate to permalink of a post
* Can view `My Posts` from the main nav
* Can not like his/her own posts
* Can not edit or delete others posts

# Live Online Blog

Above application is deployed and available for review here
http://blogit-1380.appspot.com


# Front End
* Used boostrap themes
* Custom styles throush styles.css

# Backend
* Python
* WebApp2 (Google appengine sdk)
* Google Datastore


