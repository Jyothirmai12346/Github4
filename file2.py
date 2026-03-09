import requests
api_url="https://api.github.com/orgs/google/repos"
res=requests.get(api_url)
repos=res.json()
print("Google open source repositories")
for repo in repos:
  name = repo["name"]
  description = repo["description"]
  url = repo["url"]
print("Repository name:",name)
print("Description:",description)
print("Url:",url)
print("/" * 10)
