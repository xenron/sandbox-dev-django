from apps.models import blog as blog_model

def create_new_blog():
    pass


def initial_data():
    blog = blog_model.Blog(name='name', tagline='taga')
    blog.save()
    print("initital table Blog")
    author1 = blog_model.BlogAuthor(name='tom', email='tom@hotmail.com')
    author1.save()
    author2 = blog_model.BlogAuthor(name='jerry', email='jerry@hotmail.com')
    author2.save()
    print("initital table Author")
    entry = blog_model.BlogEntry(blog=blog, headline='', body_text='', pub_date='2016-01-01', mod_date='2016-01-01', n_comments=1, n_pingbacks=2, rating=3)
    entry.save()
    entry.authors.add(author1, author2)
    entry.save()
    print("initital table Entry")

