import os


'''
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install apt-transport-https
sudo apt-get update
sudo apt-get install sublime-text
curl -sS https://download.spotify.com/debian/pubkey.gpg | sudo apt-key add - 
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
sudo apt-get update
sudo apt-get install spotify-client
'''


os.system('bash -c \"wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -\"')
os.system('bash -c \"sudo apt-get install apt-transport-https\"')
os.system('bash -c \"curl -sS https://download.spotify.com/debian/pubkey.gpg | sudo apt-key add - \"')
os.system('bash -c \"sudo apt-get update\"')
os.system('bash -c \"echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list\""')
os.system('bash -c \"sudo apt-get install sublime-text\"')
os.system('bash -c \"sudo apt-get install spotify-client\"')
