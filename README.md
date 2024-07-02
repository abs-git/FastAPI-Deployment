## FastAPI-Deployment

![Untitled](https://user-images.githubusercontent.com/48580174/213379888-870d4879-81bd-4716-adfa-3b6aaea1cdda.png)


### AWS

```shell

export name=donghyun-fastapi
export ecr=936433886933.dkr.ecr.ap-northeast-2.amazonaws.com

# aws login
aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 

# docker build
# ECR의 레포지토리 이름과 build 되는 image의 이름을 같아야 됨.
docker build -t $name -f test.Dockerfile .

# image push
docker tag $name:latest $ecr/$name:latest
docker push $ecr/$name:latest

# remove build image
docker rmi -f $name:latest
docker rmi -f $ecr/$name:latest

# image pull
docker pull $ecr/$name:latest

# run
docker run -dit -p 8000:8080 --name donghyun-fastapi $ecr/$name:latest

```


### Quick start

```shell

# local test
cd FastAPI-Deployment/fastapi-docker
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080


# docker test
cd FastAPI-Deployment/fastapi-docker
docker build -t donghyun-fastapi -f api.Dockerfile .
doker run -dit -p 8000:8080 --name donghyun-fastapi donghyun-fastapi

# docker compose test
cd FastAPI-Deployment/fastapi-docker
docker-compose up -d

```