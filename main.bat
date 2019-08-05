@echo off
:menu
echo Menu
echo Wybierz odpowiednia opcje
echo 1. Wykonaj program
echo 2. Stworz backup
echo 3. O projekcie
echo 4. Wyjscie
set /p odp=
if %odp% equ 1 (
    goto opcja1
) 
if %odp% equ 2 (
    goto opcja2
)
if %odp% equ 3 (
    goto opcja3
)
if %odp% equ 4 (
    goto quit
)


:opcja1
echo "Wykonywanie projektu"
setlocal enabledelayedexpansion

for /f "tokens=* delims=" %%a in ('dir "input\"  /b') do (
    REM echo %%a
    call statystyka.exe input\%%a output\%%a
    )

call python raport.py
rem call raport.html



goto menu
:opcja2
set data=%date%
echo %data%
if not exist backup\%data (
mkdir backup\%data%
)

echo "backup folderu input "
xcopy "%CD%\input" "%CD%\backup\%data%\input"  /i /y
echo "backup folderu output"
xcopy "%CD%\output" "%CD%\backup\%data%\output" /i /y
echo kopiowanie skryptu i raportu
xcopy raport.html "%CD%\backup\%data%" /i /y
xcopy raport.py "%CD%\backup\%data%" /i /y
pause
goto menu

:opcja3
echo "O projekcie"
echo "Program ma za zadanie wykonywac operacje statystyczne na wprowadzonych danych: srednia, mediana, odchylenie standardowe i wariacja"

pause
goto menu


:quit
echo Wyjscie
exit