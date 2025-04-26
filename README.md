# personal_blog

## Project overview
This project includes a blog view and management with multiple user types. Different user type can perform different tasks in the blog page.  
A quick overview of user types:  
| Type | Access |
| --- | --- |
| Visitors | Visitors are non-logged in users who enter the site. The blog pages 'Home', 'All Posts', 'About', and 'Contact' can be viewed by any person accessing the website, while it also contains a log-in and sign-up section. |
| Users | Any person can create an account. Logged-in users are able to comment on posts, bookmark posts, like posts, and change their profile picture and description. |
| Authors | Authors can add new posts with picture and SEO-relevant information to the blog, besides being able to perform all actions registered users can perform. |
| Admins | Admins can edit blog posts, manage (block/edit) users of types User and Author, besides being able to perform all actions registered users can perform.|
| Super-Admin | Super-admin can perform all tasks that Admins can, as well as being able to edit and block accounts of other admin users. |

## Installation
1. Clone the repo
2. Create virtual environment, `python -m venv myenv`.
3. Activate the virtual environment.  
On Mac/Linux, `source myenv/bin/activate`.  
On Windows, `myenv\Scripts\activate`  
4. To install all the dependencies listed in a requirements.txt file, run:  
`pip install -r requirements.txt`
