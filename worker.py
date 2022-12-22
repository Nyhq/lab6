from flask import Flask
from flask import request
import requests
import os
import json
app = Flask(__name__)

def get_api_key() -> str:
    secret = os.environ.get("COMPUTE_API_KEY")
    if secret:
        return secret
    else:
        #local testing
        with open('.key') as f:
            return 'ya29.a0AX9GBdXd99tV2oY34GFPqvWFgeJxCff7GyskA2pxSVsIDQdiVediv9uWBPrLlpYcgLxbA9ZQqNWEhLnKLLMMsnaXlTU_5emSLdxopST7iN3ZqKqFJZBG7Ih4ek0zqq7sMon4NeTevos-Yz_aPfuemu2sLMHNsDOh-BFfk8gyamERQsP85-bB_KUqClLInOdGqqnUs-qkNJno8DQy-n8bDP2lJWuqWu5UBqsrGgaCgYKAWMSARESFQHUCsbCy30x3SLlW5Rk5gsDVM-cwQ0237'
      
@app.route("/")
def hello():
    return "Add workers to the Spark cluster with a POST request to add"

@app.route("/test")
def test():
    #return "Test" # testing 
    return(get_api_key())

@app.route("/add",methods=['GET','POST'])
def add():
  if request.method=='GET':
    return "Use post to add" # replace with form template
  else:
    token=get_api_key()
    ret = addWorker(token,request.form['num'])
    return ret


def addWorker(token, num):
    with open('payload.json') as p:
      tdata=json.load(p)
    tdata['name']='slave'+str(num)
    data=json.dumps(tdata)
    url='https://www.googleapis.com/compute/v1/projects/fluid-door-304916/zones/europe-west2-c/instances'
    headers={"Authorization": "Bearer "+token}
    resp=requests.post(url,headers=headers, data=data)
    if resp.status_code==200:     
      return "Done"
    else:
      print(resp.content)
      return "Error\n"+resp.content.decode('utf-8') + '\n\n\n'+data



if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
