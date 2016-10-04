from django.db import models

class BookAuthor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class BookPublisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(BookAuthor)
    publisher = models.ForeignKey(BookPublisher)
    publish_date = models.DateField()
    print_date = models.DateField()

class BookStore(models.Model):
    name = models.CharField(max_length=300)
    registered_users = models.PositiveIntegerField()
    hoge = models.CharField(max_length=100, default='fuga')

    class Meta:
        db_table = 'store'

class BookCascadeKey(models.Model):
    name = models.CharField(max_length=100)

class BookProtectKey(models.Model):
    name = models.CharField(max_length=100)

class BookSetNullKey(models.Model):
    name = models.CharField(max_length=100)

class BookSetDefaultKey(models.Model):
    name = models.CharField(max_length=100)

class BookSetKey(models.Model):
    name = models.CharField(max_length=100)

class BookDoNothingKey(models.Model):
    name = models.CharField(max_length=100)

class BookDeletion(models.Model):
    name = models.CharField(max_length=200)
    cascade_row = models.ForeignKey(BookCascadeKey, on_delete=models.CASCADE)
    protect_row = models.ForeignKey(BookProtectKey, on_delete=models.PROTECT)
    set_null_row = models.ForeignKey(BookSetNullKey,
                                     null=True,
                                     on_delete=models.SET_NULL)
    set_default_row = models.ForeignKey(BookSetDefaultKey,
                                        default=9,
                                        on_delete=models.SET_DEFAULT)
    set_key_row = models.ForeignKey(BookSetKey,
                                    default=10,
                                    on_delete=models.SET(11))
    do_nothing_row = models.ForeignKey(BookDoNothingKey, on_delete=models.DO_NOTHING)


