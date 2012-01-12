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

## Caveat

I am a newcomer to ST2 and far from a Vim wizard, so the code may certainly
leave room for improvement and the commands may not behave like their Vim
counterparts in every respect (although more so than the corresponding
standard Vintage commands).
