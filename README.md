# Commit-Text-Organizer
Do you like to organize your commit messages?
Follow this simple system while creating your commit messages, and then when it comes time to squash your commits, run Commit-Text-Organizer to clean and categorize all of those messages.

## Requirements
Python 3.10 or higher is required to run __Commit-Text-Organizer__.
This is because the Union Type Operator is used (not available in 3.9 or earlier).

## Commit Message Structure
You commit messages are organized into high level groups, which are defined by their header name.

Structure your commits using your own set of headers, such as:
- Database Migration 32
- Database Integration
- Test Database Migrations

When writing commits, ensure that you add a colon (:) immediately after the header name.

Then, the lines immediately below the header are included in that group. These are called Commit Lines.

### Subjects (Files or Groups of Files)
A Subject is the start of a Commit Line in a header Group. It will usually describe a change in a single file, but you can group files into the subject.

#### Subject Matching
Lines in the same Header Group can be merged, but only if the subjects match.

When Content details are merged, they are separated from the Subject, sorted alphabetically, and joined with a comma-space separator.

#### Subject Content Separators
The subject is separated from content details by one of these separators: (+) or (-).

If a separator appears more than once in a Commit Line, it is ignored.

### Line Prefix Shortcuts
To reduce typing the same word for so many file changes (such as "Update", or "Create"), CTO includes a Line Prefix recognition and replacement feature.

     cto/text/generation/commit_line_prefixes.py  

It recognizes prefixes (that you can change) and replaces them with the most commonly used words.

#### Existing Prefixes
| Shortcut | Prefix |
|----------|--------|
| c | Create |
| f | Fix |
| m | Move |
| r | Remove |
| t | Test |
| u | Update |

#### Existing Secondary Prefixes
There are also secondary prefixes that can be based on more than one character, and map to other prefixes.

| Shortcut | Prefix |
|----------|--------|
| cr | Create |
| del | Remove |
| mv | Move |
| up | Update |

#### Important Commit Line Characters
- A header ends with a colon ":"
- A blank line will start a new group
- Commit Lines start with the star (*)
- Subject is separated from content by (+) or (-)
- Content may contain multiple changes that are comma-separated

### Example
__Input:__
```
Header 1:
*u File.c - new method hello_world()
*u File.c - new method foo()

Header 2:
*c NewFile.c

Header 2:
*r OldFile.c
```
__Output:__
```
Header 1:
* Update File.c - new method hello_world(), new method foo()

Header 2:
* Create NewFile.c
* Remove OldFile.c
```

### Sorting
The sort method of CommitOrganizer will combine groups with matching headers.
The sort lines in groups method of CommitTextGroup will sort the group's messages alphabetically. 

### Launch (Python) Script
The Launch script prompts user for a path, reads a file and runs Commit-Text-Organizer on it's contents. 

The output will be written to a similar file path with a "-org" suffix attached.

#### Windows Compatibility
The file extension must be (.txt).

## Project Vision
The vision for this project is to advance to a multi-functional command line tool and interface that does more commit message text management, so developers like you and me can do less.
