# Linux Commands

## Configuration

| Command                                               | Purpose
| --                                                    | --
| `export <ENVIRONMENT_VARIABLE_NAME>=<VALUE>`          | set environment variable
| `echo  $<ENVIRONMENT_VARIABLE_NAME>`                  | see environment variable value

## File & Directory

| Command                               | Purpose
| --                                    | --
| `pwd`                                 | current directory
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



