# Ping Mesh

## Description

![Ping-Mesh_Dashboard_External-to-Fabric](images/Ping-Mesh_Dashboard_External-to-Fabric.png)

![Ping-Mesh_Dashboard_Intra-Fabric](images/Ping-Mesh_Dashboard_Intra-Fabric.png)

- Using a Configlet to enable Junos RPM probes funtionality, executing continuous PINGs to verify end-to-end reachability both intra-fabric (Underlay and Overlay) and external to the fabric (facing the External routers).
- Definition of three Telemetry services, each one collecting the results of a specific RPM probe: `Underlay_Reachbility`, `Overlay_Reachability` and `External_Reachability`.
- Creation of an IBA probe running those three services. Sepecific Graph Queries used in the source processor in order to match the services significant keys as well as defining additionnal keys to enrich the probe output with Graph context. Adding analytics processors (`Range`) to the probe to raise anomalies when measurements exceeds a defined threshold (expressed in seconds).
-  Different Widgets extracting different stages views from the IBA Probe. Widgets are grouped in Dashboards for easier consumption by the operator. 

### Content

### Configlets

```
├── configlets
    └── rpm-ping.json
```
![Ping-Mesh_Configlet_Underlay-Reachability](images/Ping-Mesh_Configlet_Underlay-Reachability.png)

![Ping-Mesh_Configlet_Overlay-Reachability](images/Ping-Mesh_Configlet_Overlay-Reachability.png)

![Ping-Mesh_Configlet_External-Reachability](images/Ping-Mesh_Configlet_External-Reachability.png)

### Property Sets

```
├── property-sets
    └── rpm-ping-ps.json
```

![Ping-Mesh_Property-Sets](images/Ping-Mesh_Property-Sets.png)

### Telemetry Service Definitions 
```
├── telemetry-service-definitions
    ├── rpm-icmp-external-RPM_ICMP_External.json
    ├── rpm-icmp-overlay-RPM_ICMP_Overlay.json
    └── rpm-icmp-underlay-RPM_ICMP_Underlay.json
```

![Ping-Mesh_Schema_Underlay-Reachability](images/Ping-Mesh_Schema_Underlay-Reachability.png)

![Ping-Mesh_Schema_Overlay-Reachability](images/Ping-Mesh_Schema_Overlay-Reachability.png)

![Ping-Mesh_Schema_External-Reachability](images/Ping-Mesh_Schema_External-Reachability.png)

### Telemetry Collectors
```
├── telemetry-collectors
    ├── rpm_icmp_external.json
    ├── rpm_icmp_overlay.json
    └── rpm_icmp_underlay.json
```

![Ping-Mesh_Configlet_Underlay-Reachability](images/Ping-Mesh_Configlet_Underlay-Reachability.png)

![Ping-Mesh_Configlet_Overlay-Reachability](images/Ping-Mesh_Configlet_Overlay-Reachability.png)

![Ping-Mesh_Configlet_External-Reachability](images/Ping-Mesh_Configlet_External-Reachability.png)

### Probes
```
├── probes
│   └── ping-mesh.json
```

![Ping-Mesh_Probe](images/Ping-Mesh_Probe.png)

### Widgets
```
└── widgets
    ├── external-rtt-last-1h.json
    ├── leaf-to-ext-rtr.json
    ├── leaf-to-leaf-overlay.json
    ├── leaf-to-leaf-underlay.json
    ├── overlay-rtt-last-1h.json
    └── underlay-rtt-last-1h.json
```

![Ping-Mesh_Widget](images/Ping-Mesh_Widget.png)

### Dashboards

```
├── dashboards
    ├── ping-mesh-external-to-fabric.json
    └── ping-mesh-intra-fabric.json
```

![Ping-Mesh_Dashboard_External-to-Fabric](images/Ping-Mesh_Dashboard_External-to-Fabric.png)

![Ping-Mesh_Dashboard_Intra-Fabric](images/Ping-Mesh_Dashboard_Intra-Fabric.png)