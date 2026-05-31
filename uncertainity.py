import random

print("=== AI Decision Making Under Uncertainty Simulation ===")

# Generate uncertain traffic conditions
vehicle_count = random.randint(0, 50)
pedestrian_waiting = random.choice([True, False])
sensor_confidence = random.randint(60, 100)

print("\nTraffic Data:")
print("Vehicle Count:", vehicle_count)
print("Pedestrian Waiting:", pedestrian_waiting)
print("Sensor Confidence:", sensor_confidence, "%")

# Probability estimation
if vehicle_count > 30:
    traffic_state = "High"
elif vehicle_count > 15:
    traffic_state = "Medium"
else:
    traffic_state = "Low"

# AI Decision Making
if sensor_confidence < 70:
    decision = "STOP (Low Sensor Confidence)"
elif traffic_state == "High":
    decision = "EXTEND GREEN SIGNAL"
elif traffic_state == "Medium":
    decision = "KEEP GREEN SIGNAL"
elif traffic_state == "Low" and pedestrian_waiting:
    decision = "SWITCH TO RED SIGNAL"
else:
    decision = "KEEP GREEN SIGNAL"

print("\nEstimated Traffic State:", traffic_state)
print("AI Decision:", decision)

print("\nSimulation Completed")
