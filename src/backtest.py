# Performance simulation engine
import pandas as pd

class Backtester:
    def __init__(self, data, strategy):
        self.data = data
        self.strategy = strategy
        
    def run(self):
        results = []
        for timestamp, row in self.data.iterrows():
            bid, ask = self.strategy.get_quotes(row)
            # Simulate trades and track PnL...
            results.append({"timestamp": timestamp, "bid": bid, "ask": ask})
        return pd.DataFrame(results)