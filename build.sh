docker stop xml2json
docker rm xml2json
docker rmi xml2json
docker rmi gamh/xml2json
docker build -t xml2json .
docker tag xml2json:latest gamh/xml2json:latest
# docker push gamh/xml2json:latest
