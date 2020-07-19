char = '-'

api_dict = {
        # API references
        'discord' : {
            'concise' : "Discord API\n{}\n".format(char),
            'detail' : "Discord API\n{}\n".format(char),
            },
        'godot' : {
            'concise' : "Godot API\n{}\n".format(char),
            'detail' : "Godot API\n{}\n".format(char),
            },
        'unity' : {
            'concise' : "Unity API\n{}\n".format(char),
            'detail' : "Unity API\n{}\n".format(char),
            },
        'unreal' : {
            'concise' : "Unreal API\n{}\n".format(char),
            'detail' : "Unreal API\n{}\n".format(char),
            },
        }

docs_dict = {
        # Documentation
        'source' : {
            'concise' : "**(guts, read, tools)**\n{}\n".format(char),
            'detail' : "Brrt source code\nOptional arguments:\n**(guts, read, tools)**\n{}\n".format(char),
            },
        'c' : {
            'concise' : "**(function, syntax)**\n{}\n".format(char),
            'detail' : "C docs\nOptional arguments:\n**(function, syntax)**\n{}\n".format(char),
            },
        'c#' : {
            'concise' : "**(keyword, operator, token, preprocessor, options, errors)**\n{}\n".format(char),
            'detail' : "C# docs\nOptional arguments:\n**(keyword, operator, token, preprocessor, options, errors)**\n{}\n".format(char),
            },
        'c++' : {
            'concise' : "**()**\n{}\n".format(char),
            'detail' : "C++ docs\nOptional arguments:\n**()**\n{}\n".format(char),
            },
        'java' : {
            'concise' : "**(classes, packages, properties)**\n{}\n".format(char),
            'detail' : "Java docs\nOptional arguments:\n**(classes, packages, properties)**\n{}\n".format(char),
            },
        'javascript' : {
            'concise' : "**()**\n{}\n".format(char),
            'detail' : "Javascript docs\nOptional arguments:\n**()**\n{}\n".format(char),
            },
        'lua' : {
            'concise' : "**(intro, basic, language, api, auxiliary, standard, standalone, version-issues, syntax)**\n{}\n".format(char),
            'detail' : "Lua docs\nOptional arguments:\n**(intro, basic, language, api, auxiliary, standard, standalone, version-issues, syntax)**\n{}\n".format(char),
            },
        'perl' : {
            'concise' : "**(manual, module)**\n{}\n".format(char),
            'detail' : "Perl docs\nOptional arguments:\n**(manual, module)**\n{}\n".format(char),
            },
        'python' : {
            'concise' : "**(index, module, glossary)**\n{}\n".format(char),
            'detail' : "Python docs\nOptional arguments:\n**(index, module, glossary)**\n{}\n".format(char),
            },
        'ruby' : {
            'concise' : "**(api, standard)**\n{}\n".format(char),
            'detail' : "Ruby docs\nOptional arguments:\n**(api, standard)**\n{}\n".format(char),
            },
        'rust': {
            'concise' : "**(mod, error, rustc, edition, rustdoc, foreword, standard)**\n{}\n".format(char),
            'detail' : "Rust docs\nOptional arguments:\n**(mod, error, rustc, edition, rustdoc, foreword, standard)**\n{}\n".format(char),
            },
        }

