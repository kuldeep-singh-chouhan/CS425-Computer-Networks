# CS425-Computer-Networks
This repository contains the programming assignments done in CS425A course in 2022-23 (Sem 2) under professor Dr. Amitangshu Pal
### 1. Client Server Chat
* The zip file contains two python files along with this README. The two files make a socket programming for UDP client server chatting application. Here, the server and client can chat until one of them says `bye`. 
* To run this application, open two different terminals and run
`python server.py`
in one of them. This terminal will be our server and will wait for the client to connect with it.
* Then in other terminal, run
`python client.py`
This terminal will be our client. The first message will be sent by the client.
* Note: one cannot close the server/client through a keyboard interrupt, when it’s waiting for a response message.
### 2. Cyclic Redundancy Check
* For running the program, type the following command in the terminal
`python main.py`
* This program uses random library for random string generation.
 ```
sample test
------------------
Enter Data block: 10010011011
Enter CRC pattern: 10011
The encoded frame is: 100100110111100
------------------
Message generated: 0011101010
CRC pattern: 110101
The encoded frame is: 001110101011100
------------------
Error pattern: 010000000101011
Erroneous frame: 011110101110111
Correct frame: 001110101011100
------------------
remainder: 10011
Error detected, frame rejected
------------------
```
### 3. WiFi Path Loss Exponent Calculation
* Finding hostel WiFi's path loss exponent, by taking reading s of WiFi strength at various points through [WiFi Analyzer App](https://play.google.com/store/apps/details?id=abdelrahman.wifianalyzerpro&hl=en_IN&gl=US&pli=1) in different orientations
* Plotting the best fit line for these coordinates obtained and using the path loss equation
