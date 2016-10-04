from myapp.models.blog import Blog
from . import util


def get_all_data():
    blog = Blog.objects.all()
    # util.print_all_field(blog)
    # print(blog.__dict__)
    print("search all data from table Blog")
    print(blog.values())


def get_data_by_pk(pk_val):
    if not pk_val:
        pk_val = 1
    blog = Blog.objects.get(pk=pk_val)
    print(blog.name, blog.tagline)


def get_data_by_self_column(col_val):
    # if not name or not val:
    #     name = "tagline"
    #     val = "taga"
    blog = Blog.objects.get(tagline=col_val)
    print(blog.name, blog.tagline)


def get_data_by_self_variable_column(col_name, col_val):
    # if not name or not val:
    #     name = "tagline"
    #     val = "taga"
    blog = Blog.objects.get(**{col_name: col_val})
    print(blog.name, blog.tagline)

