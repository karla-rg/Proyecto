#!/bin/bash
ANTLR=../../../../antlr-4.9.3-complete.jar

java -cp "$ANTLR:." org.antlr.v4.gui.TestRig marzo program -gui
