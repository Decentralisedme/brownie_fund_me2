from brownie import FundMe


def contract_address():
    fund_me = FundMe[-1]
    cnt_add = fund_me.address
    print(f"The contract address is {cnt_add}")


def main():
    contract_address()
