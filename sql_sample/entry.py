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
    
    from script import get, create, delete, filter
    delete.truncate()
    create.initial_data()
    
    print("\n========= get ========= ")
    get.get_all_data()
    # get.get_data_by_pk()
    get.get_data_by_filter_self_column("taga")
    get.get_data_by_filter_self_variable_column("tagline", "taga")
    
    print("\n========= filter ========= ")
    filter.filter_data_by_filter_self_column("taga")
    filter.filter_data_by_filter_self_variable_column("tagline", "taga")
    
if __name__ == '__main__':
    print("\n========= start =========")
    entry()
    print("\n========= finish =========")
