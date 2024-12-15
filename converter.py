import sys

indent =   "    "   #derzeitige einrückung
name = "Keyboard."  #name der Keyboard Bibliothek
needed_delay = 50   #delay needed to not skip inputs 
n = ";\n"           #weil ich keine lust habe \ zu drücken
def duden(wort):    #https://docs.arduino.cc/language-reference/de/en/functions/usb/Keyboard/keyboardModifiers/
    if len(wort)==1:
        return "\"" + wort + "\""
    match wort:
        case "shift":
            return "KEY_LEFT_SHIFT"
        case "ctrl":
            return "KEY_LEFT_CTRL"
        case "alt":
            return "KEY_LEFT_ALT"
        case "option":
            return "KEY_LEFT_ALT"
        case "win":
            return "KEY_LEFT_GUI"
        case "ios":
            return "KEY_LEFT_GUI"
        case "tab":
            return "KEY_TAB"
        case "caps":
            return "KEY_CAPS_LOCK"
        case "back":
            return "KEY_BACKSPACE"
        case "enter":
            return "KEY_RETURN"
        case "rclick":
            return "KEY_MENU"
        case "strgv":
            return "KEY_INSERT"
        case "del":
            return "KEY_DELETE"
        case "home":
            return "KEY_HOME"
        case "end":
            return "KEY_END"
        case "scrollu":
            return "KEY_PAGE_UP"
        case "scrolld":
            return "KEY_PAGE_DOWN"
        case "up":
            return "KEY_UP_ARROW"
        case "down":
            return "KEY_DOWN_ARROW"
        case "left":
            return "KEY_LEFT_ARROW"
        case "right":
            return "KEY_RIGHT_ARROW"
        case "esc":
            return "KEY_ESC"
        case "pause":
            return "KEY_PAUSE"
        case "F1":
            return "KEY_F1"
        case "F2":
            return "KEY_F2"
        case "F3":
            return "KEY_F3"
        case "F4":
            return "KEY_F4"
        case "F5":
            return "KEY_F5"
        case "F6":
            return "KEY_F6"
        case "F7":
            return "KEY_F7"
        case "F8":
            return "KEY_F8"
        case "F9":
            return "KEY_F9"
        case "F10":
            return "KEY_F10"
        case "F11":
            return "KEY_F11"
        case "F12":
            return "KEY_F12"
        case "F13":
            return "KEY_F13"
        case "F14":
            return "KEY_F14"
        case "F15":
            return "KEY_F15"
        case "F16":
            return "KEY_F16"
        case "F17":
            return "KEY_F17"
        case "F18":
            return "KEY_F18"
        case "F19":
            return "KEY_F19"
        case "F20":
            return "KEY_F20"
        case "F21":
            return "KEY_F21"
        case "F22":
            return "KEY_F22"
        case "F23":
            return "KEY_F23"
        case "F24":
            return "KEY_F24"
        case _:
            print("duden hat nicht enthaltenes Wort erhalten: " + wort)
            sys.exit()
            return ""



crack_name = input("Crackname:\n")

file_t_dir = "./Text/"+crack_name+"_T.txt"
file_c_dir = "./Code/"+crack_name+"_C.txt"

file_t = open(file_t_dir,"r")
txt = file_t.readlines()
file_t.close()

for i in range(len(txt)):
    txt[i] = txt[i].replace("\n", "")

file_c = open(file_c_dir,"w")
file_c.write("// Crackname: "+ txt[0] + "\n")
file_c.write("void " + txt[2] + "_" + txt[1] + "() { \n")

for index in range(3,len(txt),2):
    print(txt[index]+": "+txt[index+1])
    match txt[index]:
        case "text":
            file_c.write(indent+name+"print(\""+txt[index+1]+"\")"+n)
        case "textl":
            file_c.write(indent+name+"println(\""+txt[index+1]+"\")"+n)
        case "comb":
            comb_list = txt[index+1].split()
            for index2 in range (0,len(comb_list),1):
                file_c.write(indent+name+"press("+duden(comb_list[index2])+")"+n)
                file_c.write(indent+"delay("+str(needed_delay)+")"+n)
            file_c.write(indent+name+"releaseAll()"+n)
        case "stroke":
            file_c.write(indent+name+"write("+duden(txt[index+1])+")"+n)
        case "hold":
            file_c.write(indent+name+"press("+duden(txt[index+1])+")"+n)
        case "rel":
            file_c.write(indent+name+"release("+duden(txt[index+1])+")"+n)
        case "relall":
            file_c.write(indent+name+"releaseAll()"+n)
        case "wait":
            file_c.write(indent+"delay("+txt[index+1]+")"+n)
        case "rep":
            if indent == "    " :
                file_c.write(indent+"while(1) {"+n)
                indent = indent + "    "
            else:
                print("Fehler in "+ file_t_dir + " zeile " + index + ". Nur eine Endlosschleife erlaubt!")
                sys.exit()
        case _:
            print("Befehl nicht erkannt: " + txt[index] + " zeile " + str(index))
            sys.exit()
    file_c.write(indent+"delay("+str(needed_delay)+")"+n)

if indent == "        ":
    file_c.write("    }" + n)
file_c.write("}")
file_c.close()



