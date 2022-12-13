from brownie import UBNFTF, network, config
from scripts.util import get_account

token_uri = "https://ipfs.io/ipfs/QmeAgmxrmMPVr3zddN9AfXzDDupm4RMxL4bLRsrKiUbPqT?filename=Unique-Art.json"


def nft_mint():
    account = get_account()

    # Check if the NFT has been deployed.
    if len(UBNFTF) == 0:
        print("The NFT has not been deployed yet!")
        return
    nft = UBNFTF[-1]

    # Check if there is enough balance in the NFT
    if nft.checkTokenBalance() == 0:
        print("There is no fund to mint NFT.")
        return

    print("Preparing to mint NFT")
    tx = nft.CreateLogoNFT(token_uri, {"from": account})
    tx.wait(1)
    print("NFT successfully minted.")


def main():
    nft_mint()
