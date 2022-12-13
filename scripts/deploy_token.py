from brownie import UBFToken, network, config
from scripts.util import get_account


def deploy_token():
    account = get_account()

    ubftoken = UBFToken.deploy(
        10_000_000 * (10**18),
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )

    print(f"The token has been deployed at {ubftoken.address}")


def main():
    deploy_token()
