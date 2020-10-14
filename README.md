# Data Visualization System (eceld-netsys/wireshark)
Data Visualization System is an application in which it will create visual representation of package traffic from
existing eceld-netsys system.
## System Requirements
DVS should run in the following O.S. 
- Windows
- Kali Linux 2020.2 64 bit
- Python 3 >= 3.35
## Installation (Linux)
clone repository and go into directory and run the following
```
./linuxinstaller.sh
```
## Installation (Windows)
Follow the instructions from the latest release to download the DatasetVisualizationSystem_v1.0-beta.zip
Extract the contents of the zip file to your local directory. There is an executable and a windows installer. Feel free to use which ever one you feel most comfortable with.
```
To use the executable simply:
Double click on the DatasetVisualizationSystem.exe to start the program. The program will run in approximately 30 - 60 seconds. Note: Disabling your antivirus might help reduce 
the time it takes for the program to run. It takes longer to open the program because the executable unpacks all of the dependencies into a temporary folder.

To use the windows installer:
Double click on the Installer.exe. Follow the instructions on the prompt. Once the installer is finished installing all the project dependencies, navigate to the directory where
the project was installed and double click on the DatasetVisualizationSystem.exe executable. The program will run in approximately 5 - 20 seconds. Note: You will not be able to
run the executable outside of the directory where it was installed. A solution to this is to create a shortcut outside of the directory.  
```
![Screenshot1](screenshots/choose-install.png)  
![Screenshot2](screenshots/installing.png)  
![Screenshot3](screenshots/completed-install.png)

## Run the GUI
```
python3 GUI/InitialWindow.py
```
