# This Python file uses the following encoding: utf-8
#
# reverse keyboard layout map (char to keys)
# mapping of a single character to keystroke(s) (combination) for a language dependent keyboard layout
# Note: only characters which can be typed with a given keyboard-layout shall be mapped (printable chars)
#
# LAYOUT: default GERMAN keyboard T1
#
# raw information is based on: https://msdn.microsoft.com/en-us/library/ms892159.aspx

chartable = { # entry for every char contains pairs of string list (modifier key combination(s) and keycode
   # which need to be pressed on the specific keyboard layout to "produce" this character

   # possible modifier keys are:
   #    mod key  | index
   # ____________|_____________________
   # R_GUI		 = 0 highest bit (x * 7^2)
   # R_ALT		 = 1
   # R_Shift     = 2
   # R_Control   = 3
   # L_GUI       = 4
   # L_ALT       = 5
   # L_Shift     = 6
   # L_Control   = 7 lowest bit (x * 0^2)
   # scancodes are HID keycodes as in keymap.py
   # multiple pairs are necessary if a char is created with a dead key e.g. grave
    u"\t" : [ [[],43] ] ,
    u"\n" : [ [[],40] ] ,

    u" " : [ [[],44] ] ,
    u"^" : [ [[],53] ] ,
    u"1" : [ [[],30] ] ,
    u"2" : [ [[],31] ] ,
    u"3" : [ [[],32] ] ,
    u"4" : [ [[],33] ] ,
    u"5" : [ [[],34] ] ,
    u"6" : [ [[],35] ] ,
    u"7" : [ [[],36] ] ,
    u"8" : [ [[],37] ] ,
    u"9" : [ [[],38] ] ,
    u"0" : [ [[],39] ] ,
    u"ß" : [ [[],45] ] ,
    u"´" : [ [[],46] ] ,
    u"q" : [ [[],20] ] ,
    u"w" : [ [[],26] ] ,
    u"e" : [ [[],8] ] ,
    u"r" : [ [[],21] ] ,
    u"t" : [ [[],23] ] ,
    u"z" : [ [[],28] ] ,
    u"u" : [ [[],24] ] ,
    u"i" : [ [[],12] ] ,
    u"o" : [ [[],18] ] ,
    u"p" : [ [[],19] ] ,
    u"ü" : [ [[],47] ] ,
    u"+" : [ [[],48] ] ,
    u"#" : [ [[],50] ] ,
    u"a" : [ [[],4] ] ,
    u"s" : [ [[],22] ] ,
    u"d" : [ [[],7] ] ,
    u"f" : [ [[],9] ] ,
    u"g" : [ [[],10] ] ,
    u"h" : [ [[],11] ] ,
    u"j" : [ [[],13] ] ,
    u"k" : [ [[],14] ] ,
    u"l" : [ [[],15] ] ,
    u"ö" : [ [[],51] ] ,
    u"ä" : [ [[],52] ] ,
    u"y" : [ [[],29] ] ,
    u"x" : [ [[],27] ] ,
    u"c" : [ [[],6] ] ,
    u"v" : [ [[],25] ] ,
    u"b" : [ [[],5] ] ,
    u"n" : [ [[],17] ] ,
    u"m" : [ [[],16] ] ,
    u"," : [ [[],54] ] ,
    u"." : [ [[],55] ] ,
    u"-" : [ [[],56] ] ,
    u"<" : [ [[],100] ] ,
    u"!" : [ [["L_Shift"],30] ] ,
    u"\"" : [ [["L_Shift"],31] ] ,
    u"§" : [ [["L_Shift"],32] ] ,
    u"$" : [ [["L_Shift"],33] ] ,
    u"%" : [ [["L_Shift"],34] ] ,
    u"&" : [ [["L_Shift"],35] ] ,
    u"/" : [ [["L_Shift"],36] ] ,
    u"(" : [ [["L_Shift"],37] ] ,
    u")" : [ [["L_Shift"],38] ] ,
    u"=" : [ [["L_Shift"],39] ] ,
    u"?" : [ [["L_Shift"],45] ] ,
    u"Q" : [ [["L_Shift"],20] ] ,
    u"W" : [ [["L_Shift"],26] ] ,
    u"E" : [ [["L_Shift"],8] ] ,
    u"R" : [ [["L_Shift"],21] ] ,
    u"T" : [ [["L_Shift"],23] ] ,
    u"Z" : [ [["L_Shift"],28] ] ,
    u"U" : [ [["L_Shift"],24] ] ,
    u"I" : [ [["L_Shift"],12] ] ,
    u"O" : [ [["L_Shift"],18] ] ,
    u"P" : [ [["L_Shift"],19] ] ,
    u"Ü" : [ [["L_Shift"],47] ] ,
    u"*" : [ [["L_Shift"],48] ] ,
    u"'" : [ [["L_Shift"],50] ] ,
    u"A" : [ [["L_Shift"],4] ] ,
    u"S" : [ [["L_Shift"],22] ] ,
    u"D" : [ [["L_Shift"],7] ] ,
    u"F" : [ [["L_Shift"],9] ] ,
    u"G" : [ [["L_Shift"],10] ] ,
    u"H" : [ [["L_Shift"],11] ] ,
    u"J" : [ [["L_Shift"],13] ] ,
    u"K" : [ [["L_Shift"],14] ] ,
    u"L" : [ [["L_Shift"],15] ] ,
    u"Ö" : [ [["L_Shift"],51] ] ,
    u"Ä" : [ [["L_Shift"],52] ] ,
    u"Y" : [ [["L_Shift"],29] ] ,
    u"X" : [ [["L_Shift"],27] ] ,
    u"C" : [ [["L_Shift"],6] ] ,
    u"V" : [ [["L_Shift"],25] ] ,
    u"B" : [ [["L_Shift"],5] ] ,
    u"N" : [ [["L_Shift"],17] ] ,
    u"M" : [ [["L_Shift"],16] ] ,
    u";" : [ [["L_Shift"],54] ] ,
    u":" : [ [["L_Shift"],55] ] ,
    u"_" : [ [["L_Shift"],56] ] ,
    u">" : [ [["L_Shift"],100] ] ,
    u"²" : [ [["R_ALT"],31] ] ,
    u"³" : [ [["R_ALT"],32] ] ,
    u"{" : [ [["R_ALT"],36] ] ,
    u"[" : [ [["R_ALT"],37] ] ,
    u"]" : [ [["R_ALT"],38] ] ,
    u"}" : [ [["R_ALT"],39] ] ,
    u"\\" : [ [["R_ALT"],45] ] ,
    u"@" : [ [["R_ALT"],20] ] ,
    u"€" : [ [["R_ALT"],8] ] ,
    u"~" : [ [["R_ALT"],48] ] ,
    u"µ" : [ [["R_ALT"],16] ] ,
    u"|" : [ [["R_ALT"],100] ] ,
    u"â" : [ [[],53], [[],4] ],
    u"ê" : [ [[],53], [[],8] ],
    u"î" : [ [[],53], [[],12] ],
    u"ô" : [ [[],53], [[],18] ],
    u"û" : [ [[],53], [[],24] ],
    u"Â" : [ [[],53], [["L_Shift"],4] ],
    u"Ê" : [ [[],53], [["L_Shift"],8] ],
    u"Î" : [ [[],53], [["L_Shift"],12] ],
    u"Ô" : [ [[],53], [["L_Shift"],18] ],
    u"Û" : [ [[],53], [["L_Shift"],24] ],
    u"^" : [ [[],53], [[],44] ],
    u"á" : [ [[],46], [[],4] ],
    u"é" : [ [[],46], [[],8] ],
    u"í" : [ [[],46], [[],12] ],
    u"ó" : [ [[],46], [[],18] ],
    u"ú" : [ [[],46], [[],24] ],
    u"ý" : [ [[],46], [[],29] ],
    u"Á" : [ [[],46], [["L_Shift"],4] ],
    u"É" : [ [[],46], [["L_Shift"],8] ],
    u"Í" : [ [[],46], [["L_Shift"],12] ],
    u"Ó" : [ [[],46], [["L_Shift"],18] ],
    u"Ú" : [ [[],46], [["L_Shift"],24] ],
    u"Ý" : [ [[],46], [["L_Shift"],29] ],
    u"´" : [ [[],46], [[],44] ],
    u"à" : [ [["L_Shift"],46], [[],4] ],
    u"è" : [ [["L_Shift"],46], [[],8] ],
    u"ì" : [ [["L_Shift"],46], [[],12] ],
    u"ò" : [ [["L_Shift"],46], [[],18] ],
    u"ù" : [ [["L_Shift"],46], [[],24] ],
    u"À" : [ [["L_Shift"],46], [["L_Shift"],4] ],
    u"È" : [ [["L_Shift"],46], [["L_Shift"],8] ],
    u"Ì" : [ [["L_Shift"],46], [["L_Shift"],12] ],
    u"Ò" : [ [["L_Shift"],46], [["L_Shift"],18] ],
    u"Ù" : [ [["L_Shift"],46], [["L_Shift"],24] ],
    u"`" : [ [["L_Shift"],46], [[],44] ],
}

# Map modifier keys to array element in the bit array
modkeys = {
    "KEY_RIGHTMETA": 0,
    "KEY_RIGHTALT": 1,
    "KEY_RIGHTSHIFT": 2,
    "KEY_RIGHTCTRL": 3,
    "KEY_LEFTMETA": 4,
    "KEY_LEFTALT": 5,
    "KEY_LEFTSHIFT": 6,
    "KEY_LEFTCTRL": 7
}


def convert(evdev_keycode):
    return keytable[evdev_keycode]


def modkey(evdev_keycode):
    if evdev_keycode in modkeys:
        return modkeys[evdev_keycode]
    else:
        return -1  # Return an invalid array element
