# About

Simple custom segment displaying current directory in tmux.
Based on [sample](https://devpro.media/custom-powerline-segment/#creating-the-custom-segment).

# Configuration

1. Install module using pip3:

   ```
   pip3 install --user --editable ./
   ```

2. To your `~/.config/powerline/themes/tmux/default.json` add something like:

   ```
   {
   	"segments": {
   		"right": [
   			{
   				"function": "mysegments.tmux_cwd.pane_current_path",
   				"priority": 50
   			}
   		]
   	}
   }
   ```

