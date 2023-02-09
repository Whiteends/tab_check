import psutil
import time
import os
import subprocess

def get_process_list():
    process_list = []
    for process in psutil.process_iter():
        process_list.append(process.name())
    return process_list

def notify_user():
    subprocess.Popen(['notify-send', 'Too many browser tabs open! Please close some tabs to save memory.'])

def check_browser_tabs():
    browser_list = ['firefox', 'chrome', 'safari', 'opera', 'edge']
    process_list = get_process_list()
    for browser in browser_list:
        if browser in process_list:
            if psutil.Process(os.getpid()).memory_info().rss > 2000000000:
                notify_user()
                break

if __name__ == '__main__':
    while True:
        check_browser_tabs()
        time.sleep(60)
