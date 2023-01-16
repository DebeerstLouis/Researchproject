previous_measurements = []

while True:
    # read measurements from the meter
    current_measurements = read_meter()
    if current_measurements != previous_measurements:
        # send the measurements to InfluxDB
        client.write_api(write_options=SYNCHRONOUS).write(bucket, org, current_measurements)
        previous_measurements = current_measurements
    time.sleep(60)
