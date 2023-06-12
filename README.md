# CommunautoAlert

This is a command line script that will alert you when a communauto vehicle is available within a reasonable distance from you. 

## Install

```
$ git clone https://github.com/joshunrau/CommunautoAlert
$ cd CommunautoAlert
$ make
```

## Recommended Setup

I recommend storing the coordinates of interest in environment variables, for example:

```
$ export YOUR_LOCATION_LATITUDE=45.5019
$ export YOUR_LOCATION_LONGITUDE=-73.5674
```

You can set these in your `.bashrc` or `.zshrc` and use as needed:

```
$ communauto-alert $YOUR_LOCATION_LATITUDE $YOUR_LOCATION_LONGITUDE
```

## Notifications
By default, the script will try to send a desktop notification. A first notification is sent at the beginning as a test. A subsequent one, when a car matching the filters is idenfied.

You can override the default behaviour specifying your own [notification provider(s)](https://github.com/caronc/apprise/wiki) creating an [apprise compatible configuration file](https://github.com/caronc/apprise/wiki/config) and using the ```--notify``` CLI option.

## Usage

```
usage: communauto-alert [-h] [-v] [--interval] [--max-distance] [--no-prius] latitude longitude

positional arguments:
  latitude         your latitude
  longitude        your longitude

options:
  -h, --help       show this help message and exit
  -v, --version    show program's version number and exit
  --interval       interval between checks in seconds (default: 30)
  --max-distance   maximum distance of vehicle in meters (default: 500)
  --no-prius       ignore vehicles with the model "Prius C" (default: False)
  --notify         apprise compatible configuration file (default: notifications are sent to dbus, macosx and windows providers)
  --province       province (e.g.: AL, NS, ON, QC) (default: QC)
```
