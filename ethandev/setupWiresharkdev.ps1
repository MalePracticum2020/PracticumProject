Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

choco install -y visualstudio2019community 
choco install -y visualstudio2019-workload-nativedesktop

mkdir D:\Development
#Invoke-WebRequest -Uri "https://download.qt.io/official_releases/online_installers/qt-unified-windows-x86-online.exe" -OutFile "D:\Development\qtinstaller.exe" 

choco install -y activeperl
choco install -y git
choco install -y cmake
choco install -y asciidoctorj xsltproc docbook-bundle
choco install -y winflexbison3
cd D:\Development
git clone https://code.wireshark.org/review/wireshark

#cmake -G "Visual Studio 16 2019" -A x64 .\wireshark
$warningmessage=@"
***********
Please make sure you have installed qt by this time (installer is the qtinstaller.exe)
Press enter to continue once this has been done
***********
"@
Read-Host -Prompt $warningmessage
$temp=@"
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars32.bat" x86 
set WIRESHARK_BASE_DIR=C:\Development
set QT5_BASE_DIR=D:\Qt\5.15.1\msvc2019
set WIRESHARK_VERSION_EXTRA=-eceldNetsys
mkdir D:\Development\wsbuild32
cd D:\Development\wsbuild32
cmake -G "Visual Studio 16 2019" -A Win32 ..\wireshark
msbuild Wireshark.sln /p:Configuration=Debug /p:Platform=Win32
"@ 
$temp | Out-File -encoding ascii temp.bat
cmd /k temp.bat
