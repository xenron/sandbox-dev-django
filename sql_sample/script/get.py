from apps.models.blog import Blog
import util

def get_all_data():
    blog = Blog.objects.all()
    # util.print_all_field(blog)
    # print(blog.__dict__)
    print(blog.values())


def get_data_by_pk():
    blog = Blog.objects.get(pk=1)
    print(blog)


