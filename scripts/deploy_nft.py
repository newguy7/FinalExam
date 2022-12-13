from brownie import UBFToken, UBNFTF, network, config
from scripts.util import get_account


def deploy_nft():
    account = get_account()

    if len(UBFToken) == 0:
        print("UBFToken has not been deployed yet!")
        return
    ubftoken_address = UBFToken[-1].address

    ubnftf = UBNFTF.deploy(
        ubftoken_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )

    print(f"The NFT has been deployed at {ubnftf.address}")


def main():
    deploy_nft()
