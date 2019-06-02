# A SocialBlog Using Django Framework with MySQL Backend.


![Alt text](preview/Dj-MySQL.png?raw=true " ")


__PREVIEW:__

1.Index :

![Alt text](preview/1.Index.png?raw=true "Index")
> There are more in Preview Directory.


__To RUN the project:__

__Step 1:__ Open MySQL from Terminal :

```
$ mysql -u root -p

> DROP DATABASE IF EXISTS socialblog;
> CREATE DATABASE socialblog;
> USE socialblog;

```

__Step 2:__  Now open your Terminal with previously installed Virtual Environment and type-in :

```
$ pipenv shell
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py makemigrations
$ python manage.py migrate (Optional - Just to be Safe.)
$ python manage.py runserver 8080
```

__Step 3:__  Now open your Web-Browser and type-in :

```
http://127.0.0.1:8080/
```


> If you Like this project. Please don't forget to star it.
