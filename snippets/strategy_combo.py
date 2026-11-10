"""Auszug aus backtester/strategies.py – kombinierte Strategie (SMA-Trendfilter + RSI-Einstieg).

Strategien liefern nur eine Positionsreihe (1 = long, 0 = flat) und nutzen ausschließlich Daten
bis zur aktuellen Kerze."""
import numpy as np
import pandas as pd

from . import indicators as ta


def combo(df: pd.DataFrame, fast: int = 20, slow: int = 50, period: int = 14, entry: int = 40,
          exit: int = 70, logic: str = "trend") -> pd.Series:
    close = df["close"]
    trend = ta.sma(close, fast) > ta.sma(close, slow)
    r = ta.rsi(close, period)
    sig = pd.Series(np.nan, index=df.index)
    if logic == "or":                                  # long, wenn SMA ODER RSI long sind
        sig[r < entry] = 1
        sig[r > exit] = 0
        return (trend | sig.ffill().fillna(0).astype(bool)).astype(int)
    sig[trend & (r < entry)] = 1                       # Kauf nur im Aufwärtstrend bei Rücksetzer
    sig[~trend | (r > exit)] = 0                       # Verkauf bei RSI-Hoch oder Trendbruch
    return sig.ffill().fillna(0).astype(int)
