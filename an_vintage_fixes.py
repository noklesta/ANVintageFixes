import sublime
import sublime_plugin
import vintage

###############################################################
# The S command should jump to indented position like Vim does
###############################################################


class AnSubstituteLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            line = self.view.line(region)
            self.view.erase(edit, line)
            self.view.run_command('reindent')
            self.view.run_command('enter_insert_mode')


###############################################################
# In visual line mode, the c and C commands should replace each
# selected region with a blank line and jump to indented
# position, like Vim does. Make two subclasses so that we can
# run the standard Vintage commands for each of them unless
# we are in visual line mode (by the way, the "Cee" forms are
# needed because ST2 doesn't accept a single capital letter
# before "Command").
###############################################################


class ChangeSelectedLines(sublime_plugin.TextCommand):
    def perform_command(self, edit):
        sel = self.view.sel()
        new_sel = []

        for region in sel:
            self.view.replace(edit, region, "\n")
            new_sel.append(sublime.Region(region.a, region.a))

        sel.clear()
        for region in new_sel:
            sel.add(region)

        self.view.run_command('reindent')
        self.view.run_command('enter_insert_mode')


class AnSmallCeeCommand(ChangeSelectedLines):
    def run(self, edit):
        if vintage.g_input_state.motion_mode == vintage.MOTION_MODE_LINE:
            self.perform_command(edit)
        else:
            # From the default Vintage keybindings; do the standard Vintage stuff
            self.view.run_command('set_action', {
                "action": "enter_insert_mode",
                "description": "Change",
                "action_args": {"insert_command": "left_delete"}
            })


class AnBigCeeCommand(ChangeSelectedLines):
    def run(self, edit):
        if vintage.g_input_state.motion_mode == vintage.MOTION_MODE_LINE:
            self.perform_command(edit)
        else:
            # From the default Vintage keybindings; do the standard Vintage stuff
            self.view.run_command('set_action_motion', {
                'action': 'enter_insert_mode',
                'action_args': {'insert_command': 'left_delete'},
                'motion': 'vi_move_to_hard_eol',
                "motion_args": {"repeat": 1, "extend": True},
                "motion_inclusive": True
            })


###################################################################
# In visual line mode, the p and P commands should replace each
# selected region with the contents of the selected register,
# not paste them before or after the selection as Vintage does now.
# Also, it should move the cursor to the first non-blank character
# after pasting.
###################################################################


class PasteLines(sublime_plugin.TextCommand):
    def run(self, edit):
        if vintage.g_input_state.motion_mode == vintage.MOTION_MODE_LINE:
            self.perform_command(edit)
        else:
            # Not visual line mode, so do the standard Vintage stuff
            self.perform_standard_vintage_command()

    def perform_command(self, edit):
        for region in self.view.sel():
            self.view.erase(edit, region)

        # In Vim, 'p' actually works like 'P' in visual line mode, so paste
        # left regardless of which command we are running
        self.view.run_command('vi_paste_left')
        self.view.run_command('exit_visual_mode')
        self.view.run_command('set_motion', {
            "motion": "vi_move_to_first_non_white_space_character",
            "motion_args": {"extend": True, "repeat": 1},
            "clip_to_line": True
        })


class AnPasteLeftCommand(PasteLines):
    def perform_standard_vintage_command(self):
        self.view.run_command('vi_paste_left')


class AnPasteRightCommand(PasteLines):
    def perform_standard_vintage_command(self):
        self.view.run_command('vi_paste_right')

###########################################
# Scrolling by more than one line a a time
###########################################


class ScrollingBase(sublime_plugin.TextCommand):
    def scroll(self, direction, animate):
        current_pos = self.view.viewport_position()
        delta = self.view.line_height() * self.nlines
        self.view.set_viewport_position((current_pos[0], current_pos[1] + delta * direction), animate)


class AnScrollUpCommand(ScrollingBase):
    def run(self, edit, nlines=3, animate=False):
        self.nlines, self.animate = nlines, animate
        self.scroll(-1, animate)


class AnScrollDownCommand(ScrollingBase):
    def run(self, edit, nlines=3, animate=False):
        self.nlines, self.animate = nlines, animate
        self.scroll(1, animate)

#################
#################
