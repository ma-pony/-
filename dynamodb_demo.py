import logging
from datetime import datetime

import boto3
from boto3.dynamodb.conditions import Attr

region_name = "ap-southeast-1"
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class DynamoDb:
    def __init__(self, table_name: str):
        self.table = None
        self.table_name = table_name

    def start_client(self):
        dynamodb = boto3.resource("dynamodb", region_name=region_name)
        self.table = dynamodb.Table(self.table_name)


class Db(DynamoDb):


    def get_data(self, name: str):
        response = self.table.get_item(
            Key={
                'name': name
            }
        )
        logger.info(f"get data: {response}")
        return response.get('Item')

    def update_data(self, name: str, age: str):
        response = self.table.update_item(
            Key={
                'name': name
            },
            UpdateExpression='SET date = :val1, age = :val2',
            ExpressionAttributeValues={
                ':val1': datetime.today().strftime("%Y-%m-%d"),
                ':val2': str(age)
            }
        )
        logger.info(f"update data: {response}")
        
    def put_data(self, name: str):
        response = self.table.put_item(
            Item={
                "name": name,
                "date": datetime.today().strftime("%Y-%m-%d")
            }
        )
        logger.info(f"put data: {response}")
        return response
        
    def scan_data(self, date: str):
        response = self.table.scan(
            FilterExpression=Attr("date").contains(date)
        )
        logger.info(f"scan data: {response}")
        return response['Items']
        
    def delete_data(self, name: str):
        response = self.table.delete_item(
            Key={
                'name': name
            }
        )
        logger.info(f"delete data: {response}")
        return response
