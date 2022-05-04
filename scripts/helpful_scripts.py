from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIROEMNTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 2000

#  we need to tell to use acc[0] also wnhen we use forked network
def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS
        or network.show_active() in FORKED_LOCAL_ENVIROEMNTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active netowrk is {network.show_active()}")
    print("Deploying monk")
    # we look at the contract constructor args in order to deploy
    #  constructor(uint8 _decimals, int256 _initialAnswer)
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS,
            Web3.toWei(STARTING_PRICE, "ether"),
            {"from": get_account()}
            # DECIMALS,
            # STARTING_PRICE,
            # {"from": get_account()},
        )
    print("Mock deployed")
