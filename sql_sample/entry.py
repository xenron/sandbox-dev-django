# !/usr/bin/env python
# -*- coding:utf-8 -*-

import django
import os

def entry():
    # sys.path.append('/www/web/')
    # pro_dir = os.getcwd()
    # sys.path.append(pro_dir)
    # os.environ['DJANGO_SETTINGS_MODULE'] ='mtpc_is_application.settings'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sql_sample.settings")
    django.setup()
    
    from script import get
    get.get_test()
    
if __name__ == '__main__':
    print("\n========= start =========")
    entry()
    print("\n========= finish =========")
