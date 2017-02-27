# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > Attaching the [cheatsheet](https://goo.gl/Vmx5Sv) I made for my Unix/Linux course a few years ago.

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > **ls** lists files under the current directory  

> > **ls -a** lists files under the current directory including hidden files

> > **ls -l** lists files under the current directory along with file details  

> > **ls -lh** is the same as **ls -l** except the **h** option prints out the file sizes in human-readable format  

> > **ls -lah** lists files under the current directory including hidden files along with file details with file sizes in human-readable format  

> > **ls -t** lists files under the current directory sorted by file modification timestamp in descending order  

> > **ls -Glp** lists files under the current directory with the following specifications: 1. print out file details but omit the group ID 2. append file type indicator (e.g. foo/ means foo is a directory) after each of the listed file names

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > **ls -R** lists files recursively

> > **ls -r** lists files under the current directory sorted by file name in descending order

> > **ls -d** lists only directories under the current directory

> > **ls -m** lists files under the current directory in a comma-separated format

> > **ls -i** lists files under the current directory along with their inode information

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > **xargs** converts standard inputs into command arguments. For example, in `echo foo.txt | xargs touch`, **xargs** converts the standard input, **foo.txt** into the argument for **touch**. In contrast, some commands, such as **grep**, can process standard inputs directly; for example `ls | grep .md`. In these cases, **xargs** is not needed.

 
