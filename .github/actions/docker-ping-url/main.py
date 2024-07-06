import requests
import time

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
    if ping_url(INPUT_URL,INPUT_DELAY,INPUT_MAX_TRIALS) == False:
        raise Exception

    


            


if __name__ == '__main__':
    run()