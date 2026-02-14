import boto3, time
import pandas as pd
import argparse
from CONSTANTS import PROFILE, REGION, WORKGROUP_NAME, DATABASE, DB_USER, NATIVE_DB

PROFILE = PROFILE
REGION = REGION

WORKGROUP_NAME = WORKGROUP_NAME
DATABASE = DATABASE
DB_USER = DB_USER
NATIVE_DB = NATIVE_DB

def quote_identifier(identifier):
    parts = identifier.split(".")
    quoted = [f'"{p}"' for p in parts]
    return ".".join(quoted)

parser = argparse.ArgumentParser()
parser.add_argument("table", help="Table in schema.table format")
args = parser.parse_args()

table_name = quote_identifier(args.table)
QUERY = f'SELECT * FROM "{NATIVE_DB}".{table_name} LIMIT 50;'

session = boto3.Session(profile_name=PROFILE)
client = session.client("redshift-data", region_name=REGION)

response = client.execute_statement(
    WorkgroupName = WORKGROUP_NAME,
    Database = DATABASE,
    Sql = QUERY
)

statement_id = response["Id"]

while True:
    status = client.describe_statement(Id=statement_id)

    if status["Status"] in ["FINISHED", "FAILED", "ABORTED"]:
        break

    time.sleep(1)

if status["Status"] != "FINISHED":
    print("Query status:", status["Status"])
    print("Error:", status.get("Error"))
    raise Exception("Query failed")

result = client.get_statement_result(Id=statement_id)

columns = [c["name"] for c in result["ColumnMetadata"]]

rows = []
for record in result["Records"]:
    row = [list(col.values())[0] if col else None for col in record]
    rows.append(row)

df = pd.DataFrame(rows, columns=columns)
df.to_csv("output.csv", index=False)

print("CSV exported!")