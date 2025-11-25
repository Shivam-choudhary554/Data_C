import os
import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

print(" Starting IT Asset Analytics Project Setup...\n")

folders = ['data', 'sql', 'python', 'powerbi', 'docs']
for folder in folders:
    os.makedirs(folder, exist_ok=True)
print(f"✓ Created folder: {folder}/")

db_path = 'data/it_asset_analytics.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
print(f"✓ Created database: {db_path}")

cursor.execute('''
               CREATE TABLE IF NOT EXISTS device (
               device_id TEXT PRIMARY KEY,
               device_name TEXT,
               device_type TEXT,
               os_version TEXT,
               last_seen DATE,
               compliance_status TEXT,
               battery_used REAL,
               device_model TEXT,
               storage_used_gb REAL,
               purchase_date DATE,
               department TEXT
               )
               ''')
cursor.execute('''
               CREATE TABLE IF NOT EXISTS device_events (
               event_id INTEGER PRIMARY KEY AUTOINCREMENT,
               device_id TEXT,
               event_date DATE,
               uptime_percentage REAL,
               security_score INTEGER,
               update_pending INTEGER,
               FOREIGN KEY (device_id) REFERENCES devices(device_id)
               )
               ''')
print("database has been created")

#create sample data

departments = ['IT','Finance','HR','Sales','Marketing','Operations']
os_versions = ['iOS 18.1','iOS 18.2', 'iOS 18.3','tvOS 18.1', 'tvOS 18.3']
models = ['iPad Pro','iPad Air','iPad','Apple TV 4K','Macbook Pro']
compliance_statuses = ['Compliant','Non-Compliant','Not-Reviewed']

devices = []
device_ids = []

for i in range(250):
    device_id = f"DEV-{str(i+1).zfill(5)}"
    device_name = f"Device-{i+1}"

    device = (
        device_id,
              f"Device-{i+1}",
              random.choice(['iPad','MacBook','Apple TV']),
              random.choice(os_versions),
              (datetime.now() - timedelta(days=random.randint(0, 30))).date(),
              random.choice (compliance_statuses),
              round(random.uniform(20, 100), 2),
              round(random.uniform(10, 256), 2),
              random.choice(models),
              (datetime.now() - timedelta(days=random.randint(365, 1095))) .date(),
              random.choice(departments)
              )
    devices.append(device)
    device_ids.append(device_id)

cursor.executemany('''
                   INSERT INTO device VALUES(?,?,?,?,?,?,?,?,?,?,?)
                   ''',devices)
#genrate event

events = []
for device_id in device_ids:
    for day in range(30):
        event_date = (datetime.now() - timedelta(days= day)).date()
        event = (
            device_id,
            event_date,
            round(random.uniform(85,100),2),
            random.randint(70,100),
            random.randint(0,5),
        )
        events.append(event)


cursor.executemany('''
                   INSERT INTO device_events VALUES (NULL,?,?,?,?,?)
                   ''',events)
conn.commit()

print(f"Genrate 250 device data for 30 days of event")

#now export data for power bi

device_summery = pd.read_sql_query('''
                                   SELECT device_id,device_name,device_type,
                                   os_version,compliance_status,battery_used,
                                   department,last_seen FROM device
                                   ''',conn)
device_perfomance = pd.read_sql_query('''
                                      SELECT d.device_id,d.device_name,d.department,de.event_date,
                                      de.uptime_percentage,de.security_score,de.update_pending
                                      FROM device d
                                      JOIN device_events de ON d.device_id = de.device_id 
                                      WHERE de.event_date >= date('now', '-7 days')
                                      ORDER BY de.event_date DESC
                                      ''',conn )
dept_summery = pd.read_sql_query('''
                                 SELECT department,device_id,COUNT(*) as Device_count,
                                 ROUND(AVG(Battery_used),2)as avg_battery,
                                 ROUND(AVG(Storage_used_gb),2)as avg_storage
                                 FROM device
                                 GROUP BY department
                                 ''',conn)
device_summery.to_csv('data/device_summery.csv',index=False)
device_perfomance.to_csv('data/device_performance.csv',index=False)
dept_summery.to_csv('data/dept_summery.csv',index=False)

print("Exported CSV into Power BI ")

conn.close()

print("\n" + "="*50)
print("setup is completed")
print("="*50)
print("\n files created")
print(f"database:data/it_asset_analytics.db")
print(f"CSV Export 1:data/device_summery.csv({len(device_summery)}rows)")
print(f"CSV Export 2:data/device_performace.csv({len(device_perfomance)}rows)")
print(f"CSV Export 3:data/dept_summery.csv({len(dept_summery)}rows)")


