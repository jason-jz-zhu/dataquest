# return to home path
cd ~

# create folder
mkdir

# remove folder
rmdir

# create file
touch

# write soemthing into file and overwrite the file
echo 'All bears should juggle' > test.txt
# write soemthing into file and not overwrite the file
echo 'All bears should juggle' >> test.txt

# ide to edit file
nano

# see detail file info
ls -l

# change permission
chmod 0760 test.txt

# move file
mv text.txt test

# copy file
cp test/test.txt test/test2.txt

# rename file
mv test/test.txt test/test_no_extension

# delete a file
rm /home/dq/test/test2.txt

# create variable
FOOD="Shrimp gumbo"

# print variable
echo $FOOD

# create environment variable
export FOOD="Chicken and waffles"

# python get environment variable
import os
print(os.environ["FOOD"])

# check PATH
echo $PATH

# list all deatil info with ignore
ls -al --ignore=.ipython

# create one csv and transfer the head to it
head -1 Hud_2005.csv > combined_hud.csv
# check the length of one file
wc -l Hud_2005.csv
# transfer many line to one file
tail -46853 Hud_2005.csv >> combined_hud.csv

# Count and display the number of lines in combined_hud.csv containing 1980-1989.
grep '1980-1989' combined_hud.csv | wc -l
