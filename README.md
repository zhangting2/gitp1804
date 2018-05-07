…or create a new repository on the command line
...
 echo "# gitp1804" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/zhangting2/gitp1804.git
git push -u origin master
...

…or push an existing repository from the command line
...
 git remote add origin https://github.com/zhangting2/gitp1804.git
git push -u origin master
...
以后经常使用的命令是
git add .
git commit -m "提交的内容说明"
git push -u origin master
