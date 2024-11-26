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
textl   String          Tippt den Inhalt ab und drückt danach [ENTER]
comb    char abfolge    Hält die vorherigen Tasten und lässt nach dem drücken der letzen Taste alle vorher gedrückten Tasten los ---noch testen---
press   char            Drückt eine Taste
hold    char            Hält eine Taste !!!Achtung ohne Zeitliche Begrenzung!!!
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
