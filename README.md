# Example of using named pipes and domain sockets on Unix

## Named pipe

First create the named pipe
```bash
mkfifo timer.pipe
```
_Print_: execute the following on two different shells for the print version
```bash
python3 timer_print.py > timer.pipe
cat < timer.pipe
```

_File_: execute the following on two different shells for the file version
```bash
python3 timer_file.py
cat < timer.pipe
```

## Domain sockets

Execute the following on two differeny shells
```bash
python3 socket_server.py
python3 socket_client.py
```