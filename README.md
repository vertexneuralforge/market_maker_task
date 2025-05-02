# market_maker_task

# AI Market Maker Test Task
# RL-Enhanced Market Maker for On-Chain Trading

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Hybrid market-making strategy combining Avellaneda-Stoikov model with Reinforcement Learning, optimized for on-chain trading pairs (USD+/wETH and USD+/cbbtc).

## Features

- **Hybrid AS-RL Model**: Combines quantitative finance with modern RL
- **On-Chain Focus**: 1inch PMM and Hashflow PMM integration ready
- **Latency-Aware**: Accounts for blockchain confirmation times
- **Multi-Exchange Data**: Incorporates Binance CEX data
- **Comprehensive Backtesting**: Full trading simulation framework


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
   
2. Clone repository:
```bash
git clone https://github.com/vertexneuralforge/market_maker_task.git
cd market_maker_task
