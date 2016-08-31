from apps.models import Blog

def get_test():
    blog = Blog.objects.all()
    print(blog)