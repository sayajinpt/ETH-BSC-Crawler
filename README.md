# ETH/BSC_Crawler

Simple Script that starts from the current block or any especific block if u set inside the Save.txt, and goes back every block saving all active addresses into a txt file. 

As example this code is using a public endpoint rpc "https://bsc-dataseed2.binance.org/", every public endpoint have requests rate limit.

If u have a private endpoint witout limits u can change the endpoint and set delay to 0.

the code append to the file the new addresses on every block.

when hitting stop button will save a 'Save.txt' that contain the last block number before close.also will load the saved addresses and remove the duplicates from file.

The program will use save file to continue a saved session.
![crawler](https://github.com/sayajinpt/ETH-BSC-Crawler/assets/61246703/476512a2-43cc-4173-9ab1-301cef15b280)

###If u find this code is usefull to you consider donation###

0x2456808AA54Cf86Fd531024b8Fd05bB2b7a671dC
