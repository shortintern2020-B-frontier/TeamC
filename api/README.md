### Set up
```
docker-compose up
mysql -u root -h 127.0.0.1 -P 13306 -p
source path/to/init.sql
pip install -r requirement.txt
```

### Run
```
uvicorn main:app --reload
```