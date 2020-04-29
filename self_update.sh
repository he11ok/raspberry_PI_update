#!/bin/bash
cd ~
sudo mkdir -p /home/pi/self_update

cd /home/pi/self_update
sudo mkdir -p backup
sudo mkdir -p temp
sudo mkdir -p on_board

cd temp
sudo git clone https://github.com/he11ok/raspberry_PI_update.git
sudo mv raspberry_PI_update ./raspberry_PI_update0
sudo cp -r /home/pi/self_update/temp/raspberry_PI_update0 /home/pi/self_update/on_board/
sudo rm -r raspberry_PI_update0
cd ..


cd backup
sudo rm -rf raspberry_PI_update10
sudo mv raspberry_PI_update9 ./raspberry_PI_update10
sudo mv raspberry_PI_update8 ./raspberry_PI_update9
sudo mv raspberry_PI_update7 ./raspberry_PI_update8
sudo mv raspberry_PI_update6 ./raspberry_PI_update7
sudo mv raspberry_PI_update5 ./raspberry_PI_update6
sudo mv raspberry_PI_update4 ./raspberry_PI_update5
sudo mv raspberry_PI_update3 ./raspberry_PI_update4
sudo mv raspberry_PI_update2 ./raspberry_PI_update3
sudo mv raspberry_PI_update1 ./raspberry_PI_update2
cd ..

cd on_board
sudo cp -r ./raspberry_PI_update0 ./raspberry_PI_update1
sudo chmod -R 0777 ./raspberry_PI_update0
sudo cp ./raspberry_PI_update0/internet_connection.sh ~/
sudo cp ./raspberry_PI_update0/self_update.sh ~/
sudo mv raspberry_PI_update1 /home/pi/self_update/backup/

#mv self_update out
#cd raspberry_PI_update0
#sudo mv self_update.sh /home/pi
cd ..


cd ~ 
python3 self_update/on_board/raspberry_PI_update0/email_IP_Gmail_func.py 'hanlimu111' 'hanlimu11' '********'
