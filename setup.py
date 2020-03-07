"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['ClockOneDay_simple.py']
APP_NAME = "Alarm Clock"
DATA_FILES = ['ClockBG_Fotor.png']
OPTIONS = {'iconfile': 'Icon.icns',
           'plist': {
               'CFBundleName': APP_NAME,
               'CFBundleDisplayName': APP_NAME
            }
    }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
