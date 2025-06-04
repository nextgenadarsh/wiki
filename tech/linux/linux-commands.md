# Linux Commands

## Configuration

| Command                                               | Purpose
| --                                                    | --
| `export <ENVIRONMENT_VARIABLE_NAME>=<VALUE>`          | set environment variable
| `echo  $<ENVIRONMENT_VARIABLE_NAME>`                  | see environment variable value

## File & Directory

| Command                               | Purpose
| --                                    | --
| `ls -l`                               | list segments. list files & directories in current directory
| `pwd`                                 | print working directory
| `cd <directory-name>`                 | change directory
| `mkdir <dir-name>`    | create new directory
| `rm <file-name>` | remove files or directories
| `touch <file-name>`   | create new empty file
| `cp <source-file> <destination-folder/>`  | copy files or directories
| `mv <old-file-name> <new-file-name>` | move or rename files or directories
| `cat <file-name>`   | display the file content
| `less <large-file-name>`    | view files instead of opening the file with scroll
| `head <file-name>`      | outputs first part of file
| `tail <file-name>`      | outputs last part of file
| `grep <pattern> <file-name>` | Global Regular Expression Print - search pattern in file
| `find <directory-name> <file-name>`   | search and locate the list of files
| `man <command>`    | display the user manual of any command
| `sudo <command>`    | perform tasks that require administrative or root permissions
| `df -h`   | display the amount of disk space used and available
| `du -sh </directory/*>`   | estimate file and directory space usage
| `ps -aux`   | provides information about the currently running processes
| `kill <process-id>`   | terminate processes manually
| `tar -cvf <file-name.tar> <directory-name>`    | create and extract .tar or .tar.gz archives
| `chmod <mode> <file-name>`  | change the permissions of a file or a directory
| `chown <username:groupname> <file-name>`  | change the owner and group of a file or directory
| `ssh <username@host>`  | Secure Shell - log into a remote machine
| `wget <url>`   | downloads files from the Web
| `curl -O <url>` | used to transfer data
| `top`    | show the Linux processes
| `alias <alias>='<command>'`   | create an alias (shortcut) for another command
| `echo "<content>"`  | display lines of text or string on standard output or a file
| `exit <statuss-code>`   | exit the shell where it is currently running
| ``
| `echo ~`                              | show user home directory

## Utilities

| Command                               | Purpose
| --                                    | --
| `echo -n <string> \| base64`          | base64 `encode` the input string. if you remove -n then it will append new line to input string.
| `echo -n <string> \| base64 --decode` | base64 `decode` the input string

## Filters
| Command                               | Purpose
| --                                    | --
| `grep <filter-text> -i`               | case-insensitive filter for filter-text



## Others
| Command                               | Purpose
| --                                    | --
| `ps aux`                              | view currently running processes



