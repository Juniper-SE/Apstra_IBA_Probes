# Repository Check Scripts

A collection of Python scripts to validate repository structure and content.

## Usage

### Running All Checks
```bash
python3 _repository_checks/check_all.py
```

### Running Individual Checks
```bash
python3 _repository_checks/check_structure.py
python3 _repository_checks/check_json_yaml.py
python3 _repository_checks/check_images.py
```

## Features

- Validates repository structure for both 4.2.1 and 5.0.0+ releases
- Checks JSON and YAML syntax
- Validates image references in README files
- Identifies unused images
- Generates clear, colorful reports with emojis

## Report Features

The script generates colorful, emoji-enhanced output with:
- Individual release reports
- Component-level details
- Summary tally of all issues
- Clear error and warning indicators

```Example
============================================================
Repository Validation
============================================================


============================================================
📦 Checking Release: release_4.2.1
============================================================


============================================================
Structure Validation
============================================================


📁 OS_Version_Compliance:
❌     Missing Content/configlets directory

📁 System_Alarm:
❌     Missing Content/configlets directory
❌     Missing Content/property-sets directory

📁 Interface_Flap:
❌     Missing Content/configlets directory
❌     Missing Content/property-sets directory

📁 DDoS_Protection_Protocols:
❌     Missing Content/configlets directory
❌     Missing Content/dashboards directory
❌     Missing Content/property-sets directory
❌     Missing Content/widgets directory

📁 Device_Uptime:
❌     Missing Content/configlets directory
❌     Missing Content/property-sets directory

📁 Loop_Detection:
❌     Missing Content/dashboards directory

============================================================
JSON/YAML Validation
============================================================


📊 Invalid JSON files:
❌     ping-mesh-intra-fabric.json at line 3: Expecting property name enclosed in double quotes: line 3 column 5 (char 30)
Context: // "__widget_id_label_dict": {
❌     ping-mesh-external-to-fabric.json at line 3: Expecting property name enclosed in double quotes: line 3 column 5 (char 30)
Context: // "__widget_id_label_dict": {
❌     leaf-to-leaf-overlay.json at line 3: Expecting property name enclosed in double quotes: line 3 column 5 (char 41)
Context: // "__blueprint_id": "evpn-vex-virtual",
❌     external-rtt-last-1h.json at line 3: Expecting property name enclosed in double quotes: line 3 column 5 (char 41)
Context: // "__blueprint_id": "evpn-vex-virtual",
❌     leaf-to-leaf-underlay.json at line 3: Expecting property name enclosed in double quotes: line 3 column 5 (char 41)
Context: // "__blueprint_id": "evpn-vex-virtual",
❌     leaf-to-ext-rtr.json at line 3: Expecting property name enclosed in double quotes: line 3 column 5 (char 41)
Context: // "__blueprint_id": "evpn-vex-virtual",
❌     overlay-rtt-last-1h.json at line 3: Expecting property name enclosed in double quotes: line 3 column 5 (char 41)
Context: // "__blueprint_id": "evpn-vex-virtual",
❌     underlay-rtt-last-1h.json at line 3: Expecting property name enclosed in double quotes: line 3 column 5 (char 41)
Context: // "__blueprint_id": "evpn-vex-virtual",
❌     interface-flap.json at line 12: Expecting property name enclosed in double quotes: line 12 column 5 (char 223)
Context: // "__blueprint_id": "evpn-vex-virtual",
❌     excessive-interface-fabric-interfaces.json at line 5: Expecting property name enclosed in double quotes: line 5 column 5 (char 106)
Context: // "probe_id": "3d85cb91-2325-46c2-b81d-a2211b6921f9",
❌     excessive-interface-server-facing-interfaces.json at line 5: Expecting property name enclosed in double quotes: line 5 column 5 (char 113)
Context: // "probe_id": "3d85cb91-2325-46c2-b81d-a2211b6921f9",
❌     system-rebooted-in-last-history.json at line 16: Expecting property name enclosed in double quotes: line 16 column 5 (char 335)
Context: // "__blueprint_id": "evpn-vex-virtual",
❌     system-uptime-System_Uptime.json at line 22: Invalid \escape: line 22 column 44 (char 773)
Context: "value": "int(re_search(r'(\d+)(?=w)', System_Uptime) or 0) * 10080 + int(re_search(r'(\d+)(?=\sd)', System_Uptime) or 0) * 1440 + int(re_search(r'(\d+)(?=:)', System_Uptime.split()[-1]) or 0) * 60 + int(re_search(r'(?<=:)(\d+)', System_Uptime.split()[-1]) or 0) if 'w' in System_Uptime or 'd' in System_Uptime or ':' in System_Uptime else int(re_search(r'(\d+)(?=\smins)', System_Uptime) or 0)",
❌     system-rebooted-in-last-hour.json at line 5: Expecting property name enclosed in double quotes: line 5 column 5 (char 96)
Context: // "probe_id": "8050e7a4-7c68-4a4c-8ef9-dcba568ebbc9",
❌     system-rebooted-in-last-week.json at line 5: Expecting property name enclosed in double quotes: line 5 column 5 (char 96)
Context: // "probe_id": "8050e7a4-7c68-4a4c-8ef9-dcba568ebbc9",
❌     system-rebooted-in-last-day.json at line 4: Expecting property name enclosed in double quotes: line 4 column 5 (char 72)
Context: // "probe_id": "8050e7a4-7c68-4a4c-8ef9-dcba568ebbc9",

============================================================
Image Validation
============================================================


----------------------------------------
Checking Component: OS_Version_Compliance
----------------------------------------

✅ No image issues found in OS_Version_Compliance

----------------------------------------
Checking Component: Ping_Mesh
----------------------------------------

🖼️ Broken Links:
❌     ./release_4.2.1/Ping_Mesh/README.md -> Ping-Mesh_Widget_x.png

🖼️ Unused Images:
⚠️     Images/Ping-Mesh_Probe_Pipeline.png

----------------------------------------
Checking Component: System_Alarm
----------------------------------------

✅ No image issues found in System_Alarm

----------------------------------------
Checking Component: Interface_Flap
----------------------------------------

✅ No image issues found in Interface_Flap

----------------------------------------
Checking Component: OSPF_Neighbor
----------------------------------------

🖼️ Unused Images:
⚠️     Images/OSPF-Neighbor_Collector.png

----------------------------------------
Checking Component: DDoS_Protection_Protocols
----------------------------------------

🖼️ Broken Links:
❌     ./release_4.2.1/DDoS_Protection_Protocols/README.md -> Device-Uptime_Probe_Stage_Widget_1.png
❌     ./release_4.2.1/DDoS_Protection_Protocols/README.md -> Device-Uptime_Dashboard.png

----------------------------------------
Checking Component: Device_Uptime
----------------------------------------

✅ No image issues found in Device_Uptime

----------------------------------------
Checking Component: Loop_Detection
----------------------------------------

✅ No image issues found in Loop_Detection

============================================================
📦 Checking Release: release_5.0.0
============================================================


============================================================
Structure Validation
============================================================


📁 OS_Version_Compliance:
❌     Missing Content directory
❌     Missing Images directory

📁 Ping_Mesh:
❌     Missing Content directory
❌     Missing Images directory

📁 System_Alarm:
❌     Missing Content directory
❌     Missing Images directory

📁 Interface_Flap:
❌     Missing Content directory
❌     Missing Images directory

📁 OSPF_Neighbor:
❌     Missing Content directory
❌     Missing Images directory

📁 DDoS_Protection_Protocols:
❌     Missing Content directory
❌     Missing Images directory

📁 Device_Uptime:
❌     Missing Content directory
❌     Missing Images directory

============================================================
JSON/YAML Validation
============================================================

✅ No JSON/YAML issues found

============================================================
Image Validation
============================================================


----------------------------------------
Checking Component: OS_Version_Compliance
----------------------------------------

✅ No image issues found in OS_Version_Compliance

----------------------------------------
Checking Component: Ping_Mesh
----------------------------------------

✅ No image issues found in Ping_Mesh

----------------------------------------
Checking Component: System_Alarm
----------------------------------------

✅ No image issues found in System_Alarm

----------------------------------------
Checking Component: Interface_Flap
----------------------------------------

✅ No image issues found in Interface_Flap

----------------------------------------
Checking Component: OSPF_Neighbor
----------------------------------------

✅ No image issues found in OSPF_Neighbor

----------------------------------------
Checking Component: DDoS_Protection_Protocols
----------------------------------------

✅ No image issues found in DDoS_Protection_Protocols

----------------------------------------
Checking Component: Device_Uptime
----------------------------------------

✅ No image issues found in Device_Uptime

============================================================
Final Summary
============================================================

ℹ️ Scope:
    Releases checked: 2
    Components checked: 15

❌ Errors Found:
    Structure issues: 26
    Invalid JSON files: 16
    Invalid YAML files: 0
    Broken image links: 3

⚠️ Warnings Found:
    Unused images: 2

❌ Found 45 errors and 2 warnings.

```


## Exit Codes
- 0: All checks passed
- 1: Issues found or errors occurred

## Adding New Checks

To add new checks:
1. Create a new Python script in the scripts directory
2. Follow the pattern of existing scripts
3. Add the new check to check_all.py if needed

## Requirements

- Python 3.6 or higher
- PyYAML package for YAML validation
