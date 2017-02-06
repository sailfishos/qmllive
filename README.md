# QmlLive

QmlLive is a system to automatically reload a QtQuick user interface on every
document save.

It is available for the PC but also for an embedded device, which supports Qt5.

More information is available form documentation (see install instructions).

Copyright (C) 2016 Pelagicore AG


## Contribution guidelines

This repository contains Qt QmlLive specifically tailored for Sailfish OS
application development.

These rules are followed so that all commits are ready for cherry-picking
upstream:

1. Always include the Gerrit's Change-Id header in the commit message.

   Install a GIT commit hook to your clone of this repository to automate this:
   `scp -p codereview.qt-project.org:hooks/commit-msg .git/hooks/`. More
   info [here](https://wiki.qt.io/Setting_up_Gerrit#Setting_up_git_hooks).

2. Use annotated tags for Sailfish OS change log autogeneration.

   Do not include the `[SHORT-DESC] LONG-DESC BUG-REF` lines in commit messages.
   Store then in tag annotations instead.

Also avoid creating real merges for pull requests. Our branch is regularly
cleaned with an approach similar to what is described
[here](https://die-antwort.eu/techblog/2016-08-git-tricks-for-maintaining-a-long-lived-fork/)
and merges would not be preserved. For those who care: related commits are
already grouped with (annotated) tags.
