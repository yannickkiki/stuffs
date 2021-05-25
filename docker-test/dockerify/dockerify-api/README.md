To run the project locally in a docker container:

    * sudo docker-compose up


- Fix the issue with containers sync
- Add migrate to the process:
  (sudo docker exec -it {container_name} python manage.py migrate) could work
  