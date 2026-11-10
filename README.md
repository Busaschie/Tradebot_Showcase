# Trading Backtester – crypto strategy backtests with Django

> **Showcase repository.** Description and selected code excerpts of a project, published for application purposes only. The full source code is not part of this repository. See [LICENSE](LICENSE).

**English** · [Deutsch](#deutsch)

## Try it live
**<https://python-django-blockchain.onrender.com/demo/>** – no sign-up: one click creates a temporary demo account with a ready example run. Demo accounts are limited (20 runs, 5 AI calls) and deleted after 48 hours. The free hosting may need a few seconds to wake up.

## What it is
A web app that tests trading strategies on past crypto prices (Bitcoin, Solana, Ethereum) and judges how trustworthy the result is – not only how good it looks. Backtests, validation, risk management, paper trading and a rule-based or AI-written commentary in one UI, available in German and English.

## Highlights
- **Honest backtests:** signals only act on the next candle (no look-ahead), fees and slippage included, execution at the next open or at the close.
- **Validation instead of curve fitting:** train/test split and walk-forward (parameters chosen on train data only, judged on unseen data), parameter stability heatmap, Monte Carlo and market-regime checks.
- **Strategies:** SMA crossover, RSI, combined SMA + RSI, Bollinger; stop-loss, take-profit, trailing stop and position sizing (full / fixed / volatility target).
- **Plausibility and confidence checks** that warn about too few trades, unstable parameters or results that depend on a single period.
- **Data robustness:** candle cache in the database, Binance archive, exchange-block protection against IP bans; six exchanges via ccxt.
- **Paper trading and current signal** with optional e-mail on signal change.
- **AI commentary on demand** (Groq), always with a rule-based fallback; natural-language strategy input.
- **Demo access:** fixed public link, temporary accounts, hard limits and locked features (see `snippets/demo_accounts.py`).
- **Quality:** about 340 tests incl. browser tests (Playwright), hand calculations for stops and sizing, a cross-check against backtesting.py, CI on GitHub Actions.

## Architecture
```
Browser ── Django views ──► jobs (thread pool) ──► engine · strategies · validation
   │                              │
   │                              ▼
   │                  marketdata: DB candle cache ─ Binance archive ─ ccxt API
   ▼
 PostgreSQL (Neon) / SQLite · Plotly charts · i18n layer (DE/EN)
```
Hosted on Render (gunicorn, WhiteNoise) with Neon PostgreSQL.

## Code excerpts
| File | Shows |
|---|---|
| [`snippets/engine_no_lookahead.py`](snippets/engine_no_lookahead.py) | next-candle execution, gap and intraday return, fees |
| [`snippets/strategy_combo.py`](snippets/strategy_combo.py) | combined trend + RSI strategy as a pure position series |
| [`snippets/demo_accounts.py`](snippets/demo_accounts.py) | demo accounts: activity-based slots, cleanup after 48 h |

## Tech stack
Python 3.13 · Django 6 · pandas / NumPy · TA-Lib · ccxt · Plotly · PostgreSQL (Neon) · gunicorn · WhiteNoise · Playwright · GitHub Actions

## Notice
Backtests use past prices. This is no investment advice.

## Author
Niko – Python/Django developer with a focus on LLM orchestration. Background: Python/Django, UX, HTML/CSS.

---

## Deutsch
**Trading Backtester – Krypto-Strategien mit Django testen**

> **Schaufenster-Repository.** Beschreibung und ausgewählte Code-Ausschnitte eines Projekts, nur zu Bewerbungszwecken veröffentlicht. Der vollständige Quellcode gehört nicht dazu. Siehe [LICENSE](LICENSE).

### Live ausprobieren
**<https://python-django-blockchain.onrender.com/demo/>** – ohne Anmeldung: ein Klick legt ein temporäres Demo-Konto mit fertigem Beispiel-Lauf an. Demo-Konten sind begrenzt (20 Läufe, 5 KI-Aufrufe) und werden nach 48 Stunden gelöscht. Beim kostenlosen Hosting kann das Aufwachen einige Sekunden dauern.

### Worum es geht
Eine Web-App, die Handelsstrategien auf vergangenen Kursen (Bitcoin, Solana, Ethereum) testet und bewertet, wie belastbar das Ergebnis ist – nicht nur, wie gut es aussieht. Backtest, Validierung, Risikomanagement, Paper-Trading und ein regelbasierter oder KI-Kommentar in einer Oberfläche, auf Deutsch und Englisch.

### Besonderheiten
- **Ehrliche Backtests:** Signale wirken erst auf der Folgekerze (kein Blick in die Zukunft), Gebühren und Slippage, Ausführung zum nächsten Open oder zum Schluss.
- **Validierung statt Überanpassung:** Train/Test-Split und Walk-Forward (Parameter nur auf Train gewählt, auf ungesehenen Daten bewertet), Stabilitäts-Heatmap, Monte Carlo und Marktphasen-Prüfung.
- **Strategien:** SMA-Crossover, RSI, Kombiniert (SMA + RSI), Bollinger; Stop-Loss, Take-Profit, Trailing-Stop und Positionsgröße (voll / fest / Volatilitätsziel).
- **Plausibilitäts- und Vertrauensprüfung:** warnt bei zu wenigen Trades, instabilen Parametern oder Ergebnissen, die an einem einzigen Zeitraum hängen.
- **Datenrobustheit:** Kerzen-Cache in der Datenbank, Binance-Archiv, Sperren-Schutz gegen IP-Sperren; sechs Börsen über ccxt.
- **Paper-Trading und aktuelles Signal** mit optionaler Mail bei Signalwechsel.
- **KI-Kommentar auf Knopfdruck** (Groq), immer mit regelbasiertem Ersatz; Strategie in natürlicher Sprache.
- **Demo-Zugang:** fester öffentlicher Link, temporäre Konten, harte Grenzen und gesperrte Funktionen (siehe `snippets/demo_accounts.py`).
- **Qualität:** rund 340 Tests inkl. Browser-Tests (Playwright), Handrechnungen für Stops und Sizing, Gegenrechnung mit backtesting.py, CI auf GitHub Actions.

### Technik
Python 3.13 · Django 6 · pandas / NumPy · TA-Lib · ccxt · Plotly · PostgreSQL (Neon) · gunicorn · WhiteNoise · Playwright · GitHub Actions

### Hinweis
Backtests rechnen mit vergangenen Kursen. Keine Anlageberatung.
