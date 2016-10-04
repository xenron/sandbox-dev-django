from myapp.models.blog import Blog
from . import util


def filter_data_by_filter_self_column(col_val):
    # if not name or not val:
    #     name = "tagline"
    #     val = "taga"
    blogs = Blog.objects.filter(tagline=col_val)
    if len(blogs):
        for blog in blogs:
            print(blog.name, blog.tagline)


def filter_data_by_filter_self_variable_column(col_name, col_val):
    # if not name or not val:
    #     name = "tagline"
    #     val = "taga"
    blogs = Blog.objects.filter(**{col_name: col_val})
    if len(blogs):
        for blog in blogs:
            print(blog.name, blog.tagline)
