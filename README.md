# Sublime Text 2 plugin: ANVintageFixes

Temporary fixes for some of the commands in the Vintage plugin for Sublime Text
2 that do not work quite the way they do in Vim.

Since I didn't have time to study the Vintage code thoroughly enough to make
the proper changes in Vintage itself, these fixes are implemented using a mix
of Vintage commands and standard API calls. I expect the fixes to gradually
become obsolete as the commands are fixed in Vintage.

## Installation

Since this is only meant to be temporary, I didn't bother to submit it to
Package Control. You can just clone it from GitHub:

    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
    git clone git@github.com:noklesta/ANVintageFixes.git

## Fixes

Currently, the following fixes are implemented:

* The 'S' command should jump to indented position like Vim does

* In visual line mode, the 'c' and 'C' commands should replace each selected
region with a blank line and jump to indented position, like Vim does.

* In visual line mode, the 'p' and 'P' commands should replace each selected
region with the contents of the selected register, not paste them before or
after the selection as Vintage does now. Also, it should move the cursor to
the first non-blank character after pasting.

## Keybindings

The plugin does not install any keybindings automatically. Put something like
this in your keybindings file:

    { "keys": ["S"], "command": "an_substitute_line", "context": [{"key": "setting.command_mode"}] },
    { "keys": ["c"], "command": "an_small_cee", "context": [{"key": "setting.command_mode"}] },
    { "keys": ["C"], "command": "an_big_cee", "context": [{"key": "setting.command_mode"}] },
    { "keys": ["p"], "command": "an_paste_right", "context": [{"key": "setting.command_mode"}] },
    { "keys": ["P"], "command": "an_paste_left", "context": [{"key": "setting.command_mode"}] }

...and then just remove the keybindings as the commands are fixed in Vintage.

## Caveat

I am a newcomer to ST2 and far from a Vim wizard, so the code may certainly
leave room for improvement and the commands may not behave like their Vim
counterparts in every respect (although more so than the corresponding
standard Vintage commands).
