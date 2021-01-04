# Helmsteuerung Ironman ![](picturesREADME/ironman.png)
Dieses Repository befasst sich mir der Entwicklung einer Software, für die Steuerung eines "Ironman Helmes".

Inhaltsverzeichnis:
  - Funktionsumfang
  - Plattform
  - Sprachsteuerung
  - Pinbelegung GPIO
  - Manuelle Installationsanleitung
    - Installation von Raspbian
    - Optional: WPA Config und SSH aktivieren
    - Optional: Remote Desktop installieren
    - Tipp: Daten auf den Pi kopieren und herunterladen!
    - Installation der GPIO Python Bibliothek (RPi.GPIO 0.7.0)
    
  - Testprogramme für die einzelnen Funktionen
    - Servotest

## Funktionsumfang
Steuerung eines Servos.
Live Bild auf einem HDMI Monitor von einer Raspberry Pi Kamera.

Die Steuerung erfolgt wahlweise über Sprache, Taster an den GPIO Pins bzw einer Flutter App.

## Plattform
Als Einheit wird ein Raspberry Pi Zero verwendet, bzw ein Raspberry Pi 3.

Aufgrund der schwachen Rechenleitung des Raspberry Pi Zero's wird die Srachsteuerung auf selbiger Plattform nicht unterstützt.

**Folgende Tabelle zeigt welche Funtkionen auf den jeweiligen Raspberry Pi Modellen unterstützt werden.**
Getestet wurde die Software lediglich mit dem Raspberry Pi Zero und dem Raspberry Pi 3 Mod. B (v1.2)
Die restlichen Angaben beziehen sich auf die Eckdaten von der Raspberry Pi Foundation.


|**Funtionen**      | Zero          | Zero W/WH     | 1 Mod. A      | 1 Mod. B      | 
| ----------------- | ------------- | ------------- | ------------- | ------------- |
|**Sprachsteuerung**| Content Cell  | Content Cell  | Content Cell  | Content Cell  |
|**GPIO Taster**    | Content Cell  | Content Cell  | First Header  | Second Header |
|**Android/IOS App**| Content Cell  | Content Cell  | Content Cell  | Content Cell  |

|**Funtionen**      | 1 Mod. B+     | 2 Mod. B      | 2 Mod. B v1.2 | 3 Mod. B      |
| ----------------- | ------------- | ------------- | ------------- | ------------- |
|**Sprachsteuerung**| Content Cell  | Content Cell  | Content Cell  | Content Cell  |
|**GPIO Taster**    | Content Cell  | Content Cell  | First Header  | Second Header |
|**Android/IOS App**| Content Cell  | Content Cell  | Content Cell  | Content Cell  |

|**Funtionen**      | 3 Mod. B+     | 4 Mod. B      |
| ----------------- | ------------- | ------------- |
|**Sprachsteuerung**| Content Cell  | Content Cell  |
|**GPIO Taster**    | Content Cell  | Content Cell  |
|**Android/IOS App**| Content Cell  | Content Cell  |

## Sprachsteuerung 
Als Spracherkennung wird die Sofware **Sopare** verwendet.
Dies ist eine "Sound Pattern Recognition" Software die es erlaubt offline und in echtzeit Sprachbefehle zu verarbeiten.
Die Sofware wurde unter der Apache Lizenz veröffentlicht und kann über diesen Link aufgerufen werden: 
[Sopare](https://github.com/bishoph/sopare)

Eventuell wird es eine zweite Version geben, in der eine API Schnittstelle zu einem STT Server aufgebaut wird. (Google Cloud Speech-to-Text).
Diese Idee wurde jedoch vererst, aufgrund den damit verbundenen Kosten, verworfen.

## Pinbelegung Raspberry PI Servo und Taster
***Servomotor:***

***Drucktaster:***

## Manuelle Installationsanleitung
  -**Installation von Raspbian**
  
   Das offizilelle Image kann mithilfe von dem Pi Imager installiert werden.
   Download für Windows: [Download](https://downloads.raspberrypi.org/imager/imager_1.5.exe)
   
  -**Optional: WPA Config und SSH aktivieren**
  
  SSH und WPA Config File erstellen um per WLAN und Putty auf den Pi zugreifen zu können.
  Vorlage für beide Files befinden sich in diesem Repository.
  Wichtig: 
  
           ssh --> ohne Dateiendung (auch zu finden in diesem Repository)
  
           wpa_supplicant.conf --> SSID und Passswort im Klartext eingeben
  
  -**Optional: Remote Desktop installieren**

   Remote Desktop installieren zum Testen und Ausprobieren.

      sudo raspi-config --> Desktop Autologin
      (Die Option befindet sich unter System Options,Boot Auto Login, Desktop Autologin.)
      sudo apt-get purge realvnc-vnc-server --> RealVNC aufrung eines Konfliktes deinstallieren.
      sudo apt-get install xrdp --> XRDP installieren (Remote Desktop)
      sudo reboot (Neustart)
      
  -**Tipp: Daten auf den Pi kopieren und herunterladen!**

  Mithilfe des Windows Programms WinSCP können Dateien mühelos vom Pi auf den Copmuter und andersherum übetragen werden.
  Hier kann das Programm heruntergelden werden: [WinSCP](https://winscp.net/download/WinSCP-5.17.9-Setup.exe)
  
   -**Installation der GPIO Python Bibliothek (RPi.GPIO 0.7.0)**
   
       pip install RPi.GPIO
       
   Mithilfe von diesem Befehl kann das Paket installiert werden.
   Weitere Informationen zu dem Modul findet man hier: [PyPi.org](https://pypi.org/project/RPi.GPIO/)
   
  ## Testprogramme für die einzelnen Funktionen
  ### Servotest
  servotesting.py testet einen Servo der an den GPIO Pins angeschlossen ist.
  Dafür wurden folgende GPIO Pins verwendet:
  
    Signal: GPIO Pin 40 am Pi
    
    Masse: GND am Pi
    
    5V: 5Volt am Pi

  Bei dem Servotest wird der Servo auf 90°, 180° und 0° im 3 Sekundentakt gefahren.
  Wichtig: Der Servo wird nicht permanent mit einem PWM Signal versorgt! Da es sonst aufgrund der softwareseitgen Implementierung zu Timing Probleme kommen kann.
  (Zittern des Servos)
  D.h der Servo wird auf die Position gefahren und dann abgeschaltet, er hält nicht aktiv die Position.
  Je nachdem welche Last auf dem Servo liegt kann man dies vernachlässichen, da der Servo aufgrund des Getriebes im ausgeschaltetem Zustand schwer drehbar ist.
  
  Als Alternative könnte man gegebenfalls eine hardwareseitge Servosteuerung vornehmen mithilfe eines Servomotor Treibers.
  
  
