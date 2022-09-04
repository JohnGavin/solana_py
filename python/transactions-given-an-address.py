
# https://stackoverflow.com/questions/70028880/i-would-like-to-get-all-transactions-given-an-address
from solana.rpc.api import Client
import pandas as pd

all_addresses = [
    '8kaAbZYLHUDadjgpRXkZE63E2AvsZDtJRddAMXtLB4ev',
    '2AQdpHJ2JpcEgPiATUXjQxA8QmafFegfQwSLWSprPicm',
    'Vote111111111111111111111111111111111111111',
    'fake address',
]

endpoint = 'https://api.mainnet-beta.solana.com'
# 'https://solana-api.projectserum.com'
# 'https://api.devnet.solana.com'    # probably for `developing`
# 'https://api.testnet.solana.com'   # probably for `testing`

solana_client = Client(endpoint)
addr = all_addresses[0]
result = solana_client.get_signatures_for_address(
      addr ) #, before='89Tv9s2uMGaoxB8ZF1LV9nGa72GQ9RbkeyCDvfPviWesZ6ajZBFeHsTPfgwjGEnH7mpZa7jQBXAqjAfMrPirHt2')
trans = pd.DataFrame( result['result'] )

res_df = pd.DataFrame(result)
pd.DataFrame( res_df['result'].items() )

bet = '4UjzRWHAWTiH5SGVNChXLzvsr2sg37jo4TSXVJ1iSba9'
store = 'wWhS6u9Vie1xUjokPZpt77d1Wa2rLZ9N4Weq49YpEjf'
trans['signature'].str.startswith('w').sum()

result2 = solana_client.get_signatures_for_address(
  addr , 
  before = trans['signature'].tail(1).values[0] )
trans2 = pd.DataFrame(result2['result'] )

result.from_dict()


trans.tail()
# trans.describe()
trans.info()
trans.info(null_counts=True, verbose=True)
trans.dtypes
trans.columns.values
trans.signature.head()
# View(trans)
    





for address in all_addresses:
    print('address:', address)
    
    #result = solana_client.get_confirmed_signature_for_address2(address, limit=1)
    result = solana_client.get_signatures_for_address(
      address) #, before='89Tv9s2uMGaoxB8ZF1LV9nGa72GQ9RbkeyCDvfPviWesZ6ajZBFeHsTPfgwjGEnH7mpZa7jQBXAqjAfMrPirHt2')
    result['result'] 
    
    
    if 'result' in result:
        print('len:', len( result['result'] ))

        # I use `[:5]` to display only first 5 values
        for number, item in enumerate(result['result'][:1], 1):
            print(number, 'signature:', item['signature'])

        # check if there is `4SNQ4h1vL9GkmSnojQsf8SZyFvQsaq62RCgops2UXFYag1Jc4MoWrjTg2ELwMqM1tQbn9qUcNc4tqX19EGHBqC5u`
        for number, item in enumerate(result['result'], 1):
            if item['signature'].startswith('4SN'):
                print('found at', number, '>>>', item['signature'])

    else:
        # error message 
        print(result)

    print('---')

    #solana_client.get_account_info(address)
