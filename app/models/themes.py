from app.extensions import db

class Blog_Theme(db.Model):
    __tablename__ = "blog_theme"
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(30), nullable=False)
    picture = db.Column(db.String(700), nullable=False)
    picture_source = db.Column(db.String(700))
    # One-to-many relationship:
    # One theme → many blog posts
    # Creates a posts attribute on each Blog_Theme object (a list of related Blog_Posts)
    # Creates a theme_group attribute on each Blog_Posts object (a reference to its Blog_Theme)
    posts = db.relationship('Blog_Posts', backref='theme_group')

    def __repr__(self):
        return f"<Theme: {self.id} {self.theme}>"
