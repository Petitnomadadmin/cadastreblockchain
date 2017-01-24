import json 
from binascii import hexlify
from  bitcoin import deserialize 
from  bitcoin import blockr_fetchtx

 tx = deserialize(str(blockr_fetchtx("8bae12b5f4c088d940733dcd1455efc6a3a69cf9340e17a981286d3778615684"))) 
#opreturn de chart.png : marche pas car surement pas lemême formatage de tx, étudier les 2 pour ameliorer le parser 
#tx = deserialize(str(blockr_fetchtx("3c1fabddae496b64a309e074836a104c8086d44212bdd4dbe7118ff31edb5b4d")))
json_tx = json.loads(json.dumps(tx))

op_return = json_tx['outs'][0]['script']

msg = bytearray.fromhex(op_return)
msg_decoded = msg[2:].decode()   
print(msg_decoded)

msg_encoded = msg_decoded.encode()
print(hexlify(bytearray(msg_encoded)))
