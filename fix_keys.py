import re

def standardize_key(m):
    # Depending on the context, we need different strategies.
    # This is a complex replacement. Let's try to do it semantically where possible.
    pass

with open('sc.html', 'r') as f:
    content = f.read()

# 1. Update the 'key =' definitions in various loops/functions
content = re.sub(
    r"const key = projectPath \+ '\|' \+ videoName;",
    r"const key = projectPath + '|' + (subfolder ? subfolder + '\\\\' : '') + videoName;",
    content
)
content = re.sub(
    r"const key = project\.path \+ '\|' \+ \(videoFile\.subfolder \|\| ''\) \+ '\|' \+ videoFile\.name;",
    r"const key = project.path + '|' + (videoFile.subfolder ? videoFile.subfolder + '\\\\' : '') + videoFile.name;",
    content
)
content = re.sub(
    r"const key = projectPath \+ '\|' \+ subfolder \+ '\|' \+ videoName;",
    r"const key = projectPath + '|' + (subfolder ? subfolder + '\\\\' : '') + videoName;",
    content
)

# Fix other specific instances
content = re.sub(
    r"shortcutSelections\.get\(projectPath \+ '\|' \+ videoName\)",
    r"shortcutSelections.get(projectPath + '|' + (subfolder ? subfolder + '\\\\' : '') + videoName)",
    content
)

# Persistence lookups
content = re.sub(
    r"editModeRotatedVideos\.get\(project\.path \+ '\|' \+ videoFile\.name\)",
    r"editModeRotatedVideos.get(key)",
    content
)

# Subfolder-sc logic in sc_actions.ps1 generation
content = re.sub(
    r"const key = sel\.projectPath \+ '\|' \+ sel\.videoName;",
    r"const key = sel.projectPath + '|' + (sel.subfolder ? sel.subfolder + '\\\\' : '') + sel.videoName;",
    content
)

with open('sc.html', 'w') as f:
    f.write(content)
