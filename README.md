# Light Control for 42's garage :
All usage restricted for 42 only. Staff or communication team, to enhance events in the garage or other places that use a GrandMA table
<img src="./bg.png" title="Banner">
## Purpose :
Connect a video to the light system and project lights to extend the video ambiant in the room

## System :
1.  The lights are controlled via a GrandMA table
2.  The stream can be from internet (youtube, twitch, netflix) or in local (VLC, mp4, wac), ... It should function from everything

## Techno used :
1.  Python  ->
2.  CPP     ->
3.  Go      ->
4.  NodeJS  ->
5.  Docker  ->  Installation of the program, with the dependencies, and auto-run

## Explanations
__Step Zero__   : Docker Launch </br>
__Step One__    : Connect to the GrandMA </br>
__Step Two__    : Divide the frame to get the dominant colors and know what to project one the walls </br>
__Step Three__  : Send the commands to the table and project the colors on the walls </br>

# USAGE
### STEP ZERO   :   Docker Instalation
> ```git clone git@github.com:NatheSief/42-lights.git ```</br>
> ```cd 42-lights``` </br>
> ```./start``` </br>

### STEP ONE : Connect to the grandMA table
> Enter the the IP Adress of the table in the field </br>
> Get the positions you want to have with each light in the matrice

### STEP TWO :
> Get the URL or path of the video you want to project </br>

### STEP THREE :
> The programm will do everything from now on </br>
> You will just need to change the path/URL when you change the source
