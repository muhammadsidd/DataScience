'''
Created on Jul 10, 2017

@author: SummitWorks
'''

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.pymongo_test
posts = db.posts
post_data = {
    'title': 'Django Training',
    'content': 'Web Development',
    'author': 'Django DEvelopment Team',
    'duration': '10 days'
}
result = posts.insert_one(post_data) #insert_many()
print("data inserted...")
#print('One post: {0}'.format(result.inserted_id))