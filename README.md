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

Initially there were 4 contrast errors, due to using roughly similar colours to Facebook (blue under white text), this caused an issue for colourblind users so a new colour scheme of green under white text was chosen.

<img src="/maxwags/static/images/readme/devices-mockup.webp" alt="responsiveness" style="width:100; height:300px"/>
<img src="/maxwags/static/images/readme/wireframe.webp" alt="wireframe" style="width:100; height:300px;"/>
<img src="/maxwags/static/images/readme/Wave-home.webp" alt="wireframe" style="width:100; height:300px;"/>
<img src="/maxwags/static/images/readme/Wave-posts.webp" alt="wireframe" style="width:100; height:300px;"/>
___

### 1.2

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
The project was managed with AGILE in mind utilising a projectboard and user stories. The public project board can be found here: https://github.com/users/FollowRob/projects/10

<img src="/maxwags/static/images/readme/project-board.webp" alt="drawing" style="width:700px;"/>

___
### 1.4
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
Initially my design philosophy was that the website would be tailed to everyone however that also just means it's specific to nobody so instead I went for a minimalistic design with similar design elements as Facebook, initially using a similar blue for the navbar with white text over the top. The idea here was that it would be minimal and easy for the elderly (high potential as clients) to use and navigate and that the similar colouring to facebook would be familiar and comfortable to a younger generation. 
However due to WAVE requirements the colour scheme had to be changed away from the "Facebook blue" to accomodate colourblind users and instead a relaxing green was chosen.

A UX design wireframe can be found in section: [LO1.1](#lo1) and a ERD for the Python logic can be found below:
<img src="/maxwags/static/images/readme/ERD.webp" alt="drawing" style="width:400px;"/>


[Back to links](#criterion)
___
## LO2

### 2.1
This can only be satisfied by looking at the code
___
### 2.2
CRUD functionality fulfilled within the comments section, logged in users can:
- Create a comment on a post
- Read comments they/others have left
- Edit their own comments only
- Delete their own comments only
___
### 2.3
Changes are fed to the user with real-time messages within the application
- Add images of these feedback messages
___
### 2.4
This can be satisfied with the registration form and the post upload form
- upload images of each form with feedback messages

[Back to links](#criterion)
___
## LO3

### 3.1
- mention that there are 3 roles, user, staff and superadmin
- add image of the login pages and the django admin login page
___
### 3.2
- add image of the top right in the navbar of the username logged in
- add image of the top right nav bar with the login option
___
### 3.3
- add image of admin panel not allowing a user to access
- sidebyside images of the upload button not being available for users but available for walkers

[Back to links](#criterion)
___
## LO4

### 4.1
- Add table 1 - User stories and outcomes
- Add images for all of these
___
### 4.2
Not applicable - no custom JavaScript added for project.
___
### 4.3
- Add table 2 - Responsibility testing size - screenshot pass/fail
- Add table 3 - browser testing - chome, brave, safari
- Add images for all of these

[Back to links](#criterion)
___
## LO5

### 5.1
Satisfied with GitHub repository
___
### 5.2
Satisfied with GitHub repository

[Back to links](#criterion)
___
## LO6

### 6.1
- Add link toHeroku deployed project
- Add images where applicable
___
### 6.2
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
Satisfied by in settings

[Back to links](#criterion)
___
## LO7

### 7.1
- add code snippet of custom model

[Back to links](#criterion)
___
## LO8

### 8.1
___
### 8.2
___
### 8.3
___
### 8.4
___
### 8.5
[Back to links](#criterion)
[Back to top](#maxwags_capstone_project)
