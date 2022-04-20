#!/bin/bash
ANTLR=../../../../antlr-4.9.3-complete.jar
java -jar $ANTLR marzo.g4
javac -cp $ANTLR *.java
