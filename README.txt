Dieses Programm dient dazu eine Tastaturabfolge (Text-Datei) in einen ausführbaren Code (Code-Datei) zu übersetzen
!!! Code zu generieren, der zu Schaden jeglicher Art führen würde wäre sehr uncool!!!

Aufbau einer Text Datei:
1 [Name des Cracks]
2 [Codierung des Cracks]
3 [Betriebssytem -> win/ios]
4 [Art des Befehls]
5 [Inhalt für den Befehl]
6 [Art des Befehls]
7 ...

Definition der Befehle:
Name    Inhalt          Beschreibung
text    String          Tippt den Inhalt ab
textl   String          Tippt den Inhalt ab und geht danach in die nächste Zeile
comb    char abfolge    Hält die vorherigen Tasten und lässt nach dem drücken der letzen Taste alle vorher gedrückten Tasten los ---noch testen---
stroke   char            Drückt eine Taste
press    char            Hält eine Taste !!!Achtung ohne Zeitliche Begrenzung!!!
rel     char            Läst die Taste los
relall  [none]          Läst alle Tasten los
wait    int             wartet die angegebene Anzahl an Millisekunden
rep     [none]          widerholt alle nachvolgenden Befehle ohne Zeitliche Begrenzung !!!Nur einmal pro Crack erlaubt!!!

!!!Definition der Sondertasten und weiterem am Ende dieser Datei!!!

Ausgabe in der Code Datei:
1 // Crackname: [Crackname]
2 void [Betriebssystem]_[Codierung des Cracks]() {
3 [Code_start]
...
n [Code_ende]
n+1 }

Sondertasten nach dem Duden:
shift   = [SHIFT]
ctrl    = [CONTROL]
alt     = [ALT]
option  = [OPTION auf ios]
win     = [WINDOWS TASTE]
ios     = [IOS TASTE]
tab     = [TAB]
caps    = [CAPS LOCK]
back    = [BACKSPACE]
enter   = [ENTER]
rclick  = [RIGHT CLICK]
strgv   = [STRG+V]
del     = [DELETE]
home    = [HOME TASTE oder POS 1]
end     = [END TASTE]
scrollu = [BILD HOCH]
scrolld = [BILD RUNTER]
up      = [PFEIL HOCH]
down    = [PFEIL RUNTER]
left    = [PFEIL LINKS]
right   = [PFEIL RECHTS]
esc     = [ESCAPE]
pause   = [PAUSE]
F1      = [F1]
F2      = [F2]
F3      = [F3]
F4      = [F4]
F5      = [F5]
F6      = [F6]
F7      = [F7]
F8      = [F8]
F9      = [F9]
F10     = [F10]
F11     = [F11]
F12     = [F12]
F13     = [F13]
F14     = [F14]
F15     = [F15]
F16     = [F16]
F17     = [F17]
F18     = [F18]
F19     = [F19]
F20     = [F20]
F21     = [F21]
F22     = [F22]
F23     = [F23]
F24     = [F24]