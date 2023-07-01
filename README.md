# communauto-alert

This is a command line script that will alert you when a communauto vehicle is available within a reasonable distance from you. 

## Install

```
$ git clone https://github.com/joshunrau/communauto-alert
$ cd communauto-alert
$ make
```

Please note, that for notifications to work on Mac or Windows, you may need to install additional packages. If you experience any errors with this, please refer to the [apprise wiki](https://github.com/caronc/apprise/wiki).

### MacOS

```bash
brew install terminal-notifier
```

### Windows

```bash
pip install pywin32
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

By default, the script will try to send a desktop notification. A first notification is sent at the beginning as a test. A subsequent one is sent when a car matching the filters is identified.

You can override the default behavior specifying your own [notification provider(s)](https://github.com/caronc/apprise/wiki) with an [apprise compatible configuration file](https://github.com/caronc/apprise/wiki/config) and using the ```--notify``` CLI option.

## Usage

```
usage: communauto-alert [-h] [-v] [--interval] [--max-distance] [--no-prius] [--province] [--notify] latitude longitude

positional arguments:
  latitude         your latitude
  longitude        your longitude

options:
  -h, --help       show this help message and exit
  -v, --version    show program's version number and exit
  --interval       interval between checks in seconds (default: 30)
  --max-distance   maximum distance of vehicle in meters (default: 500)
  --no-prius       ignore vehicles with the model "Prius C" (default: False)
  --province       the province where the search will be conducted (AL, NS, ON, QC) (default: QC)
  --notify         path to apprise compatible configuration file (https://github.com/caronc/apprise/wiki/config) (default: None)
```
