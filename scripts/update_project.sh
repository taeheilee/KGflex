#!/bin/bash

killall python manage.py runserver 0:8000
cd /root/KGflex
\cp -rf config media static KGflex templates requirements.txt /django
cd /django
source myhome/bin/activate
sudo sed -i "/twisted-iocpsupport==1.0.2/d" /django/requirements.txt
pip install -r requirements.txt

sudo sed -i "s/DEBUG = .*/DEBUG = False/" /django/config/settings.py
sudo sed -i "s/DataBase_Write_Endpoint = .*/DataBase_Write_Endpoint = \"mydb-instance-1.c7tpfyaiw1nc.ap-northeast-2.rds.amazonaws.com\"/" /django/config/settings.py
sudo sed -i "s/DataBase_Read_Endpoint = .*/DataBase_Read_Endpoint = \"mydb-instance-1-ap-northeast-2a.c7tpfyaiw1nc.ap-northeast-2.rds.amazonaws.com\"/" /django/config/settings.py
sudo sed -i "s/ REDIS_HOST = .*/ REDIS_HOST = \"redis-001-001.vo2lks.ng.0001.apn2.cache.amazonaws.com\"/" /django/config/settings.py

nohup python manage.py runserver 0:8000&

run.sh >/dev/null 2>&1 &
