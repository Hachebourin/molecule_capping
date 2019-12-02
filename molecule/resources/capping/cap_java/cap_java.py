#! /usr/bin/python
import sys
import os

FILE_TO_LOG_CMD = os.getenv("FILE_TO_LOG_CMD", "/tmp/cap_java/molecule_cap_cmd_file.txt")


if __name__ == "__main__":      
    if len(sys.argv) > 1:
        with open(FILE_TO_LOG_CMD, 'a') as writer:
            writer.write("{0}\n".format(' '.join(sys.argv[1:])))
            sys.stdout.write("INFO: Everything is up to date")
