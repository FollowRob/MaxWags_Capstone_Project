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

| Operation | Description | Evidence |
|------------|--------------|-----------|
| Registration | Password validation | <img src="/maxwags/static/images/readme/password-validation.webp" style="width:350px;height:400px"> |
| Registration | Passwords not matching | <img src="/maxwags/static/images/readme/password-validation2.webp" style="width:350px;height:400px"> |
| Registration | Email validation | <img src="/maxwags/static/images/readme/email-validation.webp" style="width:350px;height:400px"> |

[Back to links](#criterion)
___
## LO3

### 3.1
##### Role-Based Login and Registration
- mention that there are 3 roles, user, staff and superadmin
- add image of the login pages and the django admin login page
___
### 3.2
##### Reflect Login State
- add image of the top right in the navbar of the username logged in
- add image of the top right nav bar with the login option
___
### 3.3
##### Access Control
- add image of admin panel not allowing a user to access
- sidebyside images of the upload button not being available for users but available for walkers

[Back to links](#criterion)
___
## LO4

### 4.1
##### Python Test Procedures
- Add table 1 - User stories and outcomes
- Add images for all of these
___
### 4.2
##### JavaScript Test Procedures (if applicable)
Not applicable - no custom JavaScript added for project.
___
### 4.3
##### Testing Documentation
- Add table 2 - Responsibility testing size - screenshot pass/fail
- Add table 3 - browser testing - chome, brave, safari
- Add images for all of these

[Back to links](#criterion)
___
## LO5

### 5.1
##### Version Control with Git and GitHub
Satisfied with GitHub repository
___
### 5.2
##### Secure Code Management
Satisfied with GitHub repository

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
___
### 8.5
##### Reflect on AI's role in the development process and it's impact on workflow
[Back to links](#criterion)
[Back to top](#maxwags_capstone_project)
