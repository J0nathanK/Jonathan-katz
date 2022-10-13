# Jonathan-katz

Program description:
====================
The program is designed to convert format files, from json file to csv file and the opposite from csv file to json file.

How to use:
============
The program needs to be in the same place with the file that converting, the program runs by using the Terminal and the command line.
There are four arguments that the program can receive. The two arguments that the program must receive are:
Path file.
Format to convert – to which format convert the file, the program can convert only from csv->json and from json->csv.
Otherwise, the program prints "Invalid Format".
The other two arguments are:
File name – if the user wants to name the convert file he needs to write into this argument , if the program will not get argument for the name of the output file, it will name it by the name of the "path file" with the new format.
The last argument is separator, if the user convert a csv file, the default separator between the values in the file is comma (",") but if there is a file with different separator, the user needs to write into the program his separator in his file.

  -F  , --file_path    Enter the path of the file
  -C  , --format       Enter to which format to convert[json/csv]
  --separator          If you convert to json file please enter which separator
  --file_name          Enter name for file


Requirements:
=============
It is necessary use the following libraries:
-	Json, to use built in function
-	Cvs, to use built in function 
-	Argparse,  to receive arguments from user



