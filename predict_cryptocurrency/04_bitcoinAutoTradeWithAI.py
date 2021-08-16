# 변동성 돌파 전략
# 인공지능을 이용한 비트코인 자동매매
import os
# import pyupbit

from datetime import timedelta
from fbprophet import Prophet
from dotenv import load_dotenv
# import time
# import datetime
# import schedule

from local_pyupbit import quotation_api, exchange_api, request_api

load_dotenv(verbose=True)

access = os.getenv('UPBIT_OPEN_API_ACCESS_KEY')
secret = os.getenv('UPBIT_OPEN_API_SECRET_KEY')

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = quotation_api.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = quotation_api.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_start_time(ticker):
    """시작 시간 조회"""
    df = quotation_api.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = exchange_api.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return quotation_api.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

predicted_close_price = 0
def get_predict_price_24Hour(ticker):
    """Prophet으로 당일 종가 가격 예측"""
    # global predicted_close_price
    df = quotation_api.get_ohlcv(ticker, interval="minute60")
    df = df.reset_index()
    df['ds'] = df['index']
    df['y'] = df['close']
    data = df[['ds','y']]
    # print(data.head())

    model = Prophet()
    model.fit(data) # 모델 학습 

    future = model.make_future_dataframe(periods=24, freq='H')
    forecast = model.predict(future)
    # print('======== forecast check ===')
    # print(forecast['ds'])
    # print(forecast.iloc[-1]['ds'])
    # print(forecast.iloc[-1]['ds'].replace(hour=9))
    # print(forecast['ds'] == forecast.iloc[-1]['ds'].replace(hour=9))
    # print('===========================')
    closeDf = forecast[forecast['ds'] == forecast.iloc[-1]['ds'].replace(hour=9)]
    if len(closeDf) == 0:
        closeDf = forecast[forecast['ds'] == data.iloc[-1]['ds'].replace(hour=9)]
    closeValue = closeDf['yhat'].values[0]
    predicted_close_price = closeValue

    return predicted_close_price

def get_predict_price(ticker, after_hour=24):
    # global predicted_close_price
    df = quotation_api.get_ohlcv(ticker, interval="minute10")
    df = df.reset_index()
    df['ds'] = df['index']
    df['y'] = df['close']
    data = df[['ds','y']]
    # print(data.head())

    model = Prophet()
    model.fit(data) # 모델 학습 

    # future = model.make_future_dataframe(periods=24, freq='H')
    future = model.make_future_dataframe(periods=after_hour, freq='H')
    forecast = model.predict(future)
    # print('======== forecast check ===')
    lastTime = forecast.iloc[-1]['ds'].to_pydatetime()
    pastStandard = timedelta(hours=1)
    pastTime = lastTime - pastStandard
    # print(lastTime, pastTime)
    # print('===========================')
    closeDf = forecast[forecast['ds'] == pastTime]
    if len(closeDf) == 0:
        lastTime = data.iloc[-1]['ds'].to_pydatetime()
        pastTime = lastTime - pastStandard
        closeDf = forecast[forecast['ds'] == pastTime]
    closeValue = closeDf['yhat'].values[0]
    predicted_close_price = closeValue

    return predicted_close_price

COIN_NAME = "KRW-MVL"
current_price = get_current_price(COIN_NAME)
# target_price = get_target_price(COIN_NAME, 0.5)

predict_price_1hour = get_predict_price(COIN_NAME, after_hour=1)
predict_price_6hour = get_predict_price(COIN_NAME, after_hour=6)
predict_price_24hour = get_predict_price_24Hour(COIN_NAME)
ma15 = get_ma15(COIN_NAME)
print('현재가',current_price)
# print(target_price)
print('1시간', predict_price_1hour)
print('6시간', predict_price_6hour)
print('24시간', predict_price_24hour)
print('15일 이동평균선', ma15)
# schedule.every().hour.do(lambda: predict_price("KRW-BTC"))

# 로그인
# upbit = pyupbit.Upbit(access, secret)

# print("autotrade start")
# # 자동매매 시작
# while True:
#     try:
#         now = datetime.datetime.now()
#         start_time = get_start_time("KRW-BTC")
#         end_time = start_time + datetime.timedelta(days=1)
#         schedule.run_pending()

#         if start_time < now < end_time - datetime.timedelta(seconds=10):
#             target_price = get_target_price("KRW-BTC", 0.5)
#             current_price = get_current_price("KRW-BTC")
#             if target_price < current_price and current_price < predicted_close_price:
#                 krw = get_balance("KRW")
#                 if krw > 5000:
#                     upbit.buy_market_order("KRW-BTC", krw*0.9995)
#         else:
#             btc = get_balance("BTC")
#             if btc > 0.00008:
#                 upbit.sell_market_order("KRW-BTC", btc*0.9995)
#         time.sleep(1)
#     except Exception as e:
#         print(e)
#         time.sleep(1)