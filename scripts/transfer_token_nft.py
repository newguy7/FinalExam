from brownie import UBFToken, UBNFTF, network, config
from scripts.util import get_account


def transfer_token_nft():
    account = get_account()

    if len(UBFToken) == 0:
        print("UBFToken has not been deployed yet!")
        return
    token = UBFToken[-1]
    amount = 1000 * (10 ** token.decimals())

    if len(UBNFTF) == 0:
        print("NFT has not been deployed yet!")
        return
    nft = UBNFTF[-1]
    print("Initiating balance transfer")
    print(
        f"Transferring {token.symbol()} at address: {token.address} to NFT at address {nft.address}"
    )
    token.transfer(nft.address, amount, {"from": account})
    print("Balance transferred successfully.")


def main():
    transfer_token_nft()
