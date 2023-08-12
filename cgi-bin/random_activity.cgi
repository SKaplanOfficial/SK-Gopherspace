#!/bin/ksh
/usr/pkg/bin/perl -e 'srand; rand($.) < 1 && ($line = $_) while <>; print $line;' data/activities.txt