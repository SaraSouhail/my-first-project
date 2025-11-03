#  1
# the white file first_file.py means it is added to github 
# the red / orange file second_file.py means it is  been added to gihtub  but u modify it (like i do now when i write thse comments)
# the green file third_file.py means it is not been added to gihtub repo yet 

# 2
# so git status  show the files "deleted" and the file "modified" locally in vscode 
# and show finally the "untracked" files ( like the third )
# example from terminal :
# Changes not staged for commit:
#   (use "git add/rm <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
#         deleted:    first_file.py
#         modified:   second_file.py

# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         third_file.py

# 3
# so i put my self on a prblm 
# i want Restore first_file.py from GitHub (because i deleted it locally by mistake hihi) solution : (git restore first_file.py)
# Commit and push changes to second_file.py
# Add third_file.py and push it

