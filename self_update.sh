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
sudo mv raspberry_PI_update1 /home/pi/self_update/backup/
cd ..


cd ~ 
python3 /home/pi/self_update/on_board/raspberry_PI_update0/email_IP_Gmail_func.py 'receiver_name' 'user_name' 'password'
