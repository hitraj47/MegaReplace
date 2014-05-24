MegaReplace
===========

MegaReplace is a Sublime Text plugin that allows you to do batch find and replace. Currently does not support regular expressions and all searches are case sensitive.

Installation
============

1. Create a folder in your Sublime Text user packages called *MegaReplace*. The folder **MUST** have this name!
2. Pull/clone/copy the files from the Github repository into that folder.
3. Restart Sublime Text.

Usage
=====

There are a minimum of two files that need to be created in order to use MegaReplace. The first is a JSON file that lists all the items that need to be replaced and with that. The second is your Sublime Text Commands file (an example is included with the repository).

Replacement File
----------------

Below is an example file of what your find/replacements should look like. You can use this to figure out the syntax for the JSON file.

    [
      {
        "replacement": "&#34;",
        "finds": [
          "&ldquo;",
          "&rdquo;",
          "“",
          "”",
          "&quot;"
        ]
      },
      {
        "replacement": "&#39;",
        "finds": [
          "&rsquo;",
          "&lsquo;",
          "&#8217;",
          "’"
        ]
      },
      {
        "replacement": "&#45;",
        "finds": [
        "–",
        "&ndash;"
        ]
      },
      {
        "replacement": "&#151;",
        "finds": [
        "—",
        "&mdash;"
        ]
      },
      {
        "replacement": "&reg;",
        "finds": [
        "®"
        ]
      },
      {
        "replacement": "&#134;",
        "finds": [
        "†",
        "&dagger;"
        ]
      }
    ]
    
Save this file in the MegaReplace folder as "replace_html.json". I created this file to replace single/double quotes and certain characters with their HTML entities. You can use MegaReplace for whatever you want! The next thing we will need to create is a Sublime Commands file.

Sublime Commands File
---------------------
If you pulled from the Github repository you should already have a Default.sublime-commands file in the MegaReplace folder. If you open it up, you will see the following code:

    [
        { "caption": "Replace HTML Characters", "command": "mega_replace", "args": {"replacement_file": "replace_html.json"} }
    ]

You can have as many JSON files and commands as you like. If you already understand JSON and the general syntax of Sublime Text *.sublime-commands file, then you know you can ass as many JSON replacement files and commands as you like. Simply put a comma (,) at the end of the last command and then add:

{ "caption": "**Replace HTML Characters**", "command": "mega_replace", "args": {"replacement_file": "**replace_html.json**"} 

Replace the first bold text with a friendly name or description of what you are replacing and the second bold text with the name of your replacement file.

Making the Replacements
-----------------------
1. Select the text you wish to replace.
2. Bring up the command palette (Control + Shift + P on Windows/Linux, Command + Shift + P on Mac).
3. Type the name you gave for the replacement command. In our example, that would be "Replace HTML Characters". You should see it appear in the list.
4. Press Enter or click on the command to run it.

Future Features
===============
These are features I would like to add, or since this is an open-source project, someone could add them :)

 - Case insensitive find and replace option.
 - Support for regular expression pattern matching.
