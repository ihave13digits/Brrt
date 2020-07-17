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
        'embed' : "Brrt will embed a message for you, and even include a target!\nRequired arguments:\n**(mention, message)**\n{}\n".format(char),
        'echo' : "Brrt will copy you!\nRequired arguments:\n**(message)**\n{}\n".format(char),
        'banter' : "Brrt will slander you or your entry (if you have points)!\nOptional arguments:\n**(mention)**\n{}\n".format(char),
        'praise' : "Brrt will praise you or your entry!\nOptional arguments:\n**(mention)**\n{}\n".format(char),
        'give' : "Required arguments:\n**(mention, points)**\n{}\n".format(char),
        'stats' : "Brrt will show your stats!\nOptional arguments:\n**(points, level, next, exp, mention)**\n{}\n".format(char),
        'role' : "Brrt will show and give roles!\nOptional arguments:\n**(role)**\n{}\n".format(char),
        # Voting
        'vote' : "Brrt will take your vote!\n{}\n".format(char),
        # Random
        'flip' : "Brrt will flip his lucky coin for you and you can even try to guess which side it'll land on!\nOptional arguments:\n(guess)\n{}\n".format(char),
        'd' : "Brrt will roll dice for you!\nOptional arguments:\n(die sides required for roll count):\n**(die sides, roll count)**\n{}\n".format(char),
        }

role_dict = {
        'role' : "Let Brrt help you find a role!".format(char),
        'fresh_meat' : "Required level: 0\n{}\n".format(char),
        'newb' : "Required level: 1\n{}\n".format(char),
        'underling' : "Required level: 2\n{}\n".format(char),
        'novice' : "Required level: 4\n{}\n".format(char),
        'regular' : "Required level: 8\n{}\n".format(char),
        'gamer' : "Required level: 12\n{}\n".format(char),
        'game_lord' : "Required level: 16\n{}\n".format(char),
        'game_addict' : "Required level: 24\n{}\n".format(char),
        'advanced_user' : "Required level: 32\n{}\n".format(char),
        'power_user' : "Required level: 48\n{}\n".format(char),
        'advanced_power_user' : "Required level: 64\n{}\n".format(char),
        'junior_veteran' : "Required level: 80\n{}\n".format(char),
        'veteran' : "Required level: 96\n{}\n".format(char),
        'veteran_senior' : "Required level: 128\n{}\n".format(char),
        'veteran_commander' : "Required level: 160\n{}\n".format(char),
        'veteran_lord' : "Required level: 192\n{}\n".format(char),
        'enlightened_one' : "Required level: 256\n{}\n".format(char),
        'game_buddha' : "Required level: 512\n{}\n".format(char),
        }
