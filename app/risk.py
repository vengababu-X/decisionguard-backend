from config import WARNING_THRESHOLD, CRITICAL_THRESHOLD

def assess_risk(regret: float):
    if regret >= CRITICAL_THRESHOLD:
        return "CRITICAL"
    if regret >= WARNING_THRESHOLD:
        return "WARNING"
    return "STABLE"
