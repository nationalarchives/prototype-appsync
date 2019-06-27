import unittest
import boto3
import requests


class TestCollections(unittest.TestCase):

    def setUp(self):
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000", aws_access_key_id='test',
                                  aws_secret_access_key='test')

        table = dynamodb.Table('CollectionFilesTest')
        table.put_item(TableName='CollectionFilesTest',
                       Item={"id": "76ac79c8-4619-4ca2-8cac-747d8fecfe37", "name": "collection name"})

    def test_upper(self):
        query = """
                query GetCollection{
                  getCollection(id: "76ac79c8-4619-4ca2-8cac-747d8fecfe37"){
                      id,name
                  }
        }
            """

        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" \
                ".eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ" \
                ".SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c "
        headers = {'Authorization': token}
        url = "http://localhost:62222/graphql"
        response = requests.post(url, json={"query": query}, headers=headers)
        json_response = response.json()
        self.assertEqual(json_response['data']['getCollection']['name'], "collection name")


if __name__ == '__main__':
    unittest.main()
