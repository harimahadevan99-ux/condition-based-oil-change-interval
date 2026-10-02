LIMITS = {"viscosity_change_pct": 20.0, "iron_ppm": 100.0, "soot_pct": 3.5, "tbn_loss_pct": 50.0}


def condition_index(sample):
    # worst parameter relative to its limit; 1.0 means limit reached
    return max(sample[k] / v for k, v in LIMITS.items())


def forecast_hours_to_limit(history, last_n=6):
    pts = history[-last_n:]
    xs = [h for h, _ in pts]
    ys = [condition_index(s) for _, s in pts]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    if slope <= 0:
        return None
    return mx + (1.0 - my) / slope


def plan(history, fixed_interval_h=500, safety=0.9, oil_l=40.0):
    limit_h = forecast_hours_to_limit(history)
    rec = None if limit_h is None else round(limit_h * safety)
    out = {"forecast_limit_h": None if limit_h is None else round(limit_h), "recommended_change_h": rec}
    if rec:
        out["delta_vs_fixed_h"] = rec - fixed_interval_h
        out["oil_l_saved_per_1000h"] = round(max(0.0, 1000 / fixed_interval_h - 1000 / rec) * oil_l, 1)
        out["verdict"] = "extend interval" if rec > fixed_interval_h else "change earlier than fixed interval"
    return out
