# /app/services/blockchain_service.py
import logging
from bitcoinlib.wallets import Wallet, wallet_delete
from bitcoinlib.transactions import Transaction
from bitcoinlib.services.services import Service

logging.basicConfig(level=logging.INFO)

class BlockchainService:
    def __init__(self, wallet_name='mywallet', network='testnet'):
        self.wallet_name = wallet_name
        self.network = network
        self.service = Service(network=network)
        try:
            self.wallet = Wallet.create(wallet_name, keys='wpkh', network=network, db_uri='sqlite:///')
        except Exception as e:
            logging.info("Wallet already exists. Opening existing wallet.")
            self.wallet = Wallet(wallet_name)

    def create_new_address(self):
        address = self.wallet.new_key().address
        logging.info(f"New address created: {address}")
        return address

    def send_transaction(self, address, amount):
        # Amount is in Satoshis for Bitcoin
        tx = self.wallet.send_to(address, amount)
        logging.info(f"Transaction sent: {tx}")
        return tx

    def get_transaction_info(self, txid):
        tx_info = self.service.gettransaction(txid)
        logging.info(f"Transaction info: {tx_info}")
        return tx_info

    def cleanup(self):
        # Use with caution: Deletes the wallet for cleanup purposes
        wallet_delete(self.wallet_name, force=True)

# Example usage
if __name__ == '__main__':
    bs = BlockchainService()
    address = bs.create_new_address()
    print(f"Address: {address}")
    # Followed by send_transaction and get_transaction_info as needed
