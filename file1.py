import requests
url = "https://api.github.com/orgs/microsoft/repos"
response=requests.get(url)
repos=response.json()
print(" Microsoft open source repositories")
for repo in repos:
  name = repo["name"]
  description = repo["description"]
  url = repo["url"]
  print("Repository name :",name)
  print("Description:",description)
  print("url:",url)
  print("-" * 10)