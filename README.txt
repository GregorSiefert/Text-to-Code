Dieses Programm dient dazu eine Tastaturabfolge (Text-Datei) in einen ausführbaren Code (Code-Datei) zu übersetzen
!!! Code zu generieren, der zu Schaden jeglicher Art führen würde wäre sehr uncool!!!

Aufbau einer Text Datei:
1 [Name des Cracks]
2 [Betriebssytem -> win/ios]
3 [Codierung des Cracks]
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
rep     [none]          widerholt alle nachvolgenden Befehle ohne Zeitliche Begrenzung ---vielleicht mit taster abbrechbar---

!!!Definition der Sondertasten und weiterem am Ende dieser Datei!!!

Ausgabe in der Code Datei:
