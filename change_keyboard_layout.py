#!/usr/bin/python3

config_path = "/home/seves/.config/hypr/hyprland.conf"

with open(config_path, "r") as f:
    config_file_lines = f.readlines()

for a in range(0, len(config_file_lines)):
    if "kb_layout" in config_file_lines[a]:
        if "us" in config_file_lines[a]:
            config_file_lines[a] = config_file_lines[a].replace("us", "ru")
        else:
            config_file_lines[a] = config_file_lines[a].replace("ru", "us")
        
with open(config_path, "w") as f:
    f.writelines(config_file_lines)
