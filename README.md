Jamf Device Report


Overview
Jamf Device Report is a comprehensive Power BI dashboard and Python-based data simulation project for IT device analytics.
It showcases simulated Apple device data (iPad, MacBook, Apple TV) across 6 departments to demonstrate asset management insights, compliance status, and operational performance typical of enterprise environments managed with Jamf and MDM solutions.

Key Features
• Interactive Power BI Dashboard
• Device, department, and OS version views
• Top KPIs: Department count, device count, battery %, security score, device type
• Compliance status (Compliant, Non-Compliant, Not-Reviewed)
• Date range, device-type, and OS slicers for easy drill-down
• Visual summaries and data table for instant insights
• Data Simulation and ETL (Python & SQLite)
• Generates realistic device data
• Event history for each device (uptime, security score, updates)
• Exports to CSV for direct Power BI use
• Modular code structure for easy customization

Data Structure
• data/device_summery.csv: Device properties and health metrics
• data/device_performance.csv: Daily device events and scores
• data/dept_summery.csv: Aggregated departmental statistics

How to Use
1. Clone the repository
git clone https://github.com/Shivam-choudhary554/Data_C.git
2. (Optional) Run the Python script
Rerun data generation for fresh device/event data:
python powerbi/setup_project.py
3. Open the Power BI file
• Load powerbi/Device_Dashbord.pbix in Power BI Desktop
• Interact using built-in slicers and filters

Screenshot

About The Project
This project was built as an end-to-end demo for IT Analytics, focusing on:
• Modern MDM/Apple device environments
• Departmental performance and compliance tracking
• Interview and portfolio-ready BI/analytics skills

Author
Shivam Choudhary
Wipro | Data Analytics, MDM <img width="917" height="2107" alt="image" src="https://github.com/user-attachments/assets/3d66166a-9483-48f8-baf0-d05412858377" />
