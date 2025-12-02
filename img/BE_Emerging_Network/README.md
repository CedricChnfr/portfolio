# TP1: Introduction to SDN/Openflow Networks

## Objectives:
Illustrate the operating principles of a network compliant with the SDN/Openflow paradigm.

## 1. Lab Organization
The final network to be deployed will consist of 4 Pica 8 Openflow-compatible switches and an Openflow Ryu controller. Through a series of small manipulations, the goal is to understand the operation of an SDN/Openflow network. This first lab is organized as follows:
1. Setting up an instance of an OVS (Open vSwitch) bridge and illustrating the default operation of an Openflow switch;
2. Illustrating the manual installation of Openflow rules in Openflow switches;
3. Illustrating different modes ("in-band" and "out-band") of attaching the controller to Openflow switches;
4. Illustrating the operation of simple control applications for network programming in reactive and proactive modes.

## 2. Lab Setup at the Beginning
The equipment provided is as follows:
- 4 Pica 8 Openflow-compatible switches equipped with 48 Gigabit Ethernet ports;
- Ethernet cables (unshielded twisted pairs with RJ45 connectors) crossed and uncrossed;
- 12 PCs in the GEI-101 room equipped with multiple Ethernet cards acting as routers and/or Linux machines.

No configuration is set up on the PCs and routers. All equipment is physically disconnected.

## 3. Questions

### 3.1 Default Operation of an Openflow Switch
The objective of this first manipulation is to allow each group to create an instance of an OVS switch, associate it with the physical ports of the switch to which their terminal machines are connected, and illustrate the default operation of an OVS bridge instance.

#### Steps Performed:

1. Connect the different machines in each row to a Pica 8 switch as shown in Figure 3.1.
2. Via the switch console interface, reboot the switch by running the script:
    ```
    sudo picos_boot
    ```
    Choose the option "2 - picOS: Open vSwitch/Openflow" and set the management interface (eth0) address of the switch and its default gateway to 192.168.1.10i/24 (i: 1::3) and 192.168.1.254/24.
3. Restart the OVS processes by typing:
    ```
    sudo service picos restart
    ```
    Verify that the `ovsdb-server` and `ovs-vswitchd` processes are present by running:
    ```
    ps -A
    ```
    The OVS switch is operational.

#### Creating an Instance of a Logical Bridge and Attaching Physical Ports:

1. Create an OVS instance named `br0`:
    ```
    admin@picOS-OVS$ ovs-vsctl add-br br0 -- set bridge br0 datapath_type=pica8
    ```
2. Attach the physical ports of the switch to the newly created bridge:
    ```
    admin@picOS-OVS$ ovs-vsctl add-port br0 ge-1/1/10 -- set interface ge-1/1/10 type=pica8
    admin@picOS-OVS$ ovs-vsctl add-port br0 ge-1/1/13 -- set interface ge-1/1/13 type=pica8
    admin@picOS-OVS$ ovs-vsctl add-port br0 ge-1/1/16 -- set interface ge-1/1/16 type=pica8
    ```
3. Verify the configuration:
    ```
    admin@picOS-OVS$ ovs-vsctl show
    admin@picOS-OVS$ ovs-ofctl show br0
    admin@picOS-OVS$ ovs-ofctl dump-ports br0
    ```
4. Verify IP connectivity between the different machines in your row. Check the entries in the flow table:
    ```
    admin@picOS-OVS$ ovs-ofctl dump-flows br0
    ```
    If the rule is absent, add it:
    ```
    admin@picOS-OVS$ ovs-ofctl add-flow br0 ,action=normal
    ```

### 3.2 Manual Installation of Openflow Rules in Openflow Switches
The objective of this second manipulation is to illustrate the manual installation of Openflow rules.

#### Steps Performed:

1. Remove the default Openflow rule:
    ```
    admin@picOS-OVS$ ovs-ofctl del-flows br0
    ```
2. Install the necessary Openflow rules to establish IP connectivity between the two end machines in the same row. You can base it on the following command (which directs all traffic arriving on input port 1 to output port 2):
    ```
    admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=1,actions=output:2
    ```

3. Given that I connected my 3 machines to the following ports 10, 13, 16 with the created address (ifconfig eth0 128.0.0.{3,4,5}/24), the commands used are:
```
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,actions=output:13,16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,actions=output:10,16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,actions=output:10,13
```

The granularity level of the previous rule is too broad to allow precise control of network behavior. We will use a rule capable of filtering on source IP addresses to allow only traffic from specific machines. Remove the previous Openflow rule and install the new rules that ensure IP connectivity between the end machines according to the following model:
```
admin@picOS-OVS$ ovs-ofctl del-flows br0
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=<input port>,arp,actions=output:<output port>
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=<input port>,ip,nw_dst=<destination IP>,actions=output:<output port>
```
Given that I connected my 3 machines to the following ports 10, 13, 16 with IP addresses 128.0.0.{3,4,5}/24, the commands used are:
``` bash
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,arp,actions=output:13,16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,ip,nw_dst=128.0.0.4,actions=output:13
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,ip,nw_dst=128.0.0.5,actions=output:16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,arp,actions=output:10,16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,ip,nw_dst=128.0.0.3,actions=output:10
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,ip,nw_dst=128.0.0.5,actions=output:16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,arp,actions=output:10,13
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,ip,nw_dst=128.0.0.3,actions=output:10
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,ip,nw_dst=128.0.0.4,actions=output:13
```

