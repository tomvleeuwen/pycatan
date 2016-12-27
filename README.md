## Introduction
This is the Python code for the interactive Catan game designed for Taas.
If you don't know what this is, you don't need it.

## Installation notes
Install *Raspbian Pixel*
Install *apache2*

### Clone the archive to /home/pi/pycatan
```
$ git clone https://github.com/tomvleeuwen/pycatan.git
```
### Configure Apache2
```
$ sudo a2enmod proxy proxy_http
$ sudo rm /etc/apache2/sites-enabled/*
$ sudo cp pycatan/apache2-site.conf /etc/apache2/sites-enabled/pycatan.conf
```

### Autostart Chromium and PyCatan
Add the following lines to ~/.config/lxsession/LXDE-py:

```
@chromium-browser --user-data-dir=/home/pi/.catan --kiosk --app=http://localhost/
@/home/pi/pycatan/start
```

## Usage
Connect a button to GPIO 23.
