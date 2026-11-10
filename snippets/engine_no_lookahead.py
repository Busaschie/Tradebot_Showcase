"""Auszug aus backtester/engine.py – Look-ahead-Schutz und Ausführung zum Eröffnungskurs.

Das Signal der Kerze t wird erst ab Kerze t+1 gehandelt (shift(1)). Bei Ausführung zum Open
wirken die Kurslücke (Vortagesschluss -> Open) und der Intraday-Teil nacheinander."""
import pandas as pd


def simulate(df: pd.DataFrame, signal: pd.Series, fee: float = 0.001, execution: str = "close"):
    a = signal.shift(1).fillna(0)                      # Zielposition, ab Kerze t gültig
    ret = df["close"].pct_change().fillna(0)
    if execution == "open":
        b = a.shift(1).fillna(0)                       # über die Kerzengrenze gehaltene Position
        gap = (df["open"] / df["close"].shift(1) - 1).fillna(0)
        intra = df["close"] / df["open"] - 1
        strat = (1 + b * gap) * (1 + a * intra) - 1 - (a - b).abs() * fee
    else:
        turnover = a.diff().abs().fillna(a.abs())
        strat = a * ret - turnover * fee
    return a, ret, strat
