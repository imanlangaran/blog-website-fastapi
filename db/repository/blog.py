from sqlalchemy.orm import Session
from db.models.blog import Blog
from res_models.blog import CreateBlog

def list_blogs(db:Session):
    return db.query(Blog).filter(Blog.is_acvite==True).all()
    

def create_new_blog(blog:CreateBlog, db:Session, author_id:int):
    blog = Blog(**blog.dict(), author_id =author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def retreive_blog(id:int, db:Session):
    return db.query(Blog).filter(Blog.id==id).first()
