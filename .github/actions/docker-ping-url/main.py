import requests
import time
import os

def set_output(file_path, key, value):
    with open(file_path,'a') as f:
        print(f"{key}-{value}", file=f)


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
    delay = int(os.getenv('INPUT_DELAY'))
    max_trials = int(os.getenv('INPUT_MAX_TRIALS'))


    website_reachable = ping_url(url,delay,max_trials) == False
    set_output(os.getenv('GITHUB_OUTPUT'),'url-reachable',website_reachable)
    if not website_reachable:
        raise Exception

    


            


if __name__ == '__main__':
    run()