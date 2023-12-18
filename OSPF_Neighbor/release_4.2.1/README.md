# OPSF Neighbor Check

## Description of the use-case

- xxx
- xxx

## Identification of the source data (raw data)

- CLI Command: `show ospf neighbor instance <routing-instance-name> extensive` - [Junos documentation page](https://www.juniper.net/documentation/us/en/software/junos/ospf/topics/ref/command/show-ospf-ospf3-neighbor.html). 
- Sample Text Output:
```
Address          Interface              State           ID               Pri  Dead
10.110.36.3      irb.1390               Full            10.252.0.7       128    34
  Area 0.0.0.0, opt 0x52, DR 10.110.36.62, BDR 10.110.36.2
  Up 5d 16:08:43, adjacent 5d 16:08:43
  Topology default (ID 0) -> Bidirectional
10.110.36.62     irb.1390               Full            192.168.255.255  128    31
  Area 0.0.0.0, opt 0x52, DR 10.110.36.62, BDR 10.110.36.2
  Up 1w1d 00:14:44, adjacent 1w1d 00:14:43
  Topology default (ID 0) -> Bidirectional
```
<details>
    <summary>Sample XML Output:</summary>

```xml
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/23.2R1.14/junos">
    <ospf-neighbor-information xmlns="http://xml.juniper.net/junos/23.2R0/junos-routing">
        <ospf-neighbor>
            <neighbor-address>10.110.36.3</neighbor-address>
            <interface-name>irb.1390</interface-name>
            <ospf-neighbor-state>Full</ospf-neighbor-state>
            <neighbor-id>10.252.0.7</neighbor-id>
            <neighbor-priority>128</neighbor-priority>
            <activity-timer>38</activity-timer>
            <ospf-area>0.0.0.0</ospf-area>
            <options>0x52</options>
            <dr-address>10.110.36.62</dr-address>
            <bdr-address>10.110.36.2</bdr-address>
            <neighbor-up-time junos:seconds="490384">
                5d 16:13:04
            </neighbor-up-time>
            <neighbor-adjacency-time junos:seconds="490384">
                5d 16:13:04
            </neighbor-adjacency-time>
            <ospf-neighbor-topology>
                <ospf-topology-name>default</ospf-topology-name>
                <ospf-topology-id>0</ospf-topology-id>
                <ospf-neighbor-topology-state>Bidirectional</ospf-neighbor-topology-state>
            </ospf-neighbor-topology>
        </ospf-neighbor>
        <ospf-neighbor>
            <neighbor-address>10.110.36.62</neighbor-address>
            <interface-name>irb.1390</interface-name>
            <ospf-neighbor-state>Full</ospf-neighbor-state>
            <neighbor-id>192.168.255.255</neighbor-id>
            <neighbor-priority>128</neighbor-priority>
            <activity-timer>32</activity-timer>
            <ospf-area>0.0.0.0</ospf-area>
            <options>0x52</options>
            <dr-address>10.110.36.62</dr-address>
            <bdr-address>10.110.36.2</bdr-address>
            <neighbor-up-time junos:seconds="692345">
                1w1d 00:19:05
            </neighbor-up-time>
            <neighbor-adjacency-time junos:seconds="692344">
                1w1d 00:19:04
            </neighbor-adjacency-time>
            <ospf-neighbor-topology>
                <ospf-topology-name>default</ospf-topology-name>
                <ospf-topology-id>0</ospf-topology-id>
                <ospf-neighbor-topology-state>Bidirectional</ospf-neighbor-topology-state>
            </ospf-neighbor-topology>
        </ospf-neighbor>
    </ospf-neighbor-information>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>
```
</details>
  
<br>

- Fields of interest:

| Field | Information |
| --- | --- |
| `Address` | OSPF neighbor IP. |
| `Interface` | Interface through which the neighbor is reachable. |
| `Area` | OSPF area that the neighbor is in. |
| `State` | State of the neighbor. Possible values will be the following enum: `Attempt`, `Down`, `Exchange`, `ExStart`, `Full`, `Init`, `Loading` or `2Way`. |
| `adjacent` | Length of time since the adjacency with the neighbor was established. |


> [!IMPORTANT]
> We must specfiy the routing-instance (VRF) in the CLI command, otherwise the command is executed only on the default routing instance and will return an `OSPF instance is not running` message if no OSPF is enabled on that instance.

## Content

### Configlets
```
configlets
└── ospf-configlet.json
```

### Property Sets
- No Property Sets used in this example.

### Telemetry Service Schema 
```
telemetry-service-definitions
└── ospf-neighbor-OSPF_Neighbor.json
```
![OSPF-Neighbor_Probe_Source_Processor](Images/OSPF-Neighbor_Service_Schema.png)

### Telemetry Collectors
```
telemetry-collectors
└── ospf-neighbor-OSPF_Neighbor.json
```
![OSPF-Neighbor_Collector](Images/OSPF-Neighbor_Collector.png)

- Pay attention to the expression used in the `Value` and the logic to convert the text string provided by the `/ospf-neighbor-information/ospf-neighbor/ospf-neighbor-state` XML path into an integer value which will then be converted back to an enum using the "Value map" processor property of the `Extensible_Service_Data_Collector_Processor` (See probe's configuration).

```python
0 if Neighbor_State == "Attempt" 
else 2 if Neighbor_State == "Down" 
else 3 if Neighbor_State == "Exchange" 
else 4 if Neighbor_State == "ExStart" 
else 5 if Neighbor_State == "Init" 
else 6 if Neighbor_State == "Loading" 
else 7 if Neighbor_State == "2Way" 
else 1 if Neighbor_State == "Full" 
else None
```

### Probes
```
probes
└── ospf-neighbour-check.json
```
- Source Processor configuration:

![OSPF-Neighbor_Probe_Source_Processor](Images/OSPF-Neighbor_Probe_Source_Processor.png)

- IBA Probe pipeline representaiton:

![OSPF-Neighbor_Probe_Pipeline_Vertical](Images/OSPF-Neighbor_Probe_Pipeline_Vertical.png)

- Below a view from the first output stage:

![OSPF-Neighbor_Probe_Stage_1](Images/OSPF-Neighbor_Probe_Stage_1.png)

- Below a view from the second output stage:

![OSPF-Neighbor_Probe_Stage_2](Images/OSPF-Neighbor_Probe_Stage_2.png)

- Below a view from the third output stage:

![OSPF-Neighbor_Probe_Stage_3](Images/OSPF-Neighbor_Probe_Stage_3.png)



### Widgets
```
widgets
├── ospf-neighbor-count-per-border-leaf.json
└── ospf-neighbor-state.json
```

- Configuration of the first widget: 

![OSPF-Neighbor_Probe_Stage_Widget1](Images/OSPF-Neighbor_Probe_Stage_Widget1.png)

- Configuration of the second widget:
  
![OSPF-Neighbor_Probe_Stage_Widget2](Images/OSPF-Neighbor_Probe_Stage_Widget2.png)


### Dashboards
```
dashboards
└── ospf-adjacencies-on-border-leafs.json
```

![OSPF-Neighbor_Dashboard](Images/OSPF-Neighbor_Dashboard.png)