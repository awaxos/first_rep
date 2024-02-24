# import csv
# # import json
# import requests
#
# url = 'https://jsonplaceholder.typicode.com/posts'
# data = requests.get(url).json()
#
# headers = data[0].keys()
#
# field = 'posts'
#
# with open(field, 'w') as posts:
#     writer = csv.DictWriter(posts, fieldnames=field)
#     writer.writeheader()
#     writer.writerows()
