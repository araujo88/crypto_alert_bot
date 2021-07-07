import asyncio
import websockets, json, pprint, numpy
import config
from binance.client import Client
from binance.enums import *
import time
import requests
import win32api
import winsound

client = Client(config.API_KEY, config.API_SECRET)

K = 4

volume_btc = []
volume_eth = []
volume_one = []
volume_chz = []
volume_avax = []
volume_uni = []
volume_cake = []
volume_bnb = []
volume_waves = []
volume_sushi = []
volume_luna = []
volume_ftt = []
volume_yfiu = []
volume_tfuel = []
volume_theta = []
volume_link = []
volume_storj = []
volume_1inch = []
volume_stx = []
volume_atom = []
volume_matic = []
volume_comp = []
volume_cvc = []
volume_snx = []
volume_aave = []
volume_fil = []
volume_ksm = []
volume_doge = []
volume_dot = []
volume_ada = []
volume_sol = []
volume_vet = []
volume_xmr = []
volume_xrp = []

connections = set()
connections.add("wss://stream.binance.com:9443/ws/btcusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/ethusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/oneusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/chzusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/avaxusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/unisdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/cakeusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/bnbusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/wavesusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/sushiusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/lunausdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/fttusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/yfiusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/thetausdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/linkusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/storjusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/1inchusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/stxusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/atomusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/maticusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/compusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/cvcusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/cvcusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/snxusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/aaveusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/filusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/ksmusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/dogeusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/dotusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/adausdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/solusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/vetusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/xmrusdt@kline_5m")
connections.add("wss://stream.binance.com:9443/ws/xrpusdt@kline_5m")

async def handle_socket(uri, ):
    global in_position
    
    global volume_btc
    global volume_eth
    global volume_one
    global volume_chz
    global volume_avax
    global volume_uni
    global volume_cake
    global volume_bnb
    global volume_waves
    global volume_sushi
    global volume_luna
    global volume_ftt
    global volume_yfi
    global volume_tfuel
    global volume_theta
    global volume_link
    global volume_storj
    global volume_1inch
    global volume_stx
    global volume_atom
    global volume_matic
    global volume_comp
    global volume_cvc
    global volume_snx
    global volume_aave
    global volume_fil
    global volume_ksm
    global volume_doge
    global volume_dot
    global volume_ada
    global volume_sol
    global volume_vet
    global volume_xmr
    global volume_xrp
    
    async with websockets.connect(uri) as websocket:
        async for message in websocket:
            json_message = json.loads(message)
            #pprint.pprint(json_message)

            symbol = json_message['s']
            candle = json_message['k']
            is_candle_closed = candle['x']
            volume = candle['v']

            if is_candle_closed:
                if symbol == "BTCUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_btc.append(float(volume))
                    if len(volume_btc) > 1 and volume_btc[-1] > K*volume_btc[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "ETHUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_eth.append(float(volume))
                    if len(volume_eth) > 1 and volume_eth[-1] > K*volume_eth[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "ONEUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_one.append(float(volume))
                    if len(volume_one) > 1 and volume_one[-1] > K*volume_one[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "CHZUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_chz.append(float(volume))
                    if len(volume_chz) > 1 and volume_chz[-1] > K*volume_chz[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "AVAXUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_avax.append(float(volume))
                    if len(volume_avax) > 1 and volume_avax[-1] > K*volume_avax[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "UNIUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_uni.append(float(volume))
                    if len(volume_uni) > 1 and volume_uni[-1] > K*volume_uni[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "CAKEUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_cake.append(float(volume))
                    if len(volume_cake) > 1 and volume_cake[-1] > K*volume_cake[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "BNBUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_bnb.append(float(volume))
                    if len(volume_bnb) > 1 and volume_bnb[-1] > K*volume_bnb[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "WAVESUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_waves.append(float(volume))
                    if len(volume_waves) > 1 and volume_waves[-1] > K*volume_waves[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "SUSHIUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_sushi.append(float(volume))
                    if len(volume_sushi) > 1 and volume_sushi[-1] > K*volume_sushi[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "LUNAUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_luna.append(float(volume))
                    if len(volume_luna) > 1 and volume_luna[-1] > K*volume_luna[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "FTTUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_ftt.append(float(volume))
                    if len(volume_ftt) > 1 and volume_ftt[-1] > K*volume_ftt[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "YFIUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_yfi.append(float(volume))
                    if len(volume_yfi) > 1 and volume_yfi[-1] > K*volume_yfi[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "TFUELUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_tfuel.append(float(volume))
                    if len(volume_tfuel) > 1 and volume_tfuel[-1] > K*volume_tfuel[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "THETAUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_theta.append(float(volume))
                    if len(volume_theta) > 1 and volume_theta[-1] > K*volume_theta[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "LINKUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_link.append(float(volume))
                    if len(volume_link) > 1 and volume_link[-1] > K*volume_link[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "STORJUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_storj.append(float(volume))
                    if len(volume_storj) > 1 and volume_storj[-1] > K*volume_storj[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "1INCHUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_1inch.append(float(volume))
                    if len(volume_1inch) > 1 and volume_1inch[-1] > K*volume_1inch[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "STXUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_stx.append(float(volume))
                    if len(volume_stx) > 1 and volume_stx[-1] > K*volume_stx[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "ATOMUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_atom.append(float(volume))
                    if len(volume_atom) > 1 and volume_atom[-1] > K*volume_atom[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "MATICUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_matic.append(float(volume))
                    if len(volume_matic) > 1 and volume_matic[-1] > K*volume_matic[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "COMPUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_comp.append(float(volume))
                    if len(volume_comp) > 1 and volume_comp[-1] > K*volume_comp[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "CVCUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_cvc.append(float(volume))
                    if len(volume_cvc) > 1 and volume_cvc[-1] > K*volume_cvc[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "SNXUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_snx.append(float(volume))
                    if len(volume_snx) > 1 and volume_snx[-1] > K*volume_snx[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "AAVEUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_aave.append(float(volume))
                    if len(volume_aave) > 1 and volume_aave[-1] > K*volume_aave[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "FILUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_fil.append(float(volume))
                    if len(volume_fil) > 1 and volume_fil[-1] > K*volume_fil[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "KSMUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_ksm.append(float(volume))
                    if len(volume_ksm) > 1 and volume_ksm[-1] > K*volume_ksm[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "DOGEUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_doge.append(float(volume))
                    if len(volume_doge) > 1 and volume_doge[-1] > K*volume_doge[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "DOTUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_dot.append(float(volume))
                    if len(volume_dot) > 1 and volume_dot[-1] > K*volume_dot[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "ADAUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_ada.append(float(volume))
                    if len(volume_ada) > 1 and volume_ada[-1] > K*volume_ada[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "SOLUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_sol.append(float(volume))
                    if len(volume_sol) > 1 and volume_sol[-1] > K*volume_sol[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "VETUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_vet.append(float(volume))
                    if len(volume_vet) > 1 and volume_vet[-1] > K*volume_vet[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "XMRUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_xmr.append(float(volume))
                    if len(volume_xmr) > 1 and volume_xmr[-1] > K*volume_xmr[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
                if symbol == "XRPUSDT":
                    print("{} volume: {}".format(symbol, volume))
                    volume_xrp.append(float(volume))
                    if len(volume_xrp) > 1 and volume_xrp[-1] > K*volume_xrp[-2]:
                        print("High volume alert for {} !!!".format(symbol))		
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        winsound.Beep(2500, 500)
                        
async def handler():
    await asyncio.wait([handle_socket(uri) for uri in connections])

asyncio.get_event_loop().run_until_complete(handler())