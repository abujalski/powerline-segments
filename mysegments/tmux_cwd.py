# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import, print_function)

from powerline.bindings.tmux import get_tmux_output

def pane_current_path(pl):
    '''Return current tmux working directory'''
    return [{
        'contents': get_tmux_output(pl, 'display', '-p',  '#{pane_current_path}'),
        'highlight_groups': ['information:highlighted']
    }]

