def process_cloud_data(data):
    # Constants
    KW_PER_VCPU = 0.008  # Efficient cloud server wattage
    
    processed = []
    
    for item in data:
        # 1. Calculate Financial Cost
        total_cost = item['usage_hours'] * item['cost_hourly']
        
        # 2. Calculate Carbon Footprint
        # Formula: Hours * vCPU * Power * Grid Intensity / 1000 (to get kg)
        energy_kwh = item['usage_hours'] * item['vcpu'] * KW_PER_VCPU
        carbon_kg = (energy_kwh * item['carbon_intensity']) / 1000
        
        # 3. Generate AI Recommendation
        status = "Good"
        recommendation = "No action needed."
        
        if item['carbon_intensity'] > 400:
            status = "Critical"
            recommendation = "⚠️ High Carbon! Move workload to Sweden (eu-north-1)."
        elif item['cost_hourly'] > 1.0:
            status = "Warning"
            recommendation = "💰 High Cost! Consider using Spot Instances."

        processed.append({
            "name": item['name'],
            "region": item['region'],
            "cost": round(total_cost, 2),
            "carbon": round(carbon_kg, 2),
            "status": status,
            "recommendation": recommendation
        })
        
    return processed