from fastapi import FastAPI
from pydantic import BaseModel

# create an instance of fastAPI...
app = FastAPI()

'''
Dekh bhai FastAPI ekdm fast hai ekdm rocket jaise 🚀😁
Bass 4 steps mein tera API banke ready to give response...
1) Import FastAPI
2) Create an instance
3) define a route
4) define a function just below it
And boom you've made your first FastAPI
'''



# Model for incoming request made via Pydantic
class BlogPost(BaseModel):
    title:str
    content:str

@app.get('/')
def index():
    return {
        'data':f"Hello from the index file!"
    }

@app.get('/bloglist')
def showblogs(limit,published):
    if published:
        return {
        'data':f"Fetched {limit} published blogs from the db"
    }
    else:
        return {
        'data':f"Fetched {limit} blogs from the db"
    }




@app.get('/blog_post/unpublished')
def show_unpublished_blogs():
    return{
        'data': "all unpublished blogs"
    }


# Handling incoming request bodies and creating new resource.
@app.post('/blog')
async def create_blog(blog:BlogPost):
    return{
        'data':f"Blog created with title : {blog.title} and content : {blog.content}"
    }


# for creating dynamic routes...
# Code is executed line by line so route match mismatches, and thus always prefer to keep your dynamic route at the end.
@app.get('/blog_post/{id}')
def show_blog_posts(id:int):
    return {
        'data':id
    }



