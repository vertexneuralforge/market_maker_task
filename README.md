# market_maker_task

# AI Market Maker Test Task

## Solution Overview
- **Hybrid Strategy**: Combines Avellaneda-Stoikov with PPO reinforcement learning
- **Key Metrics**:
  - Sharpe Ratio: 0.10 → 0.85 after tuning
  - Max Drawdown: $63.04 (0.63% of capital)
- **Innovations**:
  - Latency-aware spread adjustment
  - Volatility-scaled inventory control

## How to Reproduce
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
