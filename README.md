…or create a new repository on the command line
echo "# Peloton" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/kotbeg/Peloton.git
git push -u origin master
…or push an existing repository from the command line
git remote add origin https://github.com/kotbeg/Peloton.git
git push -u origin master

# Exercises

### ex_2 is modified to assert that the submitted results are coherent, though I did not add more tests.

### ex_3 checks the existence of a gif with #cute, if nothing returned = passed, else the assertionError shown.

### Using selenium and time libraries only, could do implicitly_wait() instead of the time.sleep() but newer version of selenium is not my friend at this moment. This I might update a little later today.