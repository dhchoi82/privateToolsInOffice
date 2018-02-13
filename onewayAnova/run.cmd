@ECHO OFF
python init.py
R CMD BATCH --quiet --no-restore --no-save --no-init-file script.R cmdOutput.txt
ECHO ERRORLEVEL: %ERRORLEVEL%
type cmdOutput.txt
PAUSE
EXIT
