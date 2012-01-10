import sublime_plugin

###############################################################
# The S command should jump to indented position like Vim does
###############################################################


class AnBigSCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, ddd!")


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
