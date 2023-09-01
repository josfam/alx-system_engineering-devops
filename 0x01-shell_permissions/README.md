# 0x01.Shell, permissions
---
## What each script does
### `0-iam_betty`
Switches the current user to the user `betty`.
### `1-who_am_i`
Prints the effective username of the current user.
### `2-groups`
Prints all the groups the current user is part of.
### `5-execute`
Adds execute permission to the owner of the file `hello`.
### `6-multiple_permissions`
Adds execute permission to the owner and the group owner, and read permission to other users, 
\
to the file `hello`.
### `7. Everybody!`
Adds execution permission to the owner, the group owner and the other users, to the file `hello`.
### `8-James_Bond`
Sets the permission to the file hello as follows:

Owner: no permission at all
Group: no permission at all
Other users: all the permissions
### `9-John_Doe`
Sets the mode of the file `hello` to this:
```
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
```
### `10-mirror_permissions`
Sets the mode of the file `hello` the same as `olleh`’s mode.
### `11.11-directories_permissions`
adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.

Regular files should not be changed.
### `12-directory_permissions`
Creates a directory called `my_dir` with permissions 751 in the working directory.
### `13. Change group`
Script that changes the group owner to `school` for the file `hello`.
### `14. 100-change_owner_and_group`
Changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory.

