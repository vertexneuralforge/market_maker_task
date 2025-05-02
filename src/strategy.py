# Hybrid A-S + RL strategy
import numpy as np

class HybridStrategy:
    def __init__(self, rl_model=None, gamma=5.0):
        self.rl_model = rl_model  #  Trained PPO agent
        self.gamma = gamma        # Risk aversion
        
    def get_quotes(self, state):
        """Combines A-S math with RL adjustments"""
        # A-S Spread Calculation 
        spread = self.gamma * (state["volatility"] ** 1.5) * (1 - (state["inventory"]/3)**2)
        
        # RL Adjustment
        if self.rl_model:
            adj = self.rl_model.predict(state["rl_features"])[0]
            spread *= (1 + 0.2 * adj)  # Scale adjustment
            
        return (
            state["mid_price"] - spread/2,
            state["mid_price"] + spread/2
        )