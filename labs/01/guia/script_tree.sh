#!/bin/bash

mkdir lab

mkdir lab/prog
mkdir lab/prog/deprecated
mkdir lab/prog/working

mkdir lab/example
mkdir lab/example/recovered

mkdir lab/data
mkdir lab/data/last
mkdir lab/data/dummy

chmod 444 lab/prog/deprecated
chmod 244 lab/prog/working
chmod 444 lab/prog
chmod 125 lab/example/recovered
chmod 345 lab/example
chmod 345 lab/data/last
chmod 125 lab/data/dummy
chmod 244 lab/data
chmod 700 lab
