# ETH/BSC_Crawler

Simple Script that starts from the current block and goes back every block saving all active addresses into a txt file. 

As example this code is using a public endpoint rpc "https://bsc-dataseed2.binance.org/", every public endpoint have requests rate limit.

If u have a private endpoint witout limits u can change the endpoint and set delay to 0.

the code append to the file the new addresses on every block.

when hitting stop button will save a 'Save.txt' that contain the last block number before close.

The program will use save file to continue a saved session.

remember to clean the addresses file before usage. it will contain many repeated addresses because the same address can appear in diferent blocks. simply use notepad++ option to remove duplicated lines.

![crawler](https://github.com/sayajinpt/ETH-BSC-Crawler/assets/61246703/476512a2-43cc-4173-9ab1-301cef15b280)

###If u find this code is usefull to you consider donation###

0x2456808AA54Cf86Fd531024b8Fd05bB2b7a671dC
