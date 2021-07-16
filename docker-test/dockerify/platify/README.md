To run the project locally, run:
* `sudo docker-compose up -d --build`
then go to http://localhost:8000 for the website 
and http://localhost:5555 for the flower.

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

consumer Service can be useful in microservices. Another service produce a message 
in rabbitmq and this app consume it from there.


---- to test before pushing
* confirm that going on http://localhost:8000/fruit/register/ register a new task on http://localhost:5555/tasks
* confirm that periodic tasks are still running
* follow consumer service logs (sudo docker logs consumer -f) 
and confirm that when you go on http://localhost:8000/fruit/produce/, you have
the message reception log
* confirm that products api is working http://localhost:8000/api/product/
* confirm that you can upload files at http://localhost:8000/upload/

Features:
- docker architecture for deploy 
- nginx reverse proxy configuration, sub-domains & SSL: web, flower
- rest api structure with djangorestframework
- views also available
- files upload on server
- support for async jobs via celery
- support for messages consuming in micro services architecture
- basic user authentication system (email, password), verification emails, etc


Notes
* to connect to aws instance:
    * `ssh -i ~/.ssh/templatify_aws_instance.pem ec2-user@templatify.almeki.io`
    * to fix unprotected private key file warning:
        * `sudo chmod 600 ~/.ssh/templatify_aws_instance.pem`
    
* deploy prod
    * `docker-compose -f docker-compose.prod.yml up -d --build`
