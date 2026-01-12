#!/bin/bash
set -e
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade

#! run this command to make the script executable:
#! sudo chmod +x /usr/local/bin/update.sh

sudo apt-get autoremove
sudo apt-get autoclean
echo "System update complete!"
sudo snap refresh
echo "Snap packages update complete!"   
echo "All updates are complete!"

#! then you can run the script with:
#! sudo /usr/local/bin/update.sh 
echo "System update script executed successfully."

#! you can also create an alias for easier access:
