def enrich_customer_data(customer_record):
    """
    Enrichment logic:
    - Add risk score
    - Add loyalty tier
    """
    risk_score = 0
    if customer_record.get("country") in ["US", "UK"]:
        risk_score = 2
    else:
        risk_score = 5

    loyalty_points = customer_record.get("loyalty_points", 0)
    if loyalty_points > 2000:
        tier = "GOLD"
    elif loyalty_points > 700:
        tier = "SILVER"
    else:
        tier = "BRONZE"

    enriched_record = {
        **customer_record,
        "risk_score": risk_score,
        "loyalty_tier": tier
    }

    return enriched_record
