#!/bin/bash

cd /KGflex
source myhome/bin/activate
sudo sed -i "/twisted-iocpsupport==1.0.2/d" /KGflex/requirements.txt
pip install -r requirements.txt

sudo sed -i "s/DEBUG = .*/DEBUG = False/" /KGflex/config/settings.py
sudo sed -i "s/is_Production = .*/is_Production = False/" /KGflex/config/settings.py
sudo sed -i "s/DataBase_Write_Endpoint = .*/DataBase_Write_Endpoint = \"{Write_Endpoint}\"/" /KGflex/config/settings.py
sudo sed -i "s/DataBase_Read_Endpoint = .*/DataBase_Read_Endpoint = \"{Read_Endpoint}\"/" /KGflex/config/settings.py
sudo sed -i "s/USE_CACHE = .*/USE_CACHE = False/" /KGflex/config/settings.py
sudo sed -i "s/IS_HOME = .*/IS_HOME = False/" /KGflex/config/settings.py
sudo sed -i "s/ REDIS_HOST = .*/ REDIS_HOST = \"{REDIS_HOST}\"/" /KGflex/config/settings.py
sudo systemctl restart KGflex
source myhome/bin/activate
nohup python manage.py runserver 0:8000 &
