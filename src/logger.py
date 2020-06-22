from service import *
import time


def log_info(message):
    with open(to_logs("log.txt"), 'a') as log:
        log.write(time.ctime() + " : info : " + str(message) + '\n')


def log_collected(message):
    with open(to_logs("log_collected.txt"), 'a') as log:
        log.write(time.ctime() + " : collected : " + str(message) + '\n')


def log_debug(message):
    with open(to_logs("log_debug.txt"), 'a') as log:
        log.write(time.ctime() + " : debug : " + str(message) + '\n')
