
**Chatterbox** is a real-time chat platform where users can sign up, log in, and chat with each other.

## Features
- User authentication (Sign up & Login)
- Real-time messaging
- Redis and Celery integration for background tasks


## Tech Stack
- Django
- Redis
- Celery


## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/chatterbox.git
cd chatterbox


# Install this application
1. Activate redis by using this command - sudo service redis-server start
2. Activate Celery - celery -A Chatterbox worker --loglevel=info 
2. Run this application - python manage.py runserver 0.0.0.0:8000

# If you get any issue so please, you are ready to contribute on this project

