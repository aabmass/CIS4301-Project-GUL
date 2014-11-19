#!/bin/sh
# Argument passed is the username
ssh -L 1521:oracle.cise.ufl.edu:1521 $1@storm.cise.ufl.edu
