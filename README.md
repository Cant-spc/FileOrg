# Filefix :
A Python library to organize files in a directory based on their file type.
It will help to organize and manage files in a more organized way so that users can easily find and access their files.

## Features :

- Organize files in a directory based on their file type.
- Clear the directory by removing empty directories.
- Show statistics about files in the directory.
- Add a new file category.
- Remove a file category.
- Undo organize files in a directory.
- List all file categories and their extensions.
- Create a folder structure based on a YAML template.(!note always use a (YAML File Tree with Inline Content))

## Installation :
```
pip install filefix
```
## Image :
![Image](/test/Images/testcase.png)

## Usage :
```
filefix organize "<directory>"
filefix clean "<directory>"
filefix stats "<directory>"
filefix add-category <extension> <category>
filefix remove-category <extension>
filefix undo-organize "<directory>"
filefix list-categories "<directory>"
filefix create-structure <template_path> <target_dir> (!note always use a (YAML File Tree with Inline Content))

```
## Contributing : 
(Open Source Project) Anyone can contribute to this project. 

- Fork the repository.
- Create a new branch.
- Make your changes.
- Commit your changes.
- Push your changes.
- Create a pull request.

