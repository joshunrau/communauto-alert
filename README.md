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
$ export DOWNTOWN_MONTREAL_LATITUDE=45.5019
$ export DOWNTOWN_MONTREAL_LONGITUDE=-73.5674
```

You can set these in your `.bashrc` or `.zshrc` and use as needed:

```
$ communauto-alert $DOWNTOWN_MONTREAL_LATITUDE $DOWNTOWN_MONTREAL_LONGITUDE
```

## Usage

```
usage: communauto-alert [-h] [-v] [--interval] [--max-distance] [--no-prius] latitude longitude

positional arguments:
  latitude         your latitude
  longitude        your longitude

options:
  -h, --help       show this help message and exit
  -v, --version    show program's version number and exit
  --interval       interval between checks in seconds (default: 60)
  --max-distance   maximum distance of vehicle in meters (default: 500)
  --no-prius       ignore vehicles with the model "Prius C" (default: False)
```
