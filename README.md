# Monitor (Unhandled Orders)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/68f6ca72e58946dea6e5b667ea978b8e)](https://www.codacy.com/manual/Silver3310/Monitor?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Silver3310/Monitor&amp;utm_campaign=Badge_Grade)

The repository contains all the necessary configurations to make the clean Raspberry PI work. It shows orders in real time and notifies users by a special sound when there are new ones.

## Setup

1.  Make sure you have the chromium and ffmpeg being installed on your device: ```sudo apt install ffmpeg``` && ```sudo apt install chromium-browser```

2.  Copy the folder **NotifySoundScript** to the ```/home/pi/Documents/```

3.  Copy the file **autostart** to the ```/home/pi/.config/lxsession/LXDE-pi/```

4.  Disable screen sleep, open the file ```sudo nano /etc/lightdm/lightdm.conf``` and add the following lines to the ```[SeatDefaults]``` section: ```xserver-command=X -s 0 dpms```
