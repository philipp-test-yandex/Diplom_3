import time
import random

def generate_user_data():
    timestamp = int(time.time() * 1000)
    return {
        "email": f"user{timestamp}@test.com",
        "password": "Test123",
        "name": f"TestUser{random.randint(1000,9999)}"
    }