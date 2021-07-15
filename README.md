# Prerequisites

docker needs to be installed

# run the app

```
cd docker/compose
docker build . -t alpine-python3
cd -
docker run -d -v /home/nic/shared/Bible-Games/json:/home --name mongo mongo # use -p 27017:27017 if you want to expose port to localhost
docker exec -it mongo /bin/bash -c 'cd /home ; mongoimport --db Bible --collection Books --type json --file books.json --jsonArray'
docker run -it -v /home/nic/shared/Bible-Games/python:/home --link mongo alpine-python3 /bin/bash -c 'python3 /home/game.py'
```