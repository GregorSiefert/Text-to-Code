import sys

indent =   "    "   #derzeitige einrückung
name = "Keyboard."  #name der Keyboard Bibliothek
n = ";\n"            #weil ich keine lust habe \ zu drücken
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
    print(txt[index])
    match txt[index]:
        case "text":
            file_c.write(indent+name+"print(\""+txt[index+1]+"\")"+n)
        case "textl":
            file_c.write(indent+name+"println(\""+txt[index+1]+"\")"+n)
        case "comb":
            comb_list = txt[index+1].split
            for index2 in range (0,len(comb_list),1):
                file_c.write(indent+name+"press("+duden(comb_list[index2])+")"+n)
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

if indent == "        ":
    file_c.write("    }" + n)
file_c.write("}")
file_c.close()



