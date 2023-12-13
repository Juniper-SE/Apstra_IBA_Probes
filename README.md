# Custom IBA Probes

To do (WIP Mehdi):
- Examples to add:
  - Interface queue 
  - Interface flap
  - BFD telemetry (less important, since already documented)
- Add an XML sample output of each one of the commands, save them in XML format


## Goals of this repository
- Learn thourgh practical examples how to create a custom IBA probe, from the definition of a Custom Telemetry Collector to using it in a Custom IBA probe.
- The examples in this repository are provided for educational purposes and are expected to be tested and customised to your specific needs before deploying them in your production blueprints.

### Importing the examples into a runing Apstra instance
- This can be through API. You can also use the Apstra-cli `content import` command:
  - Git clone this repository.
  - Copy the `content` folder of the example your are an interested in into a folder you can mount as a volume when launching the Apstra-cli utililty (point to the documentaiton) 
  - From the Apstra-cli prompt execute `content import` command by pasing the folder path through the `--folder` argument.
- Be aware that until Apstra `4.2.1` IBA Widgets and Dashboards are keyed with the Blueprint ID. This will be enhanced in 5.0.0, but until then, this part of the `content` folder cannot be imported in a blueprint as is, you should first provide the ID of your blueprint in the JSON file.

### Contributing with additional examples
- Git clone the repo, and create a branch to add an example for an IBA probe. This repo is configured such that the `main` branch is a protected branch, so no commits can be made directly to this branch, but rather through branch merging.
- Use the below command to create the structure for your additional example.
```
mkdir -p IBA_Probe_Example/release_4.2.1/{Images,CLI_Command,Content/{configlets,property-sets,telemetry-service-definitions,telemetry-collectors,probes,widgets,dashboards}} && touch IBA_Probe_Example/README.md && touch IBA_Probe_Example/CLI_Command/README.md && touch IBA_Probe_Example/CLI_Command/xml_command_output.xml
```
It is important to follow this structure to streamline collaboraiton and testing. This will generate the following hierarchy:
```
├── IBA_Probe_Example
│   └── release_X.Y.Z
│       ├── CLI_Command
│       │   ├── README.md
│       │   └── xml_command_output.xml
│       ├── Content
│       │   ├── configlets
│       │   ├── dashboards
│       │   ├── probes
│       │   ├── property-sets
│       │   ├── telemetry-collectors
│       │   ├── telemetry-service-definitions
│       │   └── widgets
│       └── Images
```



## High-Level Architecture of IBA
Explain the notion of Probe, Collector, Grpah Query ..
### Key elements of Custom Telemetry Collectors
  - High-level pointers to Custom Collectors such as the notion of OS Variant etc ... 
(Pick slides from the Tech-Fest)






```
mkdir IBA_Probe_Example
cd IBA_Probe_Example
mkdir release_4.2.1
cd release_4.2.1
mkdir Images
mkdir Content
cd Content
mkdir configlets
mkdir property-sets
mkdir telemetry-service-definitions
mkdir telemetry-collectors
mkdir probes
mkdir widgets
mkdir dashboards
```
