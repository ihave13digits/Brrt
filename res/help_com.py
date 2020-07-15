char = '-'

api_dict = {
        #'' : "\n{}\n".format(char),
        # API references
        'discord' : "Discord API\n{}\n".format(char),
        'godot' : "Godot API\n{}\n".format(char),
        'unity' : "Unity API\n{}\n".format(char),
        'unreal' : "Unreal API\n{}\n".format(char),
        }

docs_dict = {
        #'' : "\n{}\n".format(char),
        # Documentation
        'source' : "Brrt source code\nOptional arguments:\n**(guts, read, tools)**\n{}\n".format(char),
        'c' : "C docs\nOptional arguments:\n**(function, syntax)**\n{}\n".format(char),
        'c#' : "C# docs\nOptional arguments:\n**(keyword, operator, token, preprocessor, options, errors)**\n{}\n".format(char),
        'c++' : "C++ docs\nOptional arguments:\n**()**\n{}\n".format(char),
        'java' : "Java docs\nOptional arguments:\n**(classes, packages, properties)**\n{}\n".format(char),
        'javascript' : "Javascript docs\nOptional arguments:\n**()**\n{}\n".format(char),
        'lua' : "Lua docs\nOptional arguments:\n**(intro, basic, language, api, auxiliary, standard, standalone, version-issues, syntax)**\n{}\n".format(char),
        'perl' : "Perl docs\nOptional arguments:\n**(manual, module)**\n{}\n".format(char),
        'python' : "Python docs\nOptional arguments:\n**(index, module, glossary)**\n{}\n".format(char),
        'ruby' : "Ruby docs\nOptional arguments:\n**(api, standard)**\n{}\n".format(char),
        'rust': "Rust docs\nOptional arguments:\n**(mod, error, rustc, edition, rustdoc, foreword, standard)**\n{}\n".format(char),
        }

help_dict = {
        #'' : "\n{}\n".format(char),
        # Help
        'help' : "\nLet Brrt help you talk to Brrt.\n{}\n".format(char),
        'docs' : "\nLet Brrt help you find documentation.\n{}\n".format(char),
        'api' : "\nLet Brrt help you find APIs.\n{}\n".format(char),
        # Privacy
        'keep-data' : "Allow or disallow Brrt saving data.\nRequired arguments:\n**(yes, no, status)**\n{}\n".format(char),
        # Social
        'broadcast' : "Brrt will broadcast a message!\nRequired arguments:\n**(channel, message)**\n{}\n".format(char),
        'embed' : "Brrt will embed a message for you, and even include a target!\nRequired arguments:\n**(target, message)**\n{}\n".format(char),
        'echo' : "Brrt will copy you!\nRequired arguments:\n**(message)**\n{}\n".format(char),
        'banter' : "Brrt will slander you or your entry!\nOptional arguments:\n**(target)**\n{}\n".format(char),
        'praise' : "Brrt will praise you or your entry!\nOptional arguments:\n**(target)**\n{}\n".format(char),
        'stats' : "Brrt will show your stats!\nOptional arguments:\n**(points)**\n{}\n".format(char),
        # Voting
        'vote' : "Brrt will take your vote!\n{}\n".format(char),
        # Random
        'flip' : "Brrt will flip his lucky coin for you!\n{}\n".format(char),
        'd' : "Brrt will roll dice for you!\nOptional arguments:\n**(arg1=die sides, arg2=roll count)**\n{}\n".format(char),
        }
