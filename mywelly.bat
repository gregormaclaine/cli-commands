start /B code "C:\Projects\myWelly\myWellyClient"
start /B code "C:\Projects\myWelly\myWellyServer"

start /D "C:\Projects\myWelly\myWellyhttps" caddy
start /D "C:\Projects\myWelly\myWellyServer" npm run start

cd C:\Projects\myWelly\myWellyClient
npm run start