help_dict = {
        # Help
        'help' : {
            'concise' : "Let Brrt help you talk to Brrt.\n{}\n".format(char),
            'detail' : "Let Brrt help you talk to Brrt.\n{}\n".format(char),
            },
        'docs' : {
            'concise' : "Let Brrt help you find documentation.\n{}\n".format(char),
            'detail' : "Let Brrt help you find documentation.\n{}\n".format(char),
            },
        'api' : {
            'concise' : "Let Brrt help you find APIs.\n{}\n".format(char),
            'detail' : "Let Brrt help you find APIs.\n".format(char),
            },
        # Settings
        'settings' : {
            'concise' : "Let Brrt help you look at some of Brrt's features!\n{}\n".format(char),
            'detail' : "Let Brrt help you look at some of Brrt's features!\n".format(char),
            },
        'disable' : {
            'concise' : "**(documentation, moderation, scoring, welcome, random, social, voting)**\n{}\n".format(char),
            'detail' : "Disable a feature!\n{}\nList arguments:\n**(documentation, moderation, scoring, welcome, random, social, voting)**\n".format(char),
            },
        'enable' : {
            'concise' : "**(documentation, moderation, scoring, welcome, random, social, voting)**\n{}\n".format(char),
            'detail' : "Enable a feature!\n{}\nList arguments:\n**(documentation, moderation, scoring, welcome, random, social, voting)**\n".format(char),
            },
        'shutdown' : {
            'concise' : "Shuts Brrt down and saves member data.\n{}\n".format(char),
            'detail' : "Shuts Brrt down and saves member data.\n{}\n".format(char),
            },
        # Privacy
        'keep-data' : {
            'concise' : "**(yes, no, status)**\n{}\n".format(char),
            'detail' : "Allow or disallow Brrt saving data.  Brrt encrypts this data, so only Brrt can use it.\n{}\nRequired arguments:\n**(yes, no, status)**\n".format(char),
            },
        # Social
        'broadcast' : {
            'concise' : "**(channel mention, message)**\n{}\n".format(char),
            'detail' : "Brrt will broadcast a message!\n{}\nRequired arguments:\n**(channel mention, message)**\n".format(char),
            },
        'embed' : {
            'concise' : "**(mention, message)**\n{}\n".format(char),
            'detail' : "Brrt will embed a message for you, and even include a target!\n{}\nRequired arguments:\n**(mention, message)**\n".format(char),
            },
        'echo' : {
            'concise' : "**(message)**\n{}\n".format(char),
            'detail' : "Brrt will copy you!\n{}\nRequired arguments:\n**(message)**\n".format(char),
            },
        'banter' : {
            'concise' : "**(mention)**\n{}\n".format(char),
            'detail' : "Brrt will slander you or your entry (if you have points)!\n{}\nOptional arguments:\n**(mention)**\n".format(char),
            },
        'praise' : {
            'concise' : "**(mention)**\n{}\n".format(char),
            'detail' : "Brrt will praise you or your entry!\n{}\nOptional arguments:\n**(mention)**\n".format(char),
            },
        # Points
        'give' : {
            'concise' : "**(mention, points)**\n{}\n".format(char),
            'detail' : "Brrt Will give someone points if you have them!\n{}\nRequired arguments:\n**(mention, points)**\n".format(char),
            },
        'stats' : {
            'concise' : "**(points, level, next, exp, mention)**\n{}\n".format(char),
            'detail' : "Brrt will show your stats!\n{}\nOptional arguments:\n**(points, level, next, exp, mention)**\n".format(char),
            },
        'role' : {
            'concise' : "**(role)**\n{}\n".format(char),
            'detail' : "Brrt will show and give roles!\n{}\nOptional arguments:\n**(role)**\n".format(char),
            },
        'balance-karma' : {
            'concise' : "Brrt will balance your karma for you!\n{}\n".format(char),
            'detail' : "Brrt will balance your karma for you!\n{}\n".format(char),
            },
        # Voting
        'vote' : {
            'concise' : "**(vote)**\n{}\n".format(char),
            'detail' : "Brrt will take your vote!\nRequired arguments:\n**(vote)**\n{}\n".format(char),
            },
        # Random
        'flip' : {
            'concise' : "**(guess)**\n{}\n".format(char),
            'detail' : "Brrt will flip his lucky coin for you and you can even try to guess which side it'll land on!\n{}\nOptional arguments:\n**(guess)**\n".format(char),
            },
        'd' : {
            'concise' : "**(die sides, roll count)**\n{}\n".format(char),
            'detail' : "Brrt will roll dice for you!\n{}\nOptional arguments (die sides required for roll count):\n**(die sides, roll count)**\n".format(char),
            }
        }

role_dict = {
        'role' : {
            'concise' : "Let Brrt help you find a role!".format(char),
            'detail' : "Let Brrt help you find a role!".format(char),
            },
        'sample' : {
            'concise' : "Required level: 0\n{}\n".format(char),
            'detail' : "Required level: 0\n{}\n".format(char),
            }
        }

sets_dict = {
        'settings' : {
            'concise' : "Let Brrt help you look at some of Brrt's features!\n{}\n".format(char),
            'detail' : "Let Brrt help you look at some of Brrt's features!\n{}\n".format(char),
            },
        'documentation' : {
            'concise' : "**(api, docs, source (including their respective commands))**\n{}\n".format(char),
            'detail' : "\nCommands:\n**(api, docs, source (including their respective commands))**\n{}\n".format(char),
            },
        'moderation' : {
            'concise' : "Per message.\n{}\n".format(char),
            'detail' : "This looks for certain words or phrases in all messages.\n{}\n".format(char),
            },
        'scoring' : {
            'concise' : "**(give, stats, role, balance-karma)**\n{}\n".format(char),
            'detail' : "This keeps track of scores to promote interaction with Brrt.\nCommands:\n**(give, stats, role, balance-karma)**\n{}\n".format(char),
            },
        'welcome' : {
            'concise' : "Member greetings.\n{}\n".format(char),
            'detail' : "This will greet members that join in a set channel.\n{}\n".format(char),
            },
        'random' : {
            'concise' : "**(flip, d)**\n{}\n".format(char),
            'detail' : "This is pretty random.\nCommands:\n**(flip, d)**\n{}\n".format(char),
            },
        'social' : {
            'concise' : "**(broadcast, embed, echo, banter, praise)**\n{}\n".format(char),
            'detail' : "This is for fun among members.\nCommands:\n**(broadcast, embed, echo, banter, praise)**\n{}\n".format(char),
            },
        'voting' : {
            'concise' : "**(vote)**\n{}\n".format(char),
            'detail' : "This is for member voting.\nCommands:\n**()**\n{}\n".format(char),
            },
        }