4. Referring to Figure 3.2 involving two devices D1, D2, and a Gateway GW represented by the 3 machines in the same row, identify and install the necessary Openflow rules to:

We chose port 16 for the Gateway (GW), port 10 for device 1 (D1), and port 13 for device 2 (D2).

- Allow UDP traffic between the GW and each device with a port number used at the Device level equal to 5683 (default used by a CoAP server):
    ```bash
    admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,udp,tp_dst=5683,actions=output:10,13
    admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,udp,tp_dst=5683,actions=output:16
    admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,udp,tp_dst=5683,actions=output:16
    ```

- Establish an SSH session from the GW to each device:
    ```bash
    admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,tcp,tp_dst=22,actions=output:10,13
    admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,tcp,tp_dst=22,actions=output:16
    admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,tcp,tp_dst=22,actions=output:16
    admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,tcp,tp_src=22,actions=output:10,13
    admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,tcp,tp_src=22,actions=output:16
    admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,tcp,tp_src=22,actions=output:16
    ```

Don't forget to add ARP rules to allow address resolution:
```bash
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,arp,actions=output:10,16
```

    ```bash
    admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,tcp,tp_src=22,actions=output:16
    admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,tcp,tp_dst=22,actions=output:13
    ```

To connect via SSH, first set the password for the root user on each machine using the `passwd` command:

    ```bash
    root@device$ passwd
    ```

    Then, from the Gateway, you can establish an SSH connection to each device using the corresponding IP address:

    ```bash
    root@gateway$ ssh root@128.0.0.3
    root@gateway$ ssh root@128.0.0.4
    ```

### Note on Telnet and FTP

**Telnet**: Telnet is a network protocol used to provide bidirectional interactive communication via a virtual terminal connection. It allows users to connect to remote computers and execute commands as if they were physically present in front of the machine. However, Telnet is not secure because it transmits data in plain text, including passwords.

**FTP (File Transfer Protocol)**: FTP is a standard protocol used to transfer files between a client and a server on a computer network. It allows downloading and uploading files, creating and deleting directories, and managing file permissions. Like Telnet, FTP is not secure by default because it transmits data in plain text, but secure variants like FTPS and SFTP exist to encrypt communications.

### 3.3 Attaching an Openflow RYU Controller

We will consider an "out-of-band" control, in other words, the Openflow traffic between the controller and the Openflow switches is transported by a different network than the one used for user data transport. To do this, we will connect the controllers to the management network used to configure the switches with SSH sessions. To do this:

1. First, if not already done, connect an interface of the machine acting as the controller to the management network by assigning it an appropriate IP address:
```bash
ifconfig eth1 192.168.0.42
```

2. For each created bridge, declare the controller to which it is associated using the following command:
```bash
admin@picOS-OVS$ ovs-vsctl set-controller br0 tcp:192.168.0.42:6633
```
6633 being the default port number on which the RYU controller listens.

3. Start the RYU controller in verbose mode:
```bash
controller# ryu-manager --verbose
```

4. Check the connection status with the controller, the exchanges between the controller and the switch, and the content of the flow table using the following commands:
```bash
admin@picOS-OVS$ ovs-vsctl show
admin@picOS-OVS$ ovs-ofctl snoop br0
admin@picOS-OVS$ ovs-ofctl dump-flows br0
```

5. For now, no network control application has been launched on the controller. By testing IP connectivity between the nodes in your row, verify on the controller console that events related to packet arrivals are reported to the controller without it proposing any treatment.

Here are the commands I did at the beginning:
```bash
ifconfig eth1 192.168.0.42
admin@picOS-OVS$ ovs-vsctl set-controller br0 tcp:192.169.1.101:6633
```
Then, I pinged the controller at address 192.169.1.101.

### 3.4 Study of a Network Control Application

The RYU distribution provides a set of simple applications to illustrate the development of network control applications. The `simple_switch` application aims to make the switches controlled by the controller behave like classic layer 2 switches (with auto-learning for node localization and flooding on all interfaces when the recipient is unknown). Thus, the `simple_switch` application processes each "packet-in" packet reported to the controller by a bridge following the arrival of a packet whose recipient is unknown, by asking the bridge to relay the corresponding packets on all its other output ports. When the recipient transmits a frame in response (including its MAC address), the application adds an entry in the flow table that directs the packet flow from the initial input port to the output port from which the recipient can be reached.

1. Start the `simple_switch_14` application using the following command:
    ```bash
    controller# ryu-manager --verbose simple_switch_14.py
    ```

2. Start a ping between two terminal machines in the row and check the entries added to the flow table:
    ```bash
    admin@picOS-OVS$ ovs-ofctl dump-flows br0
    ```

3. Study the source code of `simple_switch_14.py` to understand the application's behavior.

### 3.5 Final Exercise

Figure 3.5 represents the topology to be deployed by each row using the 4 available Pica8 switches. Each row will instantiate a bridge with an interface to a machine in the row and will be connected to two other bridges deployed on two other Pica8 switches according to a partially full mesh topology. The bridges in each row will be associated with the same controller specific to each row. The controller can be launched on one of the terminal machines.

1. First, do not physically connect the dotted link to avoid creating a physical loop.
2. Start the `simple_switch_14` application and check IP connectivity between the terminal machines.
3. Observe the Openflow rules installed by the controller.
4. Connect the last link, restart the `simple_switch_14` application, and then check connectivity between terminal machines. What do you observe? What solution do you propose? Check the list of available applications in the controller's installation directory and identify an application that could solve the problem.
