start /B code "C:\Projects\myWellyClient"
start /B code "C:\Projects\myWellyServer"

start /D "C:\Projects\myWellyhttps" caddy
start /D "C:\Projects\myWellyServer" npm run start

cd C:\Projects\myWellyClient
npm run start