from apps.models.blog import Blog, Author, Entry

def truncate():
    Entry.objects.all().delete()
    Blog.objects.all().delete()
    Author.objects.all().delete()

def delete_by_pk():
    Entry.objects.get(pk=1).delete()
    

