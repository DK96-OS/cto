# Commit-Text-Organizer
Do you like to organize your commit messages?
Follow this simple system while creating your commit messages, and then when it comes time to squash your commits, run Commit-Text-Organizer to clean and categorize all of those messages.

## Requirements
Python 3.10 or 3.11 is required to run __Commit-Text-Organizer__.
This is because the Union Type Operator is used (not available in 3.9 or earlier).

## Commit Message Structure
Structure your commits using your own set of headers.

- A header ends with a colon ":"
- Lines under the header are part of that header Group
- A blank line will start a new group

### Subjects
A Subject is the start of a Line in a header Group.

- The subject is separated from details by one of these separators (+ or -)
- Lines with the same Header and Subject are automatically merged
- Details after the subject are comma-separated

### Example
__Input:__
```
Header 1:
* Modify File.c - new method hello_world()
* Modify File.c - new method foo()

Header 2:
* Create NewFile.c

Header 2:
* Modify NewFile.c - add method bar()
```
__Output:__
```
Header 1:
* Modify File.c - new method hello_world(), new method foo()

Header 2:
* Create NewFile.c
* Modify NewFile.c - add method bar()
```

### Sorting
The sort method of CommitOrganizer will combine groups with matching headers.
The sort lines in groups method of CommitTextGroup will sort the group's messages alphabetically. 

### Python Script
The Python script reads and runs Commit-Text-Organizer on a file of your choosing.

The script will prompt user for the path of the file to read.
The output will be written to a similar path with a "-organized" suffix. (sorry windows users, this currently messes up the file extension)
