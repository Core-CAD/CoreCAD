@echo off
rem Abre o programa salvando as configurações direto na pasta do projeto
start "" "%~dp0bin\FreeCAD.exe" -u "%~dp0config\user.cfg" -s "%~dp0config\system.cfg"