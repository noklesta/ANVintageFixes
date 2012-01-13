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
    git clone https://github.com/noklesta/ANVintageFixes

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

## Licence

All of ANVintageFixes is licensed under the MIT licence.

  Copyright (c) 2012 Anders Nøklestad

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.
