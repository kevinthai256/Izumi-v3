
version = '2.7'

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

Made by Powiz | v2.7

"""

seperator = '•-•-•-•-•-•-•-•-•'

log = f"""

{seperator}
Added Komi command and Tinder command
"""


cmdinfo = [


{"general": 
[
  {"name": "Help me!",
    "bio": "Helps with commands.",
    "Aliases": ['help','commands','helpme', 'cmd'],
    "Syntax": "`cmd <command>/<catagory>`"
  }
,
  {"name": "Info!",
    "bio": "Shows info about a user.",
    "Aliases": ['info','whois', 'user'],
    "Syntax":"`user <@user>`"
    }
,
  {"name": "Welcome!",
    "bio": "Shows avaliable terms and actions.",
    "Aliases": ['actionlist','tl','termlist','actions','terms', 'al'],
    "Syntax":"`al`"
    }
,
  {"name": "Spice!",
    "bio": "Spice up a message.",
    "Aliases": ['s'],
    "Syntax":"`s <message>`"
    }
,
  {"name": "Welcome!",
    "bio": "Welcome a member!",
    "Aliases": ['welcome', 'wc'],
    "Syntax":"`wc <@user>`"
    }
,
  {"name": "Avatar!",
    "bio": "Get the avatar image of a user!",
    "Aliases": ['pfp', 'avatar'],
    "Syntax":"`pfp <@user>`"
    }
]

,

"giveaway":
[
  {"name": "Create a Giveaway!",
    "bio": "Create a giveaway. (MOD)",
    "Aliases": ['giveaway','gcreate', 'gcr'],
    "Syntax": "`gcr`"
  }
,
  {"name": "Reroll a Giveaway!",
    "bio": "Rerolls a giveaway! (MOD)",
    "Aliases": ['grr'],
    "Syntax":"`grr <messageid>`"
    }
,
  {"name": "Delete a Giveaway!",
    "bio": "Deletes a giveaway.",
    "Aliases": ['gdel'],
    "Syntax":"`gdel <messageid>`"
    }
]

,

"mod":
[
  {"name": "Delete messages!",
    "bio": "Deletes messages- (MOD)",
    "Aliases": ['clear','delete'],
    "Syntax": "`c <value>`"
  }
,
  {"name": "Log!",
    "bio": "Shows changes made since last version! (MOD)",
    "Aliases": ['log'],
    "Syntax":"`log`"
    }
,
  {"name": "Mute!",
    "bio": "Removes speaking privileges.",
    "Aliases": ['mute'],
    "Syntax":"`mute <@user>`"
    }
,
  {"name": "Unmute!",
    "bio": "you may speak.",
    "Aliases": ['unmute'],
    "Syntax":"`unmute <@user>`"
    }
,
  {"name": "Announce!",
    "bio": "Sends out an announcment!",
    "Aliases": ['an','embed'],
    "Syntax":"`an <title> <message>`"
    }
,
  {"name": "Poll!",
    "bio": "Creates a poll!. Up to 5 options!",
    "Aliases": ['poll'],
    "Syntax":"`poll <title> <option1> <option2> ...`"
    }
,
  {"name": "Add role!",
    "bio": "Gives a role!.",
    "Aliases": ['role', 'addrole', 'giverole'],
    "Syntax":"`role <@user> <@role>`"
    }
,
  {"name": "Takes role!",
    "bio": "Takes a role away!.",
    "Aliases": ['rrole', 'removerole'],
    "Syntax":"`rrole <@user> <@role>`"
    }
]

,

"fun": 
[
    {"name": "Pick!",
    "bio": "Picks out of options! Seperate by ',' or 'or'.",
    "Aliases": ['pick','random', 'choose'],
    "Syntax": "`pick <option1> or <option2> or...`"
  }
,
  {"name": "8 ball!",
    "bio": "Answers your questions!",
    "Aliases": ['8b', '8ball'],
    "Syntax":"`8b <yesornoquestion>`"
    }
,
  {"name": "Topic!",
    "bio": "Gets a random topic!",
    "Aliases": ['topic', 'question', 'randomtopic'],
    "Syntax":"`topic`"
    }
,
  {"name": "Would you rather!",
    "bio": "Gets a random would you rather question!",
    "Aliases": ['wyr'],
    "Syntax":"`wyr`"
    }
,
  {"name": "Puns!",
    "bio": "Gets a random pun!",
    "Aliases": ['pun','badpun'],
    "Syntax":"`pun`"
    }
,
  {"name": "Videos!",
    "bio": "Gets a random video!",
    "Aliases": ['video'],
    "Syntax":"`video`"
    }
,
  {"name": "Copycat!",
    "bio": "Copies what you say!",
    "Aliases": ['repeat'],
    "Syntax":"`repeat <text>`"
    }
,
  {"name": "Plant Tree!",
    "bio": "Plants a tree :D",
    "Aliases": ['planttree'],
    "Syntax":"`plantree`"
    }
,
  {"name": "Roll a dice!",
    "bio": "Rolls a number between zero and input!",
    "Aliases": ['dice', 'roll'],
    "Syntax":"`roll <input>`"
    }
]

,

"action": 
[
      {"name": "BAKA!",
    "bio": "BAKAAA!",
    "Aliases": ['baka'],
    "Syntax": "`baka <@user>`"
  }
,
  {"name": "memez",
    "bio": "sends a meme!",
    "Aliases": ['meme'],
    "Syntax":"`meme <@user>`"
    }
,
  {"name": "Action!",
    "bio": "Do something to someone!",
    "Aliases": ['see al command.'],
    "Syntax":"`<term> <@user>`"
    }
]

,

"image": 
[
  {"name": "Komi!",
    "bio": "Komi says something!",
    "Aliases": ['komi'],
    "Syntax":"`komi <text>`"
    },
  {"name": "Tinder!",
    "bio": "Gets a tinder profile! (use tindere to make one!)",
    "Aliases": ['tinder'],
    "Syntax":"`tinder <@user>`"
    },
  {"name": "Booru!",
    "bio": "Look up images on danbooru!",
    "Aliases": ['booru'],
    "Syntax":"`booru <search>`"
    }
,
  {"name": "Anime GIF!",
    "bio": "Get an anime GIF!",
    "Aliases": ['ag'],
    "Syntax":"`ag <search>`"
    }
,
  {"name": "GIF!",
    "bio": "Get A GIF!",
    "Aliases": ['g'],
    "Syntax":"`g <search>`"
    }
]

,

"anime": 
[
  {"name": "Search for an Anime!",
    "bio": "Search for an anime by search!",
    "Aliases": ['anime','asearch'],
    "Syntax":"`anime <search>`"
    }
    ,
  {"name": "Search for a Character!",
    "bio": "Gets info about an anime character!",
    "Aliases": ['char', 'character', 'charsearch'],
    "Syntax":"`char <search>`"
    }
]
}
]



