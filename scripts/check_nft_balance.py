from brownie import UBNFTF
from web3 import Web3


def check_nft_balance():
    if len(UBNFTF) == 0:
        print("NFT has not been deployed yet!")
        return

    nft = UBNFTF[-1]

    print("Getting NFT balance....")
    nft_balance = Web3.fromWei(nft.checkTokenBalance(), "ether")

    print(f"The NFT balance is {nft_balance}")


def main():
    check_nft_balance()
