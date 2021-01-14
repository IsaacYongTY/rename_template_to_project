# Introduction
As a content creator on YouTube, having an organised project folder structure is very valuable, as an organised and predictable structure enables me to locate files easily. To reinforce a consistent folder structure, each new project is copied from a master template. The title and file name will then be renamed to reflect the project.

This Python script is written to facilitate this process to reduce time and error, ensures naming consistency and improve productivity.

# Pain Points
- Time is spent renaming files within each individual projects
- Messy file names, as sometimes the file names are not changed, either accidentally or because of convenience

# Features
- Written in Python
- PyQt5 GUI
- Copy from a designated template and replace template’s file name with the intended song title
- Ability to designate the template to be used

# Use Case
1. Open up the script
2. If the intended template is not the default, browse to the intended template to select the it.
3. Key in the project title, e.g Hai Kuo Tian Kong
4. Click “Create Folder”
5. Success message shown, and new project is now copied and file names inside are renamed. The new project will be created at the same location as the template.

# Releases
## Current Release
### v1.0.0
  - Refactor hard-coded code
  - Read stats from csv
  
## Previous Releases
### v0.0.0 
  - Working alpha build
