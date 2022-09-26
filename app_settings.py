import json


version = '1.0.3'
settings = {}


def writesettings():
    with open('settings.json', 'w') as outfile:
        json.dump(settings, outfile, indent=4, sort_keys=True)


def initialise():
    global settings
    settings['logging'] = {}
    settings['logging']['logfilepath'] = '.\\logs\\'
    settings['logging']['logappname'] = 'ICPMS'
    settings['batchfilepath'] = '.\\'
    writesettings()


def readsettings():
    global settings
    try:
        with open('settings.json') as json_file:
            settings = json.load(json_file)
    except FileNotFoundError:
        initialise()


readsettings()
