
import os #used to all external commands
import sys # used to exit the script
import dbus
import dbus.service
import dbus.mainloop.glib
import time
import thread
import keymap

R_GUI		= 0
R_ALT		= 1
R_Shift     = 2
R_Control   = 3
L_GUI       = 4
L_ALT       = 5
L_Shift     = 6
L_Control   = 7

class BtkStringClient():

        """simple client of the Bluetooth Keyboard Emulator
        writes a string to the BTK Keyboard
        http://yetanotherpointlesstechblog.blogspot.com
        """

        #constants
	KEY_DOWN_TIME=0.01
	KEY_DELAY=0.1


        def __init__(self):

            #the structure for a bt keyboard input report (size is 10 bytes)

            self.state=[
                    0xA1, #this is an input report
                    0x01, #Usage report = Keyboard
                    #Bit array for Modifier keys
                    [0, #Right GUI - Windows Key
                     0, #Right ALT
                     0, #Right Shift
                     0, #Right Control
                     0, #Left GUI
                     0, #Left ALT
                     0, #Left Shift
                     0],    #Left Control
                    0x00,   #Vendor reserved
                    0x00,   #rest is space for 6 keys
                    0x00,
                    0x00,
                    0x00,
                    0x00,
                    0x00]


	    self.scancodes={
		" ": "KEY_SPACE"
	     }


            #connect with the Bluetooth keyboard server
            print "setting up DBus Client"

            self.bus = dbus.SystemBus()
            self.btkservice = self.bus.get_object('org.yaptb.btkbservice','/org/yaptb/btkbservice')
            self.iface = dbus.Interface(self.btkservice,'org.yaptb.btkbservice')




        def send_key_state(self):

            """sends a single frame of the current key state to the emulator server"""

            bin_str=""
            element=self.state[2]
            for bit in element:
                    bin_str += str(bit)
            self.iface.send_keys(int(bin_str,2),self.state[4:10]  )


        def send_key_down(self, scancode):

            """sends a key down event to the server"""

            self.state[4]=scancode
            self.send_key_state()


        def send_key_up(self):

            """sends a key up event to the server"""

            self.state[4]=0
            self.send_key_state()

        def send_keystroke(self,scancode):

            """sends a keystroke to the server"""

            self.send_key_down(scancode)
            time.sleep( BtkStringClient.KEY_DOWN_TIME)
            self.send_key_up()
            time.sleep( BtkStringClient.KEY_DELAY)


        def send_key_test(self):

            """send euro sign"""
            self.state[2][R_ALT]=1
            self.send_keystroke(8)







	def send_string(self, string_to_send):

		for c in string_to_send:

			cu = c.upper()

			if(cu in self.scancodes):
				scantablekey = self.scancodes[cu]
			else:
			        scantablekey = "KEY_"+c.upper()

			print scantablekey

			scancode = keymap.keytable[scantablekey]
			self.send_key_down(scancode)
			time.sleep( BtkStringClient.KEY_DOWN_TIME)
			self.send_key_up()
			time.sleep( BtkStringClient.KEY_DELAY)




if __name__ == "__main__":


    if(len(sys.argv) <2):
        print "Usage: send_string <string to send> "
        dc = BtkStringClient()
        #dc.send_string('e')
        dc.send_keystroke(8)
        dc.send_key_test()
        exit()

    print "Setting up virtual Bluetooth kb emulator client"

    dc = BtkStringClient()

    string_to_send = sys.argv[1]

    print "Sending " + string_to_send

    dc.send_string(string_to_send)

    print "Done."
