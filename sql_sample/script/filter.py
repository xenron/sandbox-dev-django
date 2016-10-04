from myapp.models.blog import Blog
from . import util


def filter_data_by_self_column(col_val):
    # if not name or not val:
    #     name = "tagline"
    #     val = "taga"
    blogs = Blog.objects.filter(tagline=col_val)
    if len(blogs):
        for blog in blogs:
            print(blog.name, blog.tagline)


def filter_data_by_self_variable_column(col_name, col_val):
    # if not name or not val:
    #     name = "tagline"
    #     val = "taga"
    blogs = Blog.objects.filter(**{col_name: col_val})
    if len(blogs):
        for blog in blogs:
            print(blog.name, blog.tagline)


def filter_data_by_lookup_type(col_name, lookup_type, col_val):
    
    Blog.objects.filter(name__exact='beatles blog')
    Blog.objects.filter(name__exact=['beatles blog', 'title'])
    
    Blog.objects.filter(name__iexact='beatles blog')
    Blog.objects.filter(name__iexact=['beatles blog', 'title'])
    Blog.objects.filter(name__iexact=None)
    
    Blog.objects.filter(name__startswith='beatles')
    Blog.objects.filter(name__startswith=['beatles', 'title'])
    
    Blog.objects.filter(name__istartswith='beatles')
    Blog.objects.filter(name__istartswith=['beatles', 'title'])
    
    Blog.objects.filter(name__endswith='blog')
    Blog.objects.filter(name__endswith=['blog', 'title'])
    
    Blog.objects.filter(name__iendswith='blog')
    Blog.objects.filter(name__iendswith=['blog', 'title'])
    
    Blog.objects.filter(name__contains='blog')
    Blog.objects.filter(name__contains=['blog', 'title'])
    
    Blog.objects.filter(name__icontains='blog')
    Blog.objects.filter(name__icontains=['blog', 'title'])
    
    blogs = Blog.objects.filter(**{col_name+"__"+lookup_type: col_val})
    if len(blogs):
        for blog in blogs:
            print(blog.name, blog.tagline)





