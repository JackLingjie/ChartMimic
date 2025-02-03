curl -sSL -O https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb

sudo dpkg -i packages-microsoft-prod.deb

sudo apt-get update 

sudo apt-get install -y azure-cli

sudo apt-get install -y blobfuse2

umount /mnt/lingjiejiang