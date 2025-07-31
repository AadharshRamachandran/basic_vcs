# 🗃️ File Version Control System (VCS) in C++

A lightweight Git-like version control system built from scratch in C++. This system supports core VCS features including staging, committing, branching, logging, diffs, and server-side remote functionality.

---

## ✨ Features

- ✅ Initialize a repository (`init`)
- ✅ Stage and commit files with messages
- ✅ View commit history (`log`)
- ✅ Checkout specific file versions by commit
- ✅ Manage multiple branches
- ✅ Detect and display file changes (`diff`)
- ✅ Track per-file commit graphs using diffs
- ✅ Start/Stop a local repository server
- ✅ Clone, push to, and pull from remote repositories

---

## 🛠️ CLI Commands

| Command                                | Description                                 |
|----------------------------------------|---------------------------------------------|
| `init`                                 | Initialize a new repository                 |
| `add <filename>`                       | Stage a file                                |
| `commit <message>`                     | Commit staged files with a message          |
| `log`                                  | Show commit history                         |
| `checkout <file> <commit>`             | Checkout a specific version of a file       |
| `status`                               | Show repository status                      |
| `createbranch <branch>`                | Create a new branch                         |
| `switch <branch>`                      | Switch to another branch                    |
| `current-branch`                       | Show the currently active branch            |
| `branches`                             | List all branches                           |
| `files`                                | List all tracked files                      |
| `diff <filename>`                      | Show changes between staged and committed   |
| `clone <remote> <local>`               | Clone a repository from a remote source     |
| `push [remote]`                        | Push changes to a remote repository         |
| `pull [remote]`                        | Pull changes from a remote repository       |
| `start`                                | Start the repository server                 |
| `stop`                                 | Stop the repository server                  |

---
