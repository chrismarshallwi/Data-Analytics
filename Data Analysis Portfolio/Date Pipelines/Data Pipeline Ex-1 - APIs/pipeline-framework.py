#EXTERNAL API --> POSTGRES DATABASE 
#PYTHON SCRIPT

#PART 1: API (THIS IS A MOCK API, NOT REAL DATA)

#This file cretes a fake API (replication) that gathers fake transactional data
#The following script demonstrates the following:

#1 API build
#2 Flask 
#3 Date Pipelines

from flask import Flask, Response, stream_with_context

import time
import uuid
import random

import requests
import psycopg2 as pg2

APP = Flask(__name__)

@APP.route('/very_large_request/<int:rowcount>', methods=['GET'])

def get_large_request(rowcount):
    def f():
        for _i in range(rowcount):
            time.sleep(.01)
            txid = uuid.uuid4()
            uid = uuid.uuid4()
            amount = round(random.uniform(-1000,1000),2)

            yield f"('{txid}', '{uid}'', {amount})\n"
    return Response(stream_with_context(f()))

if __name__ == "__main__":
    APP.run(debug=True)



