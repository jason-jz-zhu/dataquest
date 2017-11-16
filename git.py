# We can use git rev-parse along with the HEAD variable to
# find the commit hash corresponding to a particular commit number.
# In the diagram above, git rev-parse HEAD will return 646,
# and git rev-parse HEAD~3 will return c53.
git rev-parse HEAD

# reset commit to HEAD which we want
git reset --hard HEAD~1

# HEAD will revert the working directory to the state of the most recent commit
# HEAD~1 will get the second newest commit in the local repo,
# HEAD~2 will get the third newest commit


# create a branch
git branch rocky
# checkout branch
git checkout rocky
# create and checkout branch
git checkout -b rocky

# merge branch
git checkout master
git merge more-speech

# delete branch
git branch -d more-speech

# git fetch will fetch all of the current branches and commits from the remote.
# This won't make any changes to the working directory,
# but will update Git's list of branch names and commits.
git fetch

# git diff
git --no-pager diff master happy-bot


# When naming branches,
# it's common to use a prefix that describes the type of branch,
# then a slash, then the name of the feature or fix we're making.
git checkout -b feature/happy-bot
git checkout -b fix/remove-error
git checkout -b chore/add-analytics

# One way to resolve a conflict is to abort the merge altogether.
# We can do this with git merge --abort.
git merge --abort
