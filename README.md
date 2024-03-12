# ETH-BSC-Crawler
Simple Script that starts from the current block and goes back every block saving all active addresses into a txt file. 
As example this code is using a public endpoint rpc "https://bsc-dataseed2.binance.org/", every public endpoint have requests rate limit.
If u have a private endpoint witout limits u can change the endpoint and remove the sleep time. increasing the process speed.
the code append to the file the new addresses on every block.
