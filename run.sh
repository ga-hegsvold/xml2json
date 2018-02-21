docker stop xml2json
docker rm xml2json
docker run -d -p 5000:5000 --name xml2json xml2json
