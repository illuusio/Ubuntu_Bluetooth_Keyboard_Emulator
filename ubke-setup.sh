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

sleep 40s

while true
do
    UBKE_HCICONFIG=$(hciconfig)
    if [ -n "${UBKE_HCICONFIG}" ]
    then
        echo "Bluetooth 'hciX' is available"
        break
    else
        echo "Bluetooth waiting for adapter 10 seconds"
    fi
    sleep 10s
done

echo "Setup Bluetooth adapter act as keyboard named: '$UBKE_KB_NAME'"

hciconfig hcio up
hciconfig hcio class 0x002540
hciconfig hcio name "$UBKE_KB_NAME"

# Make keyboard findable
hciconfig hcio piscan

