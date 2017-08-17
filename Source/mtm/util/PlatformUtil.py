from mtm.util.Assert import *

from mtm.util.Platforms import Platforms

def toPlatformFolderName(platform):
    # We can just directly use the full platform name for folder names
    return platform

def fromPlatformFolderName(platformDirName):
    platformDirName = platformDirName.lower()

    for curPlatform in Platforms.All:
        if curPlatform.lower() == platformDirName:
            return curPlatform

    assertThat(False)

def fromPlatformArgName(platformArgStr):

    if platformArgStr == 'win':
        return Platforms.Windows

    if platformArgStr == 'webp':
        return Platforms.WebPlayer

    if platformArgStr == 'webgl':
        return Platforms.WebGl

    if platformArgStr == 'and':
        return Platforms.Android

    if platformArgStr == 'osx':
        return Platforms.OsX

    if platformArgStr == 'ios':
        return Platforms.Ios

    if platformArgStr == 'lin':
        return Platforms.Linux

    if platformArgStr == 'uwp':
        return Platforms.UWP

    assertThat(False)
    return ''
