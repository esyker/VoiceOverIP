#INSTRUÇÕES DE INSTALAÇÃO

#Instalar o Asterisk
sudo apt-get update
sudo apt-get install asterisk

#Copiar ficheiros sip.conf e extensions.conf para a diretoria correta
sudo cp sip.conf /etc/asterisk
sudo cp extensions.conf /etc/asterisk

#Copiar ficheiros de som para a diretoria correta
sudo cp *.gsm /usr/share/asterisk/sounds

#Instalar a interface de conversao de texto para voz googletts
sudo apt install git
git clone git://github.com/zaf/asterisk-googletts
sudo cp asterisk-googletts/googletts.agi /usr/share/asterisk/agi-bin/
sudo chmod 777 /usr/share/asterisk/agi-bin/googletts.agi

#Instalar os pacotes sox e mpg123, necessarios ao funcionamento da
#interface googletts
sudo apt-get install sox
sudo apt-get install mpg123

#Copiar o ficheiro postal_code.py para a diretoria correta
sudo cp postal_code.py /usr/share/asterisk/agi-bin
sudo chmod 777 /usr/share/asterisk/agi-bin/postal_code.py

#Instalar o pacote python-pip, bem como as necessarias bibliotecas 
#em modo root
sudo apt install python-pip
sudo -i
pip install pyst2
pip install beautifulsoup4
pip install requests
pip install lxml
exit

#Arranque do asterisk
sudo asterisk -vvvvr
reload