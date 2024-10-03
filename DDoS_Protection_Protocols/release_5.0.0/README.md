# README for Apstra Analytics Components

## Overview of Intent-Based Analytics (IBA)

Intent-Based Analytics (IBA) is a powerful feature of Apstra that allows for the creation of custom analytics services, collectors, probes, and dashboards. This package includes examples of these components focused on DDoS Protection Protocols.

The main components are:
1. A custom analytics service defined in `DDoS_Protection_Protocols.json`
2. A dashboard with associated probes and widgets defined in `Dashboard - DDoS Protection Protocols Dashboard.json`

## How to Import

To import these components into your Apstra environment:

1. Log in to your Apstra instance
2. For the custom service:
   - Navigate to the Analytics section on the left hand side
   - Go to the 'Services' tab
   - Click 'Import Service Scheme'
   - Select the `DDoS_Protection_Protocols.json` file
4. For the dashboard:
   - Go to the your blueprint
   - Go to the 'Analytics > Dashboards' tab
   - Click 'Create Dashboard'and select 'Import Dashboard'
   - Select the `Dashboard - DDoS Protection Protocols Dashboard.json` file

After importing, you may need to adjust any system-specific settings or filters to match your environment.

## Reporting Issues

If you encounter any issues or have suggestions for improvements, please report them through the GitHub Issues page for this repository. When reporting an issue, please include:

- A clear description of the problem
- Steps to reproduce the issue
- Any relevant error messages or screenshots
- Your Apstra version