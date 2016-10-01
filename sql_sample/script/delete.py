from apps.models.blog import Blog, BlogAuthor, BlogEntry

def truncate():
    BlogEntry.objects.all().delete()
    print("truncate table Entry")
    Blog.objects.all().delete()
    print("truncate table Blog")
    BlogAuthor.objects.all().delete()
    print("truncate table Author")

def delete_by_pk():
    BlogEntry.objects.get(pk=1).delete()
    

