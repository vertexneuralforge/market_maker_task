# RL training pipeline
from stable_baselines3 import PPO
from trading_env import TradingEnv
from strategy import HybridStrategy

def train():
    env = TradingEnv(load_clean_data())  # Data pipeline
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10_000)
    model.save("ppo_mm")
    
if __name__ == "__main__":
    train()