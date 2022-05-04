from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The entrance fees are: {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})
    print(f"The entrance fees paid: {entrance_fee}")


def withdraw2():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def getPrice():
    fund_me = FundMe[-1]
    priceUsd = fund_me.getPrice()
    print(f"Price in usd is: {priceUsd}")


def getConversionRate():
    fund_me = FundMe[-1]
    conversion_rate = fund_me.getConversionRate(1)
    print(f"Conversion Rate is: {conversion_rate}")


# Fees: 0.025000000000000000
def main():
    fund()
    withdraw2()
    getPrice()
    getConversionRate()

