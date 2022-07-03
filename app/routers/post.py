from sqlalchemy import func
from app import oauth2
from .. import models, schemas
from fastapi import Depends, HTTPException, status, Response, APIRouter
from ..database import get_db
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

# @router.get("/", response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.PostOuts])
def get_posts(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    if posts is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "No posts available")
    return posts


@router.get("/{id}", response_model=schemas.PostOuts)
def get_post(id: int, db: Session = Depends(get_db)):
    the_post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).first()
    if the_post is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"post of id: {id} not found")
    return the_post


# @router.get("/myposts", response_model=List[schemas.Post])
# def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     # posts = db.query(models.Post).order_by("id").all()
#     posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
    
#     if posts is None:
#         raise HTTPException(
#             status_code = status.HTTP_404_NOT_FOUND, 
#             detail = "No posts available")
#     return posts


@router.post("/createposts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_dict = post.dict()
    new_post = models.Post(owner_id = current_user.id, **post_dict)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    

"""deleting a post by its id
"""
@router.delete("/delposts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)
    the_post = post.first()
    if post.first() is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"post of id: {id} not found")
    if the_post.owner_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, 
                            detail="Not authorized to perform the requested action")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/updateposts/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_dict = post.dict()
    the_post = db.query(models.Post).filter(models.Post.id == id)
    post = the_post.first()
    if the_post.first() is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"post of id: {id} not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, 
                            detail="Not authorized to perform the requested action")
    the_post.update(post_dict, synchronize_session=False)
    db.commit()
    return the_post.first()