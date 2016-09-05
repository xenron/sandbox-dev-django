from apps.models.blog import Blog, Author, Entry

def truncate():
    Entry.objects.all().delete()
    print("truncate table Entry")
    Blog.objects.all().delete()
    print("truncate table Blog")
    Author.objects.all().delete()
    print("truncate table Author")

def delete_by_pk():
    Entry.objects.get(pk=1).delete()
    

