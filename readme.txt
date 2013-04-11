please download file from https://www.dropbox.com/s/hvx8mrdu9snz2nb/subcats.txt
the file looks like:
(691898,'Fields_of_mathematics','GRAPH THEORY','2012-02-01 22:52:02','','uppercase','subcat')
We need the second and third fields. And in order to keep consistent, we need to change the format of the second field to all upper case and separate by space.
so Fields_of_mathematics would become FIELDS OF MATHEMATICS 

please use 'cat sub cats.txt | python buildDAG.py' to run the code