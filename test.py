import json
import requests
"""Facebook API"""

token = "EAAfadO0YRngBAGdvwpvhxzPpHNg7TB8ELqlKXIFeIZA2yu4mcn0TBNmhvpCnpiJxC6PMZCOk6C5RlAogFN55TSFUAbhslyftfXZAYObXzCHdwzsuDzQLF6LhLlptnrR236uMtwAUY9uROgB6P1rGsoJfVCGAZCXoT7S8WZBtB50FQxHAbyj0EGk9erc2hVArqOjbXVYewmQZDZD"
myGroup = "https://graph.facebook.com/v3.2/368114830626879/?fields=feed%7Bcomments%2Cmessage%7D&access_token=" + token

myGroupData = requests.get(myGroup)

myGroupJSON = myGroupData.json()

myGroupComments = {}

for x in myGroupJSON["feed"]["data"]:
        if (x.get('message') is not None) & (x.get('comments') is not None):
                for i in x.get('comments')["data"]:
                        if "wow" in i.get("message"):
                                if x.get('message') not in myGroupComments:
                                        myGroupComments[x.get('message')] = []
                                myGroupComments[x.get('message')].append(i.get('from').get('name'))
print(myGroupComments)

