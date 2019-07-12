#!/usr/bin/python
#encoding:utf-8

import telnetlib
import threading
import threading
import sys
import requests
import time
import ssl
import re
import os


if __name__ == '__main__':
    url = 'https://123.dd.44.fdd/'

    if str(url).startswith('http'):
        print(url)
        i = url.split('/').__len__()
        print(i)
        #print(url.split('/')[0]+'//'+url.split('/')[1]+url.split('/')[2]+'/'+url.split('/')[3])


