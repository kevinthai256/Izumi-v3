version = '3.0'

acatagory = {
    'general': 'General Commands',
    'mod': 'Moderation Commands',
    'fun': 'Fun Commands',
    'action': 'Interaction Commands',
    'image': 'Image Commands',
    'giveaway': "Giveaway Commands",
    'anime': "Anime Commands"
}

Updates = """

Made by Powiz | v3

"""

seperator = '•-•-•-•-•-•-•-•-•'

log = f"""

{seperator}
Adapted support for most recent Discord.py .
{seperator}
Changed unsupported Tenor API to Klipy API.
"""

cmdinfo = {
    "general":
    " **cmd**: Helps with commands. (Aliases: 'commands' 'helpme')\n**.user**: Shows info about a user. (Aliases: 'info' 'whois')\n**al**: Shows avaliable terms and actions. (Aliases: 'actionlist' 'tl' 'termlist' 'actions' 'terms')\n**s 'message'**: Spice up a message.\n**wc 'mentioned user'**: Welcome a member! (Aliases: 'wc')",
    "giveaway":
    " **gcr**: Create a giveaway. (**Can only be used by mods.** Aliases: 'giveaway' 'gcreate')\n**grr 'channel' 'message id'**: Rerolls a giveaway. (**Can only be used by mods.**)\n**gdel 'mesaage id'**: Deletes a giveaway. (**Can only be used by mods.** Aliases: 'givedel')",
    "mod":
    " **c 'value'**: Delete messages. (Aliases: 'clear' 'delete')\n**log**: Shows changes made since last version. (Aliases: 'updates')\n**mute 'user'**: Mutes a user for all channels.\n**unmute 'user'**: unmutes a user.\n**an 'title' 'message'**: Sends out an anouncement. (Aliases: 'embed') **poll 'title' 'option 1' or 'option 2'**: Creates a poll. Can be up to 5 options!!",
    "fun":
    " **pick 'list'**: picks something random. Must be seperated by ',' or 'or'. (Aliases: 'random' 'choose')\n**8b 'question'**: Summons Magic 8 ball... (Aliases: '_8ball question' '8ball question')\n**q**: Gets a random topic. (Aliases: 'randomtopic' 'question' 'topic')\n**wyr**: Gets a would you rather question.\n**joke**: Tells you a joke.\n**pun**: Tells you a pun.(Aliases: 'badpun') ",
    "action":
    " \n**s @user**: Say something to @user!\n**'term' @user**: Do something to @user! ",
    "image":
    " \n**'tag'**: *Gets an image based on tag. Use .tags to view all tags.\n**g 'search'**: Gets a gif based on search. ",
    "anime":
    " **asearch 'anime name'**: *Gets info about an anime. (Aliases: 'anime')*\n**char 'anime character name'**: *Gets info about an anime character. (Aliases: 'character' 'charsearch')*"
}
