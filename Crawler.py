from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
import time

bsc_rpc_endpoint = "https://bsc-dataseed2.binance.org/"

web3 = Web3(HTTPProvider(bsc_rpc_endpoint))

web3.middleware_onion.inject(geth_poa_middleware, layer=0)

if not web3.isConnected():
    print("Error: Unable to connect to BSC node.")
    exit()

def get_transactions_for_address(address):
    transactions = web3.eth.get_transactions(address)
    return transactions

def get_unique_addresses(transactions):
    unique_addresses = set()
    for tx_hash in transactions:
        tx = web3.eth.get_transaction(tx_hash)
        unique_addresses.add(tx['from'])
        unique_addresses.add(tx['to'])
    return unique_addresses

def crawl_bsc(max_requests_per_interval=9999, interval_duration=1):
    current_block = web3.eth.block_number
    file_path = "addresses.txt"

    while True:
        try:
            transactions = web3.eth.get_block(current_block)['transactions']

            unique_addresses = get_unique_addresses(transactions)

            with open(file_path, 'a') as file:
                for address in unique_addresses:
                    file.write(f"{address}\n")

            print(f"Block: {current_block}, Unique Addresses: {len(unique_addresses)}")

            time.sleep(interval_duration)

            current_block -= 1

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(300)

if __name__ == "__main__":
    crawl_bsc()

