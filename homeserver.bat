@echo off
if %1 == "build" (goto OpenServer)

start /B code "C:\Projects\GServer\home-server"
start /B code "C:\Projects\GServer\home-client"

:OpenServer
start /D "C:\Projects\GServer\home-server" npm run automated
start /D "C:\Projects\GServer\home-server" npm run start
cd "C:\Projects\GServer\home-client"
npm run start
