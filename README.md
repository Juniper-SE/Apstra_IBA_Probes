# Custom IBA Probes in Apstra

To do (WIP Mehdi):

- Interface flap
    - Grab it from Boris Env.

- Interface Queue.
    - Find a device with running traffic to execute the command on, get the output and document it. 
    - Design the probe. 

- OPSF Neighbor Check
  - Enhance the configlet, leverage Device-Context and add a Property-set

- Examples to add:
  - BFD telemetry (less important, since already documented)
  - RoCEv2

- Structure of the repo:
  - Clean the content of some json files to focus only on the required elements.

- Add a nice picture in the front Readme (identity of the repo)

---

## Goals of this repository
- Learn thourgh practical examples how to create a custom IBA probe, from the definition of a Custom Telemetry Collector to using it in a Custom IBA probe.
- The examples in this repository are provided for educational purposes and are expected to be tested and customised to your specific needs before deploying them in your production blueprints.

---

## Content of this repository
- [Ping Mesh](Ping_Mesh/release_4.2.1/README.md) 
- [Device Uptime](Device_Uptime/release_4.2.1/README.md) 
- [OSPF Neighbor](OSPF_Neighbor/release_4.2.1/README.md)
- [Interface_Queue](Interface_Queue/release_4.2.1/README.md)
- [Interface_Flap](Interface_Flap/release_4.2.1/README.md)

---

## How to use this repository?
- Git clone the repository: `git clone git@github.com:mab27/Apstra_IBA_Probes.git`.
- Import the different JSON files inthe `content` folder of any given example into your running Apstra instance. You can do that via import buttons in the UI for most items, except the `telemetry-collectors`, or you can use the REST APIs to automating pushing those files. 
> [!IMPORTANT]
>  A sequence is to be follosed to ensure the files are correctly accepted by the receiving Apstra instance: (1) **Configlets** --> (2) **Property-Sets** --> (3)**telemetry-service-definitions** --> (4) **telemetry-collectors** --> (5) **probes** --> (6) **widgets** --> and (7) **dashboards**.
> To make this process easiser you can use the Apstra-Cli utility, a wrappwer around Aprstra's API that delivers safe workflows including taking care of the right sequence during import of JSON payloads.
- Copy the content of `content` folder for the example your are an interested to a location that you mount as a volume of your Apstra-cli utililty. See Apstra-CLI [documentaiton](https://www.juniper.net/documentation/us/en/software/apstra4.2/apstra-user-guide/topics/topic-map/apstra-cli.html) for more details on how ot use docker volume mount.
- From the Apstra-cli prompt execute `content import` command by pasing the folder path through the `--folder` argument.
![Apstra-cli_Content_Import](_Images/Apstra-cli_Content_Import.png)
> [!IMPORTANT]
> Until 4.2.1 included, IBA Widgets and Dashboards JSON definitions must respectively include the Probe_ID and the Blueprint_ID (This will change in `5.0.0` to have a more loosely coupled design). Therefore, when importing the content into any `4.2.1` instance you must prior to that edit the JSON files for `/widgets` and `dashboards` to include your Probe ID and Dashboard ID, otherwise this part of the `content import` will fail. 

---

## How to contribute to this repository?
- Git clone the repository: `git clone git@github.com:mab27/Apstra_IBA_Probes.git`
- Move to the repository `cd Apstra_IBA_Probes` and create a new branch: `git checkout -b <Your-Branch-Name>`.
> [!TIP]
> Name the branch after the change you are planning to do to facilitate its identification locally, when you work on it, and remotely when you later pusch it for collaboration and review. For example if you are creating a new probe, your branch name could be something like "Monitor metric foo on external links". If you are adding another release variant to existing probe because you want to benefit from the new feature enhancements, your branch name could be "release_5.0.0 for Ping Mesh".
- Create the folder structure for your new Probe: `mkdir -p IBA_Probe_Example/release_X.Y.Z/{Content/{configlets,property-sets,telemetry-service-definitions,telemetry-collectors,probes,widgets,dashboards},Images} && touch IBA_Probe_Example/README.md`. It is important to follow this structure to streamline collaboraiton and testing. 
  - This will generate the following hierarchy:
```
├── IBA_Probe_Example
│   └── release_X.Y.Z
│       ├── Content
│       │   ├── configlets
│       │   ├── dashboards
│       │   ├── probes
│       │   ├── property-sets
│       │   ├── telemetry-collectors
│       │   ├── telemetry-service-definitions
│       │   └── widgets
│       ├── Images
│       └── README.md
```
- Start filling that newly created folder structure by populating every relevant section. This includes clear description of the use-case docoumented in the README files, copies of all the relvant JSON payloads extracted from your environement (You can use UI export buttons, API calls or apstra-cli `content export` command), any useful screen capture image, etc ... Check existing content for inspiration and follow the same strucutre.
![Apstra-cli_Content_Export](_Images/Apstra-cli_Content_Export.png) 
- Stage your chnages as you progress: `git add <filename>` or `git add .` and commit them once you have a satisfacotry version: `git commit -m "<provide-commmit-message>"`.
- Push your branch to origin `git push --set-upstream origin <Your-Branch-Name>`
> [!IMPORTANT]
> Note that this repositorty `main` branch is set as a protected branch. Hence contributions cannot be ade directly against this branch but rather through merging of feature branches after peer reviews. This allows to scale the collaboraiton on this repository.
- Request a Pull Request and Merge Request.

---

## High-Level Architecture of IBA
Explain the notion of Probe, Collector, Grpah Query ..

### Key elements of Custom Telemetry Collectors
  - High-level pointers to Custom Collectors such as the notion of OS Variant etc ... 
(Pick slides from the Tech-Fest)