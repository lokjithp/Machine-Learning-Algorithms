import requests
url='http://localhost:9696/predict'
inputvalue={
    'iv':[1,2,3,4]
}
response=requests.post(url,json=inputvalue).json()
print(response)
