#!/bin/bash

for x in *.stan
do
    pygmentize -f html -O full,style=emacs -l stan -o ${x%.stan}.html $x
done
