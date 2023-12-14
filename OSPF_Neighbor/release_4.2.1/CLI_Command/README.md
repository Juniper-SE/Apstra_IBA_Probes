- CLI Command: `show ospf neighbor instance OVERLAY extensive` - [Junos documentation page](https://www.juniper.net/documentation/us/en/software/junos/ospf/topics/ref/command/show-ospf-ospf3-neighbor.html). 
- Sample Output:
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
- Fields of interest:
| Field | Information |
| --- | --- |
| `Address` | OSPF neighbor IP. |
| `Interface` | Interface through which the neighbor is reachable. |
| `Area` | OSPF area that the neighbor is in. |
| `State` | State of the neighbor. Possible values will be the following enum: `Attempt`, `Down`, `Exchange`, `ExStart`, `Full`, `Init`, `Loading` or `2Way` |
| `adjacent` | Length of time since the adjacency with the neighbor was established. |
- Notes:
  - We must specfiy the routing-instance (VRF) in the CLI command, otherwise the command is executed only on the default routing instance and will return an `OSPF instance is not running` message if no OSPF is enabled on that instance.
