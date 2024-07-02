## FastAPI-Deployment

![Untitled](https://user-images.githubusercontent.com/48580174/213379888-870d4879-81bd-4716-adfa-3b6aaea1cdda.png)


### Setting

```shell

aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 936433886933.dkr.ecr.ap-northeast-2.amazonaws.com

docker build -t test-app -f test.Dockerfile .
docker tag test-app:latest 936433886933.dkr.ecr.ap-northeast-2.amazonaws.com/test-app:latest

docker push 936433886933.dkr.ecr.ap-northeast-2.amazonaws.com/test-app:latest

docker pull 936433886933.dkr.ecr.ap-northeast-2.amazonaws.com/test-app:latest

```



### Quick start

```shell

cd FastAPI-Deployment/fastapi-docker
docker-compose up -d
docker images                 # check the images
docker ps                     # check the containers
docker-compose up -build      # rebuild

# without docker-compose
docker build -t [container_name] .
docker run -p 8000:8080 [REPOSITORY]:[TAG]

```
