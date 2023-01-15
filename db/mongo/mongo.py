import json

import pandas as pd
import pymongo
import requests

client = pymongo.MongoClient("mongodb://rmoorind:<R@i$eL2023%/$>@clusterrmind-shard-00-00.bxe4l.mongodb.net:27017,clusterrmind-shard-00-01.bxe4l.mongodb.net:27017,clusterrmind-shard-00-02.bxe4l.mongodb.net:27017/?ssl=true&replicaSet=atlas-7hup09-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
