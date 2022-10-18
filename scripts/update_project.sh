#!/bin/bash

killall python manage.py runserver 0:8000
cd /root/KGflex
\cp -rf config media static KGflex templates requirements.txt /django
cd /django
source myhome/bin/activate
sudo sed -i "/twisted-iocpsupport==1.0.2/d" /django/requirements.txt
pip install -r requirements.txt

sudo sed -i "s/DEBUG = .*/DEBUG = False/" /django/config/settings.py
sudo sed -i "s/is_Production = .*/is_Production = False/" /django/config/settings.py
sudo sed -i "s/DataBase_Write_Endpoint = .*/DataBase_Write_Endpoint = \"{Write_Endpoint}\"/" /django/config/settings.py
sudo sed -i "s/DataBase_Read_Endpoint = .*/DataBase_Read_Endpoint = \"{Read_Endpoint}\"/" /django/config/settings.py
sudo sed -i "s/USE_CACHE = .*/USE_CACHE = False/" /django/config/settings.py
sudo sed -i "s/IS_HOME = .*/IS_HOME = False/" /django/config/settings.py
sudo sed -i "s/ REDIS_HOST = .*/ REDIS_HOST = \"{REDIS_HOST}\"/" /django/config/settings.py
sudo systemctl restart django
nohup python manage.py runserver 0:8000 &
