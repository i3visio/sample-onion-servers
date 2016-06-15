Contributing to the project
===========================

Reporting issues, bugs and fresh ideas
--------------------------------------

The way in which we track the issues regarding the software is by means of the issues page in Github's project site.
Whether you have experimented problems with the installation, you have found a bug in a new platform or you feel that we can add a new functionality, you can find the place to report them there. The only "rule" is to notify one error per issue to be able to track the problems independently, as well as trying to provide as much information as possible regarding the OS or version you are trying.

If you find that a transform in Maltego is not behaving as expected, we recommend you to set the debug mode as True. Go to Manage --> Manage Transforms, choose the transform and mark the "Set debug info" as True. Please, copy the information shown in the new tab in the issue so as to provide more information to debug it faster.

Contributing code
-----------------

Whether you want to add a new wrapper or fix a bug, the basic instructions to contribute and perform a pull request on Github are the following (we assume that you have installed Git by yourself, so please follow the instructions in the project's website to install it on your system <https://git-scm.com/downloads>). We will assume that the username for this test is `youruser`.

First of all, logged in Github and fork the repository by pressing the corresponding button. This will create a copy of the repository under your profile (i. e.: `https://github.com/youruser/repository`).

You can clone your forked repository now:
```
# This is an example! Change "youruser" for your nick!
git clone https://github.com/youruser/repository
cd osrframework
```

Then, you can modify any file you want, for example, the `README.md`.
```
# Opening it with nano...
nano README.md
```

After the apprpriate changes have been performed, you can test the installation with pip.
```
pip install -e ./
```

Whenever you want, you can add the changes performed to the Git index to keep track of what you have changed and prepar it for the commit.
```
# Add one file
git add ./README.md
# Or adding all the files modified... Just be a lil' bit more careful
# git add -A
```

Once you are happy with the changes (and you have tested them!), you can commit the changes with a descriptive message.
```
git commit -m "Fixing issue #0: modifications in the README.md file."
```

You have to push the changes to your Github project.
```
git push origin
```

You're almost there. You can now go to your project's website (`http://github.com/osrframework_contributor/osrframework`) and click in the `Pulls` tab or going directly to it by appending `pulls` to your forked URL, something similar to `https://github.com/youruser/repository/pulls`. Then provide there as much detail as you can about the contents of the pull request and shortly we will evaluate the changes and pushed it upstream.

Extending OSRFramework
----------------------

This section will provide information about how to extend the different tools found in the framework.

Style guide
-----------

Just a few things to be taken into account:
* Use four spaces '    ' instead of a tab for identing blocks.
* Provide useful and not trivial comments in English to the code you write.
* Classes should start with a capitalised initial letter.
* As a convention, wrappers inside the `platform_selection.py` should be in alphabetical order. Anyone wants to find things easily!

Licensing
---------

The only thing we expect from other authors'code is to use a GPL-compatible license for their code, preferably GPLv3+ itself. We hope that anybody can use this tool for free (as in Free Software Foundation's four freedoms, not as in *free beer*), so help us to do it.
