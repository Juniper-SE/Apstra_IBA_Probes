- CLI Command: `show system uptime` - [Junos documentation page](https://www.juniper.net/documentation/us/en/software/junos/junos-overview/topics/ref/command/show-system-uptime.html#:~:text=The%20show%20system%20uptime%20command%20by%20itself%20shows%20system%2Dwide,%7C%20re1%20%7C%20fpc0%20%7C%20all%20). 
- Sample Output:
```
Current time: 2023-12-14 11:31:56 UTC
Time Source:  LOCAL CLOCK 
System booted: 2023-10-30 17:31:27 UTC (6w2d 18:00 ago)
Protocols started: 2023-10-30 17:32:34 UTC (6w2d 17:59 ago)
Last configured: 2023-12-06 10:46:26 UTC (1w1d 00:45 ago) by aosadmin
11:31AM  up 44 days, 18 hrs, 0 users, load averages: 1.30, 0.95, 0.83
```
- Fields of interest:
| Field | Information |
| --- | --- |
| `Time Source` | Time source that the system is locked to. Possible values are `LOCAL CLOCK`, `NTP CLOCK` |
| `System booted` | Time system was last booted |
- Notes:
  - The format of the `System booted` value varies depending on how long the device is up and running. Examples values includes:
    - `00:03:38` --> 3 minutes and 38 seconds.
    - `1d 20:47` --> 1 day, 20 hours and 47 minutes.
    - `6w2d 18:03` --> 6 weeks, 2 days, 18 hours and 3 minutes.
