# SGGDATA prepare
this repo aim to prepare data for sc2 scene graph generation train and test

## Preparation:
install starcraft2 (development in Windows11),

install requirements.txt,

maybe a little change for your pysc2 library.

------
## Scripts

-  extract_screen_gameloops.py
    ~~~
    extract_screen_gameloops.py --VideoDIR your_directory --JsonDIR your_directory --ReplayDIR your_directory --NUM number_of_replay_to_process
    ~~~
    saves screenshots as video in ```VideoDIR``` and saves gameloops in ```JsonDIR```
    when replay game with gameclient renderer

- generateSggData.py
  ~~~
  generateSggData.py --VideoDIR your_directory --JsonDIR your_directory --OutputDIR your_directory
  ~~~

    generate Date json and txt files for sgg training

- convertVideo2jpg.py
  ~~~
  convertVideo2jpg.py --VideoDIR your_directory --OutputDIR your_directory
  ~~~
    convert Videos to jpg files