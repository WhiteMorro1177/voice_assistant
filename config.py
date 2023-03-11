microphone_index = 1

apps = {  # applications, that bot can execute
    "браузер" : "firefox.exe",
    "файлы" : "explorer.exe"
}

options = {
    "alias": {"григорий", "гриша", "григ", "бот"},  # assistant names
    "cmd": {  # assistant recognizable commands
        "time": {"сколько время", "который час"},
        "open": {
            "cmd_name": {"открой", "запусти"},
            "app": apps,
        },
        "browse": {"найди", "загугли"},
    },
}

# 1 | "bot" | "alias" | ""
# 2 | "открой" | "cmd" | "open"