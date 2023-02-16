# SGGDATA prepare
this repo aim to prepare data for sc2 scene graph generation train and test

## Preparation:
install starcraft2 (development in Windows11),

install requirements.txt,

download sc2 replay file with map

~~maybe a little change for your pysc2 library.~~

>**Note 1**: Please make sure the <font color='red'>version</font>  of the replay file is the <font color='red'>same</font> as the <font color='red'>version</font> of your game client.

>**Note 2**: Change the **path** in sc2/paths.py
  of python package ```sc2```, or add your sc2 client location in your system environment.

  ```python
  sc2/paths.py
  BASEDIR = {
    "Windows": "here is the location of your starcraft II installed.",
    "WSL1": "/mnt/c/Program Files (x86)/StarCraft II",
    "WSL2": "/mnt/c/Program Files (x86)/StarCraft II",
    "Darwin": "/Applications/StarCraft II",
    "Linux": "~/StarCraftII",
    "WineLinux": "~/.wine/drive_c/Program Files (x86)/StarCraft II",
  }
  ``` 

------
## Scripts

-  extract_screen_gameloops.py
    ~~~
    python extract_screen_gameloops.py --VideoDIR your_directory --JsonDIR your_directory --ReplayDIR your_directory --NUM number_of_replay_to_process
    ~~~
    saves screenshots as video in ```VideoDIR``` and saves gameloops in ```JsonDIR```
    when replay game with gameclient renderer

- generateSggData.py
  ~~~
  python generateSggData.py --VideoDIR your_directory --JsonDIR your_directory --OutputDIR your_directory
  ~~~

    generate Date json and txt files for sgg training

- convertVideo2jpg.py
  ~~~
  python convertVideo2jpg.py --VideoDIR your_directory --OutputDIR your_directory
  ~~~
    convert Videos to jpg files