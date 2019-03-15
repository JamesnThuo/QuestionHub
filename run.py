import os
from app import create_app

application = create_app(os.getenv("APP_SETTING"))

if __name__ == '__main__':
  application.run()