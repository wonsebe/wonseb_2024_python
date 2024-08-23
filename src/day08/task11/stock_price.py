#stock_price.py

class Stock_price:
    #생성자
    def __init__(self,date,closing_price,contrast,
                    fluctuation_rate,market_price,
                    costliness,low_price,trading_volume,transaction_amount,
                    market_capitalization,Number_of_listed_stocks):

        self.date=date          #일자
        self.closing_price = closing_price  #종가
        self.contrast = contrast    #대비
        self.fluctuation_rate = fluctuation_rate    #등락률
        self.market_price = market_price    #시가
        self.costliness = costliness    #고가
        self.low_price = low_price  #저가
        self.trading_volume = trading_volume    #거래량
        self.transaction_amount = transaction_amount    #거래대금
        self.market_capitalization = market_capitalization  #시가총액
        self.Number_of_listed_stocks = Number_of_listed_stocks  #상장주식수



