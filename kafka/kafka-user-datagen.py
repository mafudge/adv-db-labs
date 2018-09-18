import json
import datetime
import random
import uuid
import time
from kafka import KafkaProducer
user_list = [ 
    { 'name': 'abby', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'bob', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'chris', 'gender' : 'female', 'level' : 'premium' },
    { 'name': 'devin', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'elle', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'fred', 'gender' : 'male', 'level' : 'premium' },
    { 'name': 'gigi', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'hank', 'gender' : 'male', 'level' : 'premium' },
    { 'name': 'ida', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'karley', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'lisa', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'mike', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'nancy', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'otto', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'patty', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'quinn', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'rose', 'gender' : 'female', 'level' : 'premium' },
    { 'name': 'surah', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'tosh', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'vaibhav', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'walt', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'xavier', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'yolanda', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'zeke', 'gender' : 'male', 'level' : 'premium' }
]

producer = KafkaProducer(bootstrap_servers='localhost:29092')
for user in user_list:
    encoded = json.dumps(user).encode('utf-8')
    #print("%d:%s" % (id,json.dumps(data)))
    print(encoded)
    producer.send('atmusers',encoded)

producer.close()