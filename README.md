# CommunautoAlert

This is a command line script that will alert you when a communauto vehicle is available within a reasonable distance from you. 

## Install

```
$ git clone https://github.com/joshunrau/CommunautoAlert
$ cd CommunautoAlert
$ make
```

## Usage

```
usage: communauto-alert [-h] [-v] [--interval] [--max_distance] latitude longitude

positional arguments:
  latitude         your latitude
  longitude        your longitude

options:
  -h, --help       show this help message and exit
  -v, --version    show program's version number and exit
  --interval       interval between checks in seconds (default: 60)
  --max_distance   max distance of vehicle in meters (default: 500)
```

## Test

```
$ make test
```
