import gymnasium as gym
import numpy as np
import pandas as pd
from gymnasium import spaces

class TradingEnv(gym.Env):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.current_step = 0
        
        # Action space: [spread_adjustment] between -1 and 1
        self.action_space = spaces.Box(low=-1, high=1, shape=(1,), dtype=np.float32)
        
        # State space: [price, volatility, inventory, latency, spread]
        self.observation_space = spaces.Box(
            low=-np.inf, 
            high=np.inf, 
            shape=(5,), 
            dtype=np.float32
        )
        
        # Initial state
        self.inventory = 0
        self.capital = 10000

    def reset(self, seed=None):
        self.current_step = 0
        self.inventory = 0
        self.capital = 10000
        return self._get_state(), {}

    def _get_state(self):
        row = self.data.iloc[self.current_step]
        return np.array([
            row["close"],            # Normalized price
            row["volatility"] * 100, # Volatility as percentage
            self.inventory / 10,     # Scaled inventory
            row["latency"] / 1000,   # Latency in seconds
            (row["ask"] - row["bid"]) / row["close"] if "ask" in row else 0.001  # Spread %
        ], dtype=np.float32)

    def step(self, action):
        # Get current market data
        row = self.data.iloc[self.current_step]
        mid_price = row["close"]
        
        # Apply action (RL adjustment)
        spread = 0.01 * mid_price  # Base spread
        adjusted_spread = spread * (1 + action[0])
        
        # Simulate trading 
        self.inventory += 1  # Simulate buy
        self.capital -= mid_price * (1 - adjusted_spread/2)
        
        # Calculate reward 
        portfolio_value = self.capital + self.inventory * mid_price
        reward = np.log(portfolio_value / 10000)  # Log-return
        
        # Update step
        self.current_step += 1
        done = self.current_step >= len(self.data) - 1
        
        return self._get_state(), reward, done, False, {}

    def render(self, mode='human'):
        print(f"Step: {self.current_step}, Inventory: {self.inventory}, Capital: ${self.capital:.2f}")
