import tkinter as tk
from tkinter import messagebox
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
import threading
import time

class BSC_Crawler_GUI:
    def __init__(self, master):
        self.master = master
        master.title("ETH/BSC Crawler        By:SayajinPt")

        # Customize background and text color for different widgets
        self.master.configure(bg="gray")

        # Define font settings
        font_style = ("Comic Sans MS", 12)  # Change "Helvetica" to the desired font family and 12 to the desired font size

        self.rpc_endpoint_label = tk.Label(master, text="RPC Endpoint:", bg="gray", fg="black", font=font_style)
        self.rpc_endpoint_label.pack()

        self.rpc_endpoint_entry = tk.Entry(master, font=font_style)
        self.rpc_endpoint_entry.pack()

        self.rpc_endpoint_entry.insert(tk.END, "https://bsc-dataseed2.binance.org/")

        self.start_new_button = tk.Button(master, text="New Session", command=self.start_new, bg="lightblue", fg="black", font=font_style)
        self.start_new_button.pack()

        self.continue_button = tk.Button(master, text="Continue Session", command=self.continue_from_save, bg="lightgreen", fg="black", font=font_style)
        self.continue_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop, bg="red", fg="black", font=font_style)
        self.stop_button.pack()

        self.sleep_label = tk.Label(master, text="Delay(Default 1 sec):", bg="gray", fg="black", font=font_style)
        self.sleep_label.pack()

        self.sleep_entry = tk.Entry(master, font=font_style)
        self.sleep_entry.pack()

        self.textbox = tk.Text(master, height=5, width=35, font=font_style)
        self.textbox.pack()

        self.current_block = 0
        self.file_path = "Addresses.txt"
        self.file_path2 = "Save.txt"

        self.is_crawling = False
        self.crawl_thread = None

        self.web3 = None

    def crawl_bsc(self):
        self.is_crawling = True
        while self.is_crawling:
            try:
                transactions = self.web3.eth.get_block(self.current_block)['transactions']
                unique_addresses = self.get_unique_addresses(transactions)
                with open(self.file_path, 'a') as file:
                    for address in unique_addresses:
                        file.write(f"{address}\n")
                self.textbox.insert(tk.END, f"Block: {self.current_block}, Unique Addresses: {len(unique_addresses)}\n")
                self.textbox.see(tk.END)  # Auto-scroll to the bottom
                self.current_block += 1
                sleep_time = float(self.sleep_entry.get()) if self.sleep_entry.get() else 1
                time.sleep(sleep_time)  # Use user-input sleep time
            except Exception as e:
                self.textbox.insert(tk.END, f"Error: {e}\n")
                self.textbox.see(tk.END)  # Auto-scroll to the bottom
                time.sleep(300)  # Retry after 5 minutes

    def start_new(self):
        if not self.is_crawling:
            rpc_endpoint = self.rpc_endpoint_entry.get()
            self.web3 = Web3(HTTPProvider(rpc_endpoint))
            self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
            self.current_block = self.web3.eth.block_number
            self.crawl_thread = threading.Thread(target=self.crawl_bsc)
            self.crawl_thread.start()

    def continue_from_save(self):
        if not self.is_crawling:
            try:
                with open(self.file_path2, 'r') as file:
                    saved_block = int(file.read())
                    self.current_block = saved_block
                    rpc_endpoint = self.rpc_endpoint_entry.get()
                    self.web3 = Web3(HTTPProvider(rpc_endpoint))
                    self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
                    self.crawl_thread = threading.Thread(target=self.crawl_bsc)
                    self.crawl_thread.start()
            except FileNotFoundError:
                messagebox.showerror("Error", "Save file not found.")
            except ValueError:
                messagebox.showerror("Error", "Invalid block number in save file.")

    def stop(self):
        if self.is_crawling:
            with open(self.file_path2, 'w') as file:
                file.write(str(self.current_block))
            self.is_crawling = False
            self.textbox.insert(tk.END, "Crawling stopped. Current block saved.\n")
            self.textbox.see(tk.END)            # Auto-scroll to the bottom
            self.master.destroy()
    
    def get_unique_addresses(self, transactions):
        unique_addresses = set()
        for tx_hash in transactions:
            tx = self.web3.eth.get_transaction(tx_hash)
            unique_addresses.add(tx['from'])
            unique_addresses.add(tx['to'])
        return unique_addresses


root = tk.Tk()
app = BSC_Crawler_GUI(root)
root.mainloop()

