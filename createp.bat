@echo off

echo Creating project folder '%1'...

set initialpath=%cd%

cd C:\Projects\
mkdir %1
if ERRORLEVEL 1 goto END

cd C:\Projects\%1\
echo # %1> README.md

echo Initialising git...
git init
git add .
git commit -m "Initial Commit"

python C:\Projects\cli-commands\createp_linkgithub.py %1

git push -u origin master

code .

:END
cd %initialpath%