## Commit Text Organizer
Do you like to organize your commit messages? __CTO does!__

CTO likes commit messages in a readable format. The format is called FOCI.

### File Oriented Commit Information (FOCI)
___A Commit may target multiple files, but it has only one purpose.___

<details>
<summary>FOCI Concepts</summary>

- __Headers__
  - Signify the start of a commit message group
  - Make it easier to categorize and locate related changes
- __Commit Lines__
  - Lines grouped together under each header
  - Detail changes to files or groups of files
  - Enhancing traceability and readability
- __Subjects__
  - The start of a Commit Line
  - Indicating the file or group of files
  - Allowing for quick identification of affected areas
- __Content Details__
  - The end of a Commit Line
  - Comma separated list of text describing specific changes
  - Providing clarity on the nature of the modification.
</details>

CTO and FOCI ensure that commit messages are well-organized and convey the intended changes in a clear, concise manner. This is key to making revision history easy to revisit.

## Commit Message Structure
At a high level, messages are organized into groups.

<details>
<summary>Each group has a unique header name.</summary>

### Headers
Structure your commits using your own set of headers, such as:
- Database Migration 32
- Database Integration
- Test Database Migrations

When writing commits, ensure that you add a colon (:) immediately after the header name.

Then, the lines immediately below the header are included in that group. These are called Commit Lines.
</details>
<details>
<summary>A Commit Line starts with a subject, corresponding to a file, or group of files.</summary>
     
### Subjects (Files or Groups of Files)
A Subject is the start of a Commit Line in a header Group. It will usually describe a change in a single file, but you can group files into the subject.

#### Subject Matching
Lines in the same Header Group can be merged, but only if the subjects match.

When Content details are merged, they are separated from the Subject, sorted alphabetically, and joined with a comma-space separator.

#### Subject Content Separators
The subject is separated from content details by one of these separators: (+) or (-).

If a separator appears more than once in a Commit Line, it is ignored.
</details>

<details>
<summary>A subject may include a verb, such as "Update", which can be replaced with a prefix shortcut.</summary>

### Commit Line Prefix Shortcuts
To reduce typing the same word for so many file changes (such as "Update", or "Create"), CTO includes a Line Prefix recognition and replacement feature.

     cto/text/commit_line_prefixes.py  

It recognizes prefixes (that you can change) and replaces them with the most commonly used words.

#### Commit Line Prefix Shortcuts
| Shortcut | Prefix |
|----------|--------|
| c | Create |
| d | Delete |
| f | Fix |
| m | Move |
| r | Remove |
| t | Test |
| u | Update |
| cr | Create |
| del | Delete |
| mv | Move |
| up | Update |
</details>

#### Important Commit Line Characters
- A header ends with a colon ":"
- A blank line will start a new group
- Commit Lines start with the star (*)
- Subject is separated from content by (+) or (-)
- Content may contain multiple changes that are comma-separated

### Sorting
By default, your squashed PR message will have groups organized alphabetically by their header names.
- Subjects within each group are sorted alphabetically
- Sorting is done after applying Commit Line Prefix Shortcuts.

## Example
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

## How It Works
1. __Launch Script__: The user starts by running the launch.py script, which prompts for a file path. This file contains the commit messages to be organized.
2. __Commit Message Structure__: Commit messages are organized into groups defined by headers (e.g., "Database Migration 32"). Each group contains commit lines starting with a star (*) and details changes to subjects (files or groups of files).
3. __Subject Matching and Content Details__: Commit lines within the same header group can be merged if their subjects match. The tool sorts and joins content details alphabetically, separated by a comma-space.
4. __Line Prefix Shortcuts__: To simplify repetitive prefixes like "Update" or "Create", CTO includes a feature to recognize and replace line prefix shortcuts with their full forms (e.g., "c" for "Create").
5. __Sorting and Output__: The tool sorts groups and lines within groups alphabetically. The output is written to a new file with a "-org" suffix, containing the organized commit messages.

### Requirements
Python 3.10 or higher is required to run __Commit-Text-Organizer__.
This is because the Union Type Operator is used (not available in 3.9 or earlier).

### Windows Compatibility
The file extension must be (.txt).

## Project Vision
To enhance developer usability and broaden its applicability.
Enhancements aim to make CTO more versatile, user-friendly, and integrated with developers' workflows.
- Develop a more robust CLI experience
- Introduce command-line help documentation
- Implement a feature to directly read commit messages from a branch
- Allow users to add their own prefix shortcuts in a config file
