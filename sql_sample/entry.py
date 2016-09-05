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
    
    from script import get_data, create, delete, filter, query_set
    delete.truncate()
    create.initial_data()
    
    print("\n========= get ========= ")
    get_data.get_all_data()
    # get_data.get_data_by_pk()
    get_data.get_data_by_self_column("taga")
    get_data.get_data_by_self_variable_column("tagline", "taga")
    
    print("\n========= filter ========= ")
    filter.filter_data_by_self_column("taga")
    filter.filter_data_by_self_variable_column("tagline", "taga")
    filter.filter_data_by_lookup_type("tagline", "startswith", "tag")
    
if __name__ == '__main__':
    print("\n========= start =========")
    entry()
    print("\n========= finish =========")
