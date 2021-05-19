@echo off
for /f "delims=" %%a in ('dir /b') do echo,%~dp0%%a >> File_path.txt