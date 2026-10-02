import random

BASE_RATES = {"viscosity_change_pct": 0.022, "iron_ppm": 0.10, "soot_pct": 0.004, "tbn_loss_pct": 0.05}


def history(rate_mult=1.0, hours=300, step=50, seed=7):
    rnd = random.Random(seed)
    out = []
    for h in range(step, hours + 1, step):
        out.append((h, {k: r * rate_mult * h * rnd.gauss(1, 0.03) for k, r in BASE_RATES.items()}))
    return out
