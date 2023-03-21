from flask import Flask, render_template
from datetime import datetime, timezone, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///reddit_posts.db')
session = sessionmaker(bind=engine)
Base = declarative_base()

class Post(Base):
    __tablename__ = 'reddit_posts'
    id =('id',primary_key=True)
    title = ('title')
    score = ('score')
    permalink =('permalink')
    created_at =('created_at')
app = Flask(__name__)

@app.route('/')
def index():
    session = session()
    current_time = datetime.now(timezone.utc)
    start_date = datetime(current_time.year, current_time.month, current_time.day, tzinfo=timezone.utc)
    end_date = start_date + timedelta(days=1)
    top_post = session.query(Post).filter(Post.created_at >= start_date, Post.created_at < end_date).order_by(Post.score.desc()).first()
    session.close()
    return render_template('index.html', top_post=top_post)

post = Post()
post.id = 1
post.title = 'My first post'
post.score = 100
post.permalink = 'https://www.reddit.com/r/mysubreddit/comments/12345/my_first_post'
post.created_at = datetime.now()

session.add(post)
session.commit()
