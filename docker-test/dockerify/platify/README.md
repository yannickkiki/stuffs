To run the project locally, run:
* `sudo docker-compose up -d --build`
then go to http://localhost:8000.

Given that everything is installed in the docker container, no need to 
install anything on your machine. You can just edit the code, and you will 
see the changes on the dev server running (at http://localhost:8000 here) 
because this folder content is bound to the folder copy in the container.
However, sometimes in developing you might want to run some commands such as 
* `python manage.py startapp upload` but it requires you to have Django
installed. 
In such cases, you can run the commands directly inside the container 
and (since the folders are bound), the changes will reflect in this folder also.
Example:
* `sudo docker-compose exec web python manage.py startapp upload`
If you have permission issues with files created from the container, you can
fix it by giving permissions to the host user for now:
* `sudo chown -R $USER:$USER upload` in our case for the `upload` folder
The docker conf will be updated to avoid these permissions issues soon.

Some useful links:
* https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
* https://gist.github.com/yannickkiki/f7f894541aca8ff56bb544176f0e0439
* https://hub.docker.com/r/jwilder/nginx-proxy
* https://hub.docker.com/r/nginxproxy/acme-companion


Draft
Dev
* python manage.py runserver
* celery worker --beat --app config.celery_app --loglevel info
* celery flower --app config.celery_app --loglevel info
