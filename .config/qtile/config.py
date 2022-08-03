# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os, subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle Floating mode"),
    #Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "l", lazy.spawn("dm-tool switch-to-greeter"), desc="Lock session"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "n", lazy.spawn("firefox"), desc="Launch Mozilla Firefox"),
    Key([mod], "f", lazy.spawn("pcmanfm"), desc="Launch Mozilla Firefox"),
    Key([mod], "d", lazy.spawn("rofi -show drun -modi drun"), desc="Launch Dmenu"),
    Key([], "Print", lazy.spawn("sh /home/mdfk/.config/rofi/screenshot.sh")),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

# Media
    Key([], "XF86AudioRaiseVolume", lazy.spawn("python /home/mdfk/.config/scripts/notify-main volume inc 6")),
    Key(["shift"], "XF86AudioRaiseVolume", lazy.spawn("python /home/mdfk/.config/scripts/notify-main volume set 20")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("python /home/mdfk/.config/scripts/notify-main volume dec 6")),
    Key(["shift"], "XF86AudioLowerVolume", lazy.spawn("python /home/mdfk/.config/scripts/notify-main volume set 70")),
    Key([], "XF86AudioMute", lazy.spawn("python /home/mdfk/.config/scripts/notify-main volume set toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("sh /home/mdfk/.config/i3/notify-song.sh play")),
    Key(["shift"], "XF86AudioPlay", lazy.spawn("systemctl --user stop mpd")),
    Key([], "XF86AudioNext", lazy.spawn("sh /home/mdfk/.config/i3/notify-song.sh next")),
    Key([], "XF86AudioPrev", lazy.spawn("sh /home/mdfk/.config/i3/notify-song.sh prev")),

# Brigtness
    Key([], "XF86MonBrightnessUp", lazy.spawn("python /home/mdfk/.config/scripts/notify-main backlight inc 6")),
    Key(["shift"], "XF86MonBrightnessUp", lazy.spawn("python /home/mdfk/.config/scripts/notify-main backlight set 75")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("python /home/mdfk/.config/scripts/notify-main backlight dec 6")),
    Key(["shift"], "XF86MonBrightnessDown", lazy.spawn("python /home/mdfk/.config/scripts/notify-main backlight set 25")),
]

groups = [
    Group("1", label="", matches=(Match(wm_class='firefox'))),#, spawn="firefox"),
    Group("2", label=""),#, layout='floating')]

    Group("3", label="", spawn="telegram-desktop"),
    Group("4", label="", matches=(Match(wm_class='KeePassXC'))),
    Group("5", label="", matches=(Match(wm_class='tutanota-desktop'))),# spawn="tutanota-desktop"),
    Group("6", label=""),
    Group("7", label=""),
    Group("8", label=""),
    Group(
        "9",
        label="",
        matches=[
            Match(wm_class=["zoom"]),
        ],
    ),
]

for i in range(len(groups)):
    keys.append(Key([mod], str((i)), lazy.group[str(i)].toscreen()))
    keys.append(
        Key([mod, "shift"], str((i)), lazy.window.togroup(str(i), switch_group=True))
    )

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus="#00B19F", border_normal="#000000", border_width=3, margin=20),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    layout.MonadWide(border_focus="#00B19F", border_normal="#000000", border_width=3, margin=30, single_margin=10),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="feather",
    fontsize=28,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
#                widget.CurrentLayout(),
                widget.Sep(padding=5, linewidth=0),
                widget.Image(filename='~/registre/Ideas/Grafico/Hornero/Hornero.png',mouse_callbacks={'Button1': lazy.spawn("rofi -show drun -modi drun")}),
                widget.Prompt(font='Iosevka', fontsize=19),
                widget.Sep(padding=5, linewidth=0),
                widget.GroupBox(
                    highlight_method='block',
                    hide_unused=True,
                    active='#20d1bf',
                    block_highlight_text_color='#FBC02D',
                    this_current_screen_border='#202020',
                    urgent_border='#4900003f',
                    rounded=True),
                widget.Sep(padding=10, linewidth=0),
                widget.WindowName(font='Iosevka Bold', fontsize=19, max_chars=40),
                widget.Mpd2(font='feather', fontsize=19, status_format='{play_status} {artist} - {title}',idle_format='{play_status} {artist} - {title}',idle_message='',no_connection='', play_states={'pause':'','play':'','stop':''},padding=25),
                widget.Clock(font='Iosevka', fontsize=19, format="%m-%d-%a %I:%M %p", mouse_callbacks={'Button1': lazy.spawn("sh /home/mdfk/.config/scripts/cal.sh")}),
                widget.Spacer(),
                widget.Systray(),
                widget.Sep(padding=20, linewidth=0),
                widget.Bluetooth(
                    mouse_callbacks={'Button1': lazy.spawn("sh /home/mdfk/.config/rofi/bluetooth.sh")},
                    hci='/dev_04_21_44_F6_93_F8'),
                widget.Wlan(format="{percent}", interface="wlp58s0",),
                widget.Volume(theme_path='/home/mdfk/.icons/'),
                widget.BatteryIcon(notify_below=60,low_percentage=0.1, theme_path='/home/mdfk/.icons/',update_interval=20),
                widget.Sep(padding=20, linewidth=0),
#                widget.QuickExit(default_text='', foreground='#FBC02D', font='feather', fontsize=28, countdown_format=' {}'),
                widget.TextBox(fmt='',foreground="#20d1bf", mouse_callbacks={"Button1": lazy.spawn("sh /home/mdfk/.config/rofi/powermenu.sh")}),
                widget.Sep(padding=15, linewidth=0)
            ],
            42,
            opacity=0.78,
#            background="#0A0E14af",
            border_width=[0, 0, 2, 0],  # Draw top and bottom borders
            border_color=["#0A0E14", "000000", "#FBC02D", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus="#00B19F",
    border_normal="#000000",
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_type="dialog"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
#        Match(wm_window_type="dialog"),
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="galculator"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# background = #af000000
# ;background = #000000
# foreground = #CCC5B9
# sep = #CCC5B9
# bg = #88C7C7C7
# ws = #DD37C0B0
# 
# bat1 = #FF0000
# bat2 = #FF3300
# bat3 = #ff6600
# bat4 = #ff9900
# bat5 = #FFCC00
# bat6 = #FFFF00
# bat7 = #ccff00
# bat8 = #99ff00
# bat9 = #66ff00
# bat10 = #33ff00
# bat11 = #00FF00
# white = #FFFFFF
# 
# ;; _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# 
# black = #000000
# red = #EC7875
# pink = #EC407A
# purple = #BA68C8
# blue = #42A5F5
# cyan = #4DD0E1
# teal = #00B19F
# green = #1fff11
# garden = #9ff835
# lime = #B9C244
# yellow = #FDD835
# amber = #FBC02D
# orange = #E57C46
# brown = #AC8476
# indigo = #6C77BB
# gray = #9E9E9E
# blue-gray = #6D8895
# 
# ;bat0 = #B6C649
# ;bat1 = #638025
# ;bat2 = #3A5D13
# ;bat3 = #103900
# ;bat4 = #9fd835
