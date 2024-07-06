import requests
import time
import os

def ping_url(url,delay,max_trials):
    trials = 0
    while(trials < max_trials):
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            time.sleep(delay)
            trials+=1
    return False

def run():
    url = os.getenv('INPUT_URL')
    delay = os.getenv('INPUT_DELAY')
    max_trials = os.getenv('INPUT_MAX_TRIALS')

    if ping_url(url,delay,max_trials) == False:
        raise Exception

    


            


if __name__ == '__main__':
    run()