#!/bin/bash
#  
#  by mdfk <mdfk@Elite>

systemctl --user start mpd

if [ "$1" == "play" ]; then
	mpc toggle 
elif [ "$1" == "next" ]; then
	mpc next 
elif [ "$1" == "prev" ]; then
	mpc prev 
fi

#									mpc command to define path in order <artist/album> to jpg cover imge
dunstify -i "~/Musica/.art/`mpc --format "%albumartist%/%album%" current`/art.jpg" -u low -h string:x-dunst-stack-tag:music -a "Reproduciendo" "$(mpc --format '%title% - %album%\n%artist%' current)"
