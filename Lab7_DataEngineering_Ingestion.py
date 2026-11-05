# Lab 7 - Data Engineering Ingestion

# Exercise 1: Basic Data Ingestion
source_data = [120, 250, 180, 300, 150]
destination_data = []

for record in source_data:
    destination_data.append(record)

print("========== Exercise 1 ==========")
print("Source data:", source_data)
print("Destination data:", destination_data)
print("Records ingested:", len(destination_data))


# Exercise 2: Schema Validation
events = [
    {"event_id": "E101", "event_type": "click", "user_id": 10},
    {"event_id": "E102", "event_type": "purchase", "user_id": 20},
    {"event_id": "E103", "event_type": "click"},
    {"event_id": "E104", "event_type": "view", "user_id": "unknown"}
]

valid_events = []
invalid_events = []

for event in events:
    if (
        "event_id" in event
        and "event_type" in event
        and isinstance(event.get("user_id"), int)
        and not isinstance(event.get("user_id"), bool)
    ):
        valid_events.append(event)
    else:
        invalid_events.append(event)

print("\n========== Exercise 2 ==========")
print("Valid records:", len(valid_events))
print("Invalid records:", len(invalid_events))
print("Accepted events:", valid_events)


# Exercise 3: Incremental Data Extraction
all_records = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"},
    {"id": 3, "name": "Omar"},
    {"id": 4, "name": "Mona"}
]

last_processed_id = 2
new_records = []

for record in all_records:
    if record["id"] > last_processed_id:
        new_records.append(record)

print("\n========== Exercise 3 ==========")
print("New records:", new_records)
print("Records ingested:", len(new_records))


# Exercise 4: Handling Invalid Records with a Dead-Letter Queue
sensor_data = [25.5, 26.0, "error", 24.8, None, 27.1]

main_queue = []
dead_letter_queue = []

for reading in sensor_data:
    if isinstance(reading, (int, float)) and not isinstance(reading, bool):
        main_queue.append(reading)
    else:
        dead_letter_queue.append(reading)

print("\n========== Exercise 4 ==========")
print("Accepted readings:", main_queue)
print("Rejected readings:", dead_letter_queue)
print("Accepted count:", len(main_queue))
print("Rejected count:", len(dead_letter_queue))


# Exercise 5: Processing Bounded Data (Batch Filtering)
daily_sales_batch = [
    {"order_id": "A1", "status": "completed", "total": 150},
    {"order_id": "A2", "status": "pending", "total": 75},
    {"order_id": "A3", "status": "completed", "total": 200},
    {"order_id": "A4", "status": "cancelled", "total": 50}
]

def process_bounded_batch(records):
    """Filters finite bounded data for batch processing reporting."""
    print("\n--- Processing Bounded Batch Data ---")
    completed_orders = []

    for record in records:
        if record["status"] == "completed":
            completed_orders.append(record)

    return completed_orders

final_batch = process_bounded_batch(daily_sales_batch)

print("Total records processed:", len(daily_sales_batch))
print("Completed Orders for Storage:")

for order in final_batch:
    print(order)
