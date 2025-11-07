# MaxWags Pet Walking Service by Rob Smith
___
### To skip the criterion sections, please use the links below
##### Criterion
- [LO1](#lo1) Using Agile to plan/design a Full-Stack app with Django
- [LO2](#lo2) Develop & implement a data model to query & manipulate data
- [LO3](#lo3) Implement authorisation, authentication & permissions
- [LO4](#lo4) Design, create, execute Full-Stack/Django testing
- [LO5](#lo5) Utilise GitHub & hosting services safely
- [LO6](#lo6) Deploy the web app using a cloud based platform ensuring security
- [LO7](#lo7) Demonstrate object-based concepts by implementing a custom model
- [LO8](#lo8) Leverage AI tools to orchestrate the software development process
___

**Insert blurb about the website**

![MAxWags device responsiveness screenshot](/maxwags/static/images/readme/devices-mockup.webp)

## LO1
#### Using Agile to plan/design a Full-Stack app with Django

### 1.1
##### Front-End Design

Initially there were 4 contrast errors, due to using roughly similar colours to Facebook (blue under white text), this caused an issue for colourblind users so a new colour scheme of green under white text was chosen.

<img src="/maxwags/static/images/readme/devices-mockup.webp" alt="responsiveness" style="width:100; height:300px"/>
<img src="/maxwags/static/images/readme/wireframe.webp" alt="wireframe" style="width:100; height:300px;"/>
<img src="/maxwags/static/images/readme/Wave-home.webp" alt="wireframe" style="width:100; height:300px;"/>
<img src="/maxwags/static/images/readme/Wave-posts.webp" alt="wireframe" style="width:100; height:300px;"/>
___

### 1.2
##### Database

A Postgres Database linked to Django to allow the management of data records with at least one custom model (included in the code snippet below).
```
class DogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dog_posts')
    image = CloudinaryField('image', default='placeholder')
    caption = models.CharField(max_length=120, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s post on {self.date_posted.strftime('%d-%m-%Y %H:%M:%S')}"
```
___

### 1.3 
##### Agile Methodology
The project was managed with AGILE in mind utilising a projectboard and user stories. The public project board can be found here: https://github.com/users/FollowRob/projects/10

<img src="/maxwags/static/images/readme/project-board.webp" alt="drawing" style="width:700px;"/>

___
### 1.4
##### Code Quality
Code quality can be assessed within the files within the repo however an example of custom Python logic with compound statements (from views.py) has been included below for brevity:

```
@login_required
def add_comment_view(request, post_id):
    post = get_object_or_404(DogPost, id=post_id)

    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(
                post=post,
                user=request.user,
                text=text,
            )
            messages.success(request, 'Comment added successfully.')
        else:
            messages.error(request, 'Comment cannot be empty.')
    return redirect('posts')
```
PEP8 standards were adhered to utilising the guidelines captured in the link below:
[Link to PEP8 guidelines](https://peps.python.org/pep-0008/)
___
### 1.5
##### Documentation
Initially my design philosophy was that the website would be tailed to everyone however that also just means it's specific to nobody so instead I went for a minimalistic design with similar design elements as Facebook, initially using a similar blue for the navbar with white text over the top. The idea here was that it would be minimal and easy for the elderly (high potential as clients) to use and navigate and that the similar colouring to facebook would be familiar and comfortable to a younger generation. 
However due to WAVE requirements the colour scheme had to be changed away from the "Facebook blue" to accomodate colourblind users and instead a relaxing green was chosen.

A UX design wireframe can be found in section: [LO1.1](#lo1) and a ERD for the Python logic can be found below:
<img src="/maxwags/static/images/readme/ERD.webp" alt="drawing" style="width:400px;"/>


[Back to links](#criterion)
___
## LO2

### 2.1
##### Database Development
The MaxWags app uses a relational database powered by PostgreSQL (via Django ORM).  
The schema includes three main models: `User`, `DogPost`, and `Comment`.

##### ERD
<img src="/maxwags/static/images/readme/ERD.webp" alt="drawing" style="width:300px;"/>

##### Model Definitions
```python
class User(AbstractUser):
    is_walker = models.BooleanField(default=False)

class DogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='dog_images/')
    caption = models.CharField(max_length=120)
    date_posted = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(DogPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
```

python manage.py makemigrations
python manage.py migrate
___
### 2.2
##### CRUD Functionality
The Comments model provides any registered user with full CRUD functionality on any posts.
Logged in users can create, view, edit and delete comments on staff posts.
Users can only edit or delete their own comments.
###### Model
```
class Comment(models.Model):
    post = models.ForeignKey(DogPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"
```
###### View
```
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(DogPost, id=post_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(post=post, user=request.user, text=text)
            messages.success(request, "Comment added successfully!")
    return redirect('posts')
```

| Operation | Description | Evidence |
|------------|--------------|-----------|
| Create | Users can submit a comment form under each post. | !<img src="/maxwags/static/images/readme/create-crud.webp"> |
| Read | Comments display below each post with username and date. | <img src="/maxwags/static/images/readme/read-crud.webp"> |
| Update | Comment authors can edit their own text. | <img src="/maxwags/static/images/readme/update-crud.webp"> |
| Delete | Comment authors can delete their own comments. | <img src="/maxwags/static/images/readme/delete-crud.webp">
 |
___
### 2.3
##### User Notifications
| Operation | Description | Evidence |
|------------|--------------|-----------|
| DogPost | Post created message | <img src="/maxwags/static/images/readme/post-create-message.webp"> |
| Logout | Logout message | <img src="/maxwags/static/images/readme/logout-message.webp"> |
| Comment | Comment deleted message | <img src="/maxwags/static/images/readme/comment-delete-message.webp"> |
| Comment | Comment updated message | <img src="/maxwags/static/images/readme/comment-update-message.webp">|
| Comment | Comment added message | <img src="/maxwags/static/images/readme/comment-add-message.webp"> |

Changes are fed to the user with real-time messages within the application, on the page that the change occurs on.
___
### 2.4
##### Forms and Validation
Max wags contains a form with validation for potential users to be able to register for an account.
They can still view posts and comments without an accounts but an account is needed to comment. 
Maxwags also contains a form to allow staff to upload posts - this page is not available to non-staff users and defaults back to the homepage.

| Operation | Description | Evidence |
|------------|--------------|-----------|
| Registration | Password validation | <img src="/maxwags/static/images/readme/password-validation.webp" style="width:350px;height:400px"> |
| Registration | Passwords not matching | <img src="/maxwags/static/images/readme/password-validation2.webp" style="width:350px;height:400px"> |
| Registration | Email validation | <img src="/maxwags/static/images/readme/email-validation.webp" style="width:350px;height:400px"> |
| Post creation | View logged in as staff | <img src="/maxwags/static/images/readme/staff-navbar.webp" > |
| Post creation | View logged in as non-staff | <img src="/maxwags/static/images/readme/nonstaff-navbar.webp"> |
| Post creation | Upload DogPost form | <img src="/maxwags/static/images/readme/post-form.webp" style="width:325px;height:300px"> |

[Back to links](#criterion)
___
## LO3

### 3.1
##### Role-Based Login and Registration
There are 3 roles on the Maxwags web application - a login for each role should have been supplied already

| Role | Description |
|------------|--------------|
| User | Able to login and create, edit and delete comments on posts |
| Walker | Same access as user but also able to upload posts |
| Superuser | Complete access to everything within the admin panel - delete any comment, post, user etc. |

| Role | Image |
|------------|--------------|
| User/Walker | <img src="/maxwags/static/images/readme/user-admin.webp" style="width:325px;height:300px"> |
| Superuser | <img src="/maxwags/static/images/readme/superuser-admin.webp" style="width:375px;height:290px"> |
___
### 3.2
##### Reflect Login State

| Status | Description | Evidence |
|------------|--------------|-----------|
| Logged in | Navbar when logged in | <img src="/maxwags/static/images/readme/navbar-loggedin.webp"> |
| Logged in | Comment function when logged in | <img src="/maxwags/static/images/readme/create-crud.webp"> |
| Logged out | Navbar when logged out | <img src="/maxwags/static/images/readme/navbar-loggedout.webp"> |
| Logged out | Comment message when logged out | <img src="/maxwags/static/images/readme/login-comment.webp"> |
___
### 3.3
##### Access Control
| Description | Evidence |
--------------|-----------|
| Non-registered users are unable to access the commands to comment on posts | <img src="/maxwags/static/images/readme/login-comment.webp"> |
| Users without is_walker permissions are unable to access the page to upload posts | <img src="/maxwags/static/images/readme/nonstaff-navbar.webp"> |
| Users without admin perms are unable to access the admin panel and are prompted to login with an admin account | <img src="/maxwags/static/images/readme/user-admin.webp"> |

[Back to links](#criterion)
___
## LO4

### 4.1
##### Python Test Procedures

Manual testing was chosen as there were a limited about of models making automated testing seem like overkill.

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Nav links | | | |
| | Click on Logo | Redirection to Home page | Pass |
| | Click on Posts link in navbar | Redirection to Posts page | Pass |
| | Click on Upload link in navbar | Redirection to Upload page (if user is Walker)| Pass |
| | Click on Logout link in navbar | Log out user | Pass |
| | Click on Login link in navbar | Redirection to Login page | Pass |
| | Click on Register link in navbar | Redirection to Register page | Pass |
| Posts Page | | | |
| | Click on Post button on post | Adds Entered comment onto specific post | Pass |
| | Click on Edit button on comment | Navigates to edit comment page | Pass |
| | Click on Delete button on comment | Navigates to delete comment page | Pass |
| Edit page |  |  |  |
| | Click on Save Changes | Saves the comment and navigates to Posts page | Pass |
| | Click on Cancel | Does not save the comment and navigates to Posts page | Pass |
| Delete page |  |  |  |
| | Click on Yes, delete | Deletes the comment and navigates to Posts page | Pass |
| | Click on Cancel | Does not delete the comment and navigates to Posts page | Pass |
| Register | | | |
| | Enter valid email address | Field will only accept email address format | Pass |
| | Enter valid password (twice) | Field will only accept password format | Pass | 
| | Click on Create Account button | Creates the account, logs in navigates to Posts page | Pass |
| Log In | | | |
| | Click Login button | Redirects user to Posts page and logs in (provded details are correct) | Pass |
| Log Out | | | |
| | Click Logout button | Logs out user, Redirects user to Home page | Pass |
| Footer | | | |
| | Click on the Facebook icon | Opens new broswer tab to Facebook homepage | Pass |
| | Click on the Instagram icon | Opens new broswer tab to Instagram homepage | Pass |
| | Click on the Twitter (X) icon |  Opens new broswer tab to Twitter homepage | Pass |
| Upload | | | |
| | Click Choose file button | Allows user to select an image from their PC | Pass |
| | Click Upload button | Uploads posts and redirects to Posts page | Pass |
| | Click Back to posts text button | Redirects to Posts page | Pass |

| Broswer | Image | Pass/Fail |
| --- | --- | --- |
| Chrome | <img src="/maxwags/static/images/readme/chrome.png" alt="drawing" style="width:300px;"/> | Pass |
| Brave | <img src="/maxwags/static/images/readme/brave.png" alt="drawing" style="width:300px;"/> | Pass |
| Safari| <img src="/maxwags/static/images/readme/safari.png" alt="drawing" style="width:300px;"/> | Pass |

___
### 4.2
##### JavaScript Test Procedures (if applicable)
Not applicable - no custom JavaScript added for project.
___
### 4.3
##### Testing Documentation
###### User stories completed

| User Story | Acceptance Criteria | Pass/Fail |
| --- | --- | --- |
| As a Guest, I want to view a welcoming home page so that I can learn what MaxWags is about and navigate the site easily. | Visiting “/” shows the home page with information about MaxWags’ dog walking services. | Pass |
| |The home page contains links to register, log in, and view posts. | Pass |
| | Navbar and footer appear consistently across all pages. | Pass |
| As a Guest, I want to browse dog posts so that I can see photos of dogs and their captions without signing up. | Visiting “/posts” shows a feed of all dog posts ordered by date. | Pass |
| | Each post shows the username, image, caption, and date posted. | Pass | 
| | Guests can view but not comment or upload posts. |  Pass | 
| As a Guest, I want to create an account so that I can log in and interact with the community. | Registration form collects username, email, and password. | Pass | 
|  | Form validates input and shows error messages for invalid or duplicate entries. | Pass |
| | On successful registration, the user is automatically logged in and redirected to the posts page. | Pass | 
| As a Registered User, I want to securely log in and log out so that I can access member features. | Users can log in using username and password. | Pass | 
| | Failed logins show a clear error message. | Pass | 
|   | Logging out redirects the user to the home page with a confirmation message. | Pass | 
| As a Walker, I want to upload a photo and caption of dogs I’ve walked so that owners can see their pets having fun. | Only users with is_walker=True can access the upload page. | Pass | 
| | Upload form includes an image and optional caption. | Pass | 
|  | Images are uploaded to Cloudinary, and posts appear instantly on the posts page. | Pass | 
| | Invalid files are rejected with a clear message. | Pass | 
| As a Registered User, I want to comment on posts so that I can engage with other users. | Authenticated users can add comments below posts. | Pass | 
|  |Comments show username, text, and timestamp. | Pass | 
| | Empty comments are rejected with an error message. | Pass | 
|  | Successful comments trigger a success message. | Pass | 
| As a Registered User, I want to edit or delete my own comments so that I can correct mistakes or remove unwanted messages. | Edit and delete options are visible only on comments by the logged-in user. | Pass | 
|  | Edited comments update immediately. | Pass | 
| | Deleted comments disappear from the post feed with a confirmation message.| Pass | 
| As an Admin, I want to assign or remove walker status so that I can control which users can upload dog posts. | Admin can toggle is_walker via the Django Admin panel. | Pass | 
|  | Only walkers see the “Upload” link in the navbar. | Pass | 
|  | Walker uploads appear the same as regular posts, linked to their account. | Pass | 
| As a User, I want the website to be easy to navigate and readable on all devices so that I can use it anywhere. | Layout uses Bootstrap 5 responsive grid system. | Pass | 
|  | Navbar collapses into a burger menu on mobile. | Pass | 
|  | Text maintains sufficient contrast and uses accessible font sizes. | Pass | 
| As a User, I want clear visual feedback when I take an action so that I know if it succeeded or failed. | Flash messages appear after registration, login, logout, post, and comment actions. | Pass | 
|  | Alerts are styled with Bootstrap and dismissible. | Pass | 
|  | Success, warning, and error messages use distinct colors. | Pass | 
| As a Developer, I want the MaxWags app deployed on Heroku with Cloudinary storage so that it’s accessible online. | The app runs successfully on Heroku using a managed Postgres database. | Pass | 
|  | Cloudinary handles all media uploads. | Pass | 
|  | Static files are served via WhiteNoise. | Pass | 
|  | Environment variables are used for secret keys and API credentials. | Pass | 

###### Python Linting
As a note on linting, only files edited personally were linted, standard files created by Django were ignored. 
| File name | Pass/Fail | Notes | Image |
| --- | --- | --- | --- |
| admin.py | Pass |  | <img src="/maxwags/static/images/readme/admin.png" style="width:350px"> |
| forms.py | Pass |  | <img src="/maxwags/static/images/readme/forms.png" style="width:350px"> |
| models.py | Pass |  | <img src="/maxwags/static/images/readme/models.png" style="width:350px"> |
| urls.py | Pass |  | <img src="/maxwags/static/images/readme/urls.png" style="width:350px"> |
| views.py | Pass |  | <img src="/maxwags/static/images/readme/views.png" style="width:350px"> |
| settings.py | Pass | Four errors on code generated by Django | <img src="/maxwags/static/images/readme/settings.png" style="width:8000px"> |

###### CSS Validation
| File name | Pass/Fail | Notes | Image |
| --- | --- | --- | --- |
| style.css | Pass |  | <img src="/maxwags/static/images/readme/CSS-valid.png" style="width:500px"> |

###### HTML Validation
| Page | Pass/Fail | Notes | Image |
| --- | --- | --- | --- |
| 404.html | Pass | 3 errors as validator doesn't like django template language | <img src="/maxwags/static/images/readme/html-valid-404.png" style="width:600px"> |
| 500.html | Pass | 3 errors as validator doesn't like django template language | <img src="/maxwags/static/images/readme/html-valid-500.png" style="width:600px"> |
| Home| Pass |  | <img src="/maxwags/static/images/readme/html-valid-home.png" style="width:600px"> |
| Posts | Pass |  | <img src="/maxwags/static/images/readme/html-valid-post.png" style="width:600px"> |
 Upload | Pass | 3 errors as validator doesn't like django template language | <img src="/maxwags/static/images/readme/html-valid-upload.png" style="width:600px"> |
| base.html | Pass | 3 errors as validator doesn't like django template language | <img src="/maxwags/static/images/readme/html-valid-base.png" style="width:600px"> |
| Register | Pass | Three Aria errors added because of the implementation of the Django Registration template | <img src="/maxwags/static/images/readme/html-valid-reg.png" style="width:600px"> |
| Login | Pass |  | <img src="/maxwags/static/images/readme/html-valid-login.png" style="width:600px"> |
| Edit Comment | Pass | 3 errors as validator doesn't like django template language | <img src="/maxwags/static/images/readme/html-valid-edit.png" style="width:600px"> |
| Delete Comment | Pass | 3 errors as validator doesn't like django template language | <img src="/maxwags/static/images/readme/html-valid-delete.png" style="width:600px"> |
| Logout | Pass | 2 errors as validator doesn't like django template language | <img src="/maxwags/static/images/readme/html-valid-logout.png" style="width:600px"> |


[Back to links](#criterion)
___
## LO5

### 5.1
##### Version Control with Git and GitHub
Satisfied witin GitHub repository:
https://github.com/FollowRob/MaxWags_Capstone_Project
___
### 5.2
##### Secure Code Management
Satisfied within GitHub repository and Heroku deployment:
https://github.com/FollowRob/MaxWags_Capstone_Project
https://capstone-maxwags-e4277e29559a.herokuapp.com/

[Back to links](#criterion)
___
## LO6

### 6.1
##### Deploy Application to Cloud Platform
- Add link toHeroku deployed project
- Add images where applicable
___
### 6.2
##### Document Deployment Process
The site was deployed on Heroku and connected to GitHub for version control. This was done by following the below steps:

- Log in to GitHub and create a new repository
- Sign up for Heroku and create a new account.
- Create a new app and choose a suitable region for deployment.
- In the app settings, go to config vars and click "reveal config vars".
- The app requires configuration for the following variables: SECRET_KEY, DATABASE_URL & CLOUDINARY_URL. Assign the corresponding values from the project's env.py to these variables.
- Integrate Heroku with GitHub by choosing the GitHub integration option in Heroku.
- Locate and select the GitHub repository.
- Choose manual deployment from the selected branch of the GitHub repository.
- Deploy by clicking the manual deploy button.
- Once deployed, the site is accessible through the live link provided at the top of the document.
___
### 6.3
##### Ensure Security in Deployment
Satisfied by in settings

[Back to links](#criterion)
___
## LO7

### 7.1
##### Design and Implement a Custom Data Model
- add code snippet of custom model

[Back to links](#criterion)
___
## LO8

### 8.1
##### Use AI tools to assist in code creation
___
### 8.2
##### Use AI tools to assist in debugging code
___
### 8.3
##### Use AI tools to optimise code for performance and user experience
___
### 8.4
##### Use AI tools to create automated unit tests
Instructed to ignore as manual testing is satisfactory.
___
### 8.5
##### Reflect on AI's role in the development process and it's impact on workflow
[Back to links](#criterion)
[Back to top](#maxwags_capstone_project)
