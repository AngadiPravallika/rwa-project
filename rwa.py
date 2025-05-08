# RWA Sentinel: Multi-Agent AI Simulation (Kaggle Version)

import random
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------
# Sample Tokenized Assets & User Wallets
# -------------------------------------
assets = [
    {"id": 101, "owner": "0xABC123", "history": "on-time", "value": 10000, "tx_volume": 5},
    {"id": 102, "owner": "0xDEF456", "history": "late", "value": 7500, "tx_volume": 25},
    {"id": 103, "owner": "0xGHI789", "history": "unknown", "value": 15000, "tx_volume": 2},
    {"id": 104, "owner": "0xJKL012", "history": "on-time", "value": 18000, "tx_volume": 55},
]

users = {
    "0xABC123": {"civic_verified": True},
    "0xDEF456": {"civic_verified": False},
    "0xGHI789": {"civic_verified": True},
    "0xJKL012": {"civic_verified": False},
}

# -------------------------------------
# AI Agent 1: Risk Scoring Agent
# -------------------------------------
def score_rwa(asset):
    """Assign a risk score based on payment history."""
    if asset["history"] == "on-time":
        return random.randint(10, 30)
    elif asset["history"] == "late":
        return random.randint(50, 80)
    else:
        return random.randint(30, 60)

# -------------------------------------
# AI Agent 2: Compliance Agent (Civic Auth Simulation)
# -------------------------------------
def validate_kyc(wallet_address):
    """Check if the user's wallet is KYC-verified."""
    return users.get(wallet_address, {}).get("civic_verified", False)

# -------------------------------------
# AI Agent 3: Anomaly Detection Agent
# -------------------------------------
def detect_fraud(asset):
    """Flag unusually high transaction volume as potential fraud."""
    threshold = 30
    return asset["tx_volume"] > threshold

# -------------------------------------
# Run Simulation for All Agents
# -------------------------------------
def run_simulation():
    results = []

    for asset in assets:
        risk_score = score_rwa(asset)
        kyc_verified = validate_kyc(asset["owner"])
        fraud_flag = detect_fraud(asset)

        results.append({
            "Asset ID": asset["id"],
            "Owner": asset["owner"],
            "History": asset["history"],
            "Value ($)": asset["value"],
            "Risk Score": risk_score,
            "KYC Verified": "✅" if kyc_verified else "❌",
            "Fraud Suspected": "⚠️ Yes" if fraud_flag else "No"
        })

    return pd.DataFrame(results)

if __name__ == "__main__":
    df = run_simulation()
    styled_df = df.style.background_gradient(subset=["Risk Score"], cmap='Oranges')
    print(df)
