from django.db import models

class Product(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50)
    cat=models.CharField(max_length=50, default='')
    subcat=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    price=models.IntegerField(default=0)
    img=models.ImageField(upload_to="shop/images", default='')
    pub_date=models.DateField()
    discount=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Orders(models.Model):
    id= models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,default=" ")
    items_json= models.CharField(max_length=5000)
    fname=models.CharField(max_length=90)
    lname=models.CharField(max_length=90,default=" ")
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    country=models.CharField(max_length=50,default="India")
    zip_code=models.CharField(max_length=111)
    update1=models.CharField(max_length=100,default=" ")
    update2=models.CharField(max_length=100,default=" ")
    update3=models.CharField(max_length=100,default=" ")
    

class Contactdata(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=50)

    def __str__(self):
      return self.email

