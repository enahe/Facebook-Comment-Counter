import json
import requests
"""Facebook API"""

token = "EAAfadO0YRngBAMJKDs69mi6545wJaxk68BORAsIXjHxhYNyPnGZAzDcZANZBwBRP6uSEMsZBaHGVMS0x25cI579EqrpDRoSdbwuB8XFeALLRZAMOivR01paaZBr7pMA0JKX5rHMmVSZBufHoQgGuljUJgBA7XQ5cU9V9GZAUBNqlZAMsnC5ZBf8HD0wTDilVufMsOWcUNM5NMdwQZDZD"

myGroup = "https://graph.facebook.com/v3.2/368114830626879/?fields=feed%7Bcomments%2Cmessage%7D&access_token=" + token

myGroupData = requests.get(myGroup)

myGroupJSON = myGroupData.json()

print(myGroupJSON)
