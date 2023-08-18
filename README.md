# A Blog Managment System using FastAPI and Jinja

#### This repository was for practice in FastApi, and it is under development

## Home Page
![main page photo](/pics/MainPage.png)
this is a picture of the Web App's home page. [Routes](#routes)

## Routes
We have following routes until now:<br>
1. Blog routes :
    1. "/" Which redirects to ["/blog"](#home-page).
    2. ["/blog"](#home-page) : This page shows all activated blogs.
    3. ["/blog/{id: int}"](#detailed-blog) : This route retrieves a single blog from DB and returns a detailed page of it.
    4. ["/blog/create_new_blog"](#new-blog) : This route gives a title and content for a new blog - the user should log in to create a new blog.
    5. "/blog/delete/{id}" : it deletes the blog if the author user had logged in.
2. User routes :
    1. ["/register"](#register-new-user) : in this form, the user can enter his email and password which will be validated data - and the hashed password would be stored in DB.
    2. ["/login"](#login-user) : the user will enter his login data and an access token will save in his browser cookies which will be used to authorize the user.
    3. "/logout" : this route will save another access token, an expired token, so the user would log out.


## Picures
### Detailed Blog
![Detailed Blog](/pics/detailed%20page.png)
Detailed View of a Blog. [Routes](#routes)
### New Blog
![New Blog](/pics/new%20blog.png)
Create New Blog. [Routes](#routes)
### Register New User
![Register New User](/pics/register.png)
Register New User. [Routes](#routes)
### Login User
![Login User](/pics/login.png)
Login Registered User. [Routes](#routes)
