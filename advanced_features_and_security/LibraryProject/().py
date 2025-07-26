# coding: utf-8
user = CustomUser.objects.create_superuser(email="ogenna09@example.com", password="0987poiu", first_name="ogenna")
user
users = CustomUser.objects.all()
users
users = CustomUser.objects.get(id=1)
users
del(users)
users
user = CustomUser.objects.create_superuser(email="ogenna09@example.com", password="0987poiu", first_name="ogenna")
users = CustomUser.objects.all()
users
for user in users:
    if user.email__iexact="ogenna09@example.com":
        del(user)
users
del(users)
users
