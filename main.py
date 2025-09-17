from fastapi import FastAPI

# create an instance of fastAPI...

app = FastAPI()


@app.get('/')
def sayhello():
    return {
        'data':{
            'name':"Shailesh Thorat",
            'age':'22',
            'gender':'Male'
        },
        'status':200
    }

'''
Dekh bhai FastAPI ekdm fast hai ekdm rocket jaise 🚀😁
Bass 4 steps mein tera API banke ready to give response...
1) Import FastAPI
2) Create an instance
3) define a route
4) define a function just below it
And boom you've made your first FastAPI
'''
