# Script to execute calendar notification
dunstify -a "Calendar" "$(cal)" -u low -h string:x-dunst-stack-tag:cal
