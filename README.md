# AppSync Graphql Server

## To install dependencies

`yarn`

## To run in offline mode

`yarn offline`

This will also create a local instance of dynamodb. You can access a shell for this by going to http://localhost:8000

## To run the tests
You will (probably) need python 3 and you will need the offline server running. From the root directory

```
python3.6 -m venv test
source test/bin/activate
cd test 
pip install -r requirements.txt
python3.6 collection_test.py
```

There are better ways than running a test one at a time but we can look at those later. 
