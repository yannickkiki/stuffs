To run the project locally in a docker container:

    * sudo docker build --tag dockerify-api .
    * sudo docker run --detach --publish 8000:8000 --volume "$(pwd):/app" dockerify-api
