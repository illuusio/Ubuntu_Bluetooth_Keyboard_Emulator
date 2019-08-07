#!/bin/bash
#
# Configures Bluetooth adapter
# to act as keyboard
#

if [ -n "$UBKE_KB_NAME" ]
then
    UBKE_KB_NAME="UBKE-keyboard"
fi

if [ -n "$1" ]
then
    UBKE_KB_NAME="$1"
fi

echo "Setup Bluetooth adapter with name: '$UBKE_KB_NAME'"

hciconfig hcio up
hciconfig hcio class 0x002540
hciconfig hcio name "$UBKE_KB_NAME"

# Make findable
hciconfig hcio piscan
