from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid
from . import db

class Account(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(100), unique=True, nullable=False)
    access_token = db.Column(db.Text, nullable=False)
    instagram_account_id = db.Column(db.String(100), nullable=False)
    proxy_url = db.Column(db.String(255))
    daily_limit = db.Column(db.Integer, default=5)
    current_daily_posts = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), default='active')
    last_post_time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ContentFolder(db.Model):
    folder_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    path = db.Column(db.String(255), nullable=False)
    total_videos = db.Column(db.Integer, default=0)
    posts_per_week = db.Column(db.Integer, default=7)
    is_active = db.Column(db.Boolean, default=True)

class PostTask(db.Model):
    task_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    account_id = db.Column(db.String(36), db.ForeignKey('account.id'), nullable=False)
    video_path = db.Column(db.String(255), nullable=False)
    caption = db.Column(db.Text)
    folder_id = db.Column(db.String(36), db.ForeignKey('content_folder.folder_id'))
    scheduled_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='pending')
    attempts = db.Column(db.Integer, default=0)
    max_attempts = db.Column(db.Integer, default=3)
    media_id = db.Column(db.String(100))
    error_message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime) 