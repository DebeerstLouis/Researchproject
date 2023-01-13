import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "mybucket"
org = "mct"
token = "NsSlXG_EQ4gGQD2sLwSRRmSbZuRZP-J55cy2KR9cwR7WFnFKUEdIh-01H9vYBjIC5ZQiAhXFStTSRXLJtNTHxA=="
# Store the URL of your InfluxDB instance
url="http://20.216.191.227:8086"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

# Prepare the data in line protocol format
data = [
    {
        "measurement": "electricity",
        "tags": {
            "Meter serial": "1SAG3100164832"
        },
        "fields": {
            "Timestamp": 230113153741.0,
            "Rate 1 (day) - total consumption": 6264.674,
            "Rate 2 (night) - total consumption": 9047.706,
            "Rate 1 (day) - total production": 3458.885,
            "Rate 2 (night) - total production": 1308.858,
            "Current rate (1=day,2=night)": 1.0
        }
    },
    {
        "measurement": "gas",
        "tags": {
            "Meter serial": "7FLO2119133113"
        },
        "fields": {
            "Switch gas": 1.0,
            "Gas consumption": 2735.156
        }
    }
]


write_api = client.write_api(write_options=SYNCHRONOUS)

# p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
# write_api.write(bucket=bucket, org=org, record=p,)

# Send the data to InfluxDB
# client.write_points(data)
write_api.write(bucket, org, data )
