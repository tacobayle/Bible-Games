# Prerequisites

docker needs to be installed

# Build your environment

```
cd docker/compose ; docker build . -t alpine-python3 ; cd -
mongo_id=$(docker run -d -v /home/nic/shared/Bible-Games/json:/home mongo)
# use -p 27017:27017 if you want to expose port to localhost
mongo_name=$(basename $(docker inspect --format='{{.Name}}' $mongo_id))
#mongo_db=$(jq -r .db.Bible.name json/mongo.json)
#mongo_collection=$(jq -r .db.Bible.collection.name json/mongo.json)
docker exec -it $mongo_name /bin/bash -c 'cd /home ; mongoimport --db Bible --collection Books --type json --file books.json --jsonArray'
```

# Find the previous and next book

```
docker run -it --env MONGO_HOST=$mongo_name --env MONGO_PORT=27017 -v /home/nic/shared/Bible-Games/python:/home --link $mongo_name alpine-python3 /bin/bash -c 'python3 /home/games.py'
```

# Find the writer(s) of a book

```
docker run -it --env MONGO_HOST=$mongo_name --env MONGO_PORT=27017 -v /home/nic/shared/Bible-Games/python:/home --link $mongo_name alpine-python3 /bin/bash -c 'python3 /home/writers.py'
```
