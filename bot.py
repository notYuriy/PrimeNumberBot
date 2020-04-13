import praw
from dotenv import load_dotenv
import os

load_dotenv()
reddit = praw.Reddit(client_id = os.getenv('PNB_CLIENT_ID'),
                     client_secret = os.getenv('PNB_CLIENT_SECRET'),
                     username = os.getenv('PNB_USERNAME'),
                     password = os.getenv('PNB_PASSWORD'),
                     user_agent = os.getenv('PNB_USER_AGENT'))

prime_number_daily = reddit.subreddit('primenumberdaily')

def next_prime(prime):
    n = prime + 1
    while not is_prime(n):
        n += 1
    return n

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def main():
    with open('last_prime.txt', 'r+') as f:
        prime = f.read()
        prime_number_daily.submit(prime, '')
        f.seek(0)
        f.truncate()
        f.write(str(next_prime(int(prime))))

if __name__ == '__main__':
    main()