import boto3
import os
import sys
import time


def getBrewReviews():
    dynamodb = boto3.client('dynamodb')
    table_data = dynamodb.scan(TableName='BrewReviews', Limit=10)
    brew_reviews = []

    for item in table_data['Items']:
        brew_rev = {
                'revid': item['revid']['S'],
                'name': item['name']['S'],
                'abv': item['abv']['S'],
                'rating': item['rating']['N'],
                'btype': item['type']['S'],
                'location': item['location']['S'],
                }
        brew_reviews.append(brew_rev)
    return brew_reviews


if __name__=="__main__":
    getBrewReviews()
