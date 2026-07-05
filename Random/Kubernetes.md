Kubernetes architecture is primarily divided into two types of components:

- `The Control Plane` (master node), which is responsible for controlling the Kubernetes cluster
- `The Worker Nodes` (minions), where the containerized applications are run

![](../Attachements/Pasted%20image%2020260620215302.png)

The master node hosts the Kubernetes `Control Plane`, which manages and coordinates all activities within the cluster and it also ensures that the cluster's desired state is maintained. On the other hand, the `Minions` execute the actual applications and they receive instructions from the Control Plane and ensure the desired state is achieved.

![](../Attachements/Pasted%20image%2020260620215340.png)
Within a containerized environment, the `Minions` (worker nodes) serve as the designated location for running applications. It's important to note that each node is managed and regulated by the Control Plane, which helps ensure that all processes running within the containers operate smoothly and efficiently.

The `Scheduler`, based on the `API server`, understands the state of the cluster and schedules new pods on the nodes accordingly. After deciding which node a pod should run on, the API server updates the `etcd`.

Understanding how these components interact is essential for grasping the functioning of Kubernetes. The API server is the entry point for all the administrative commands, either from users via kubectl or from the controllers. This server communicates with etcd to fetch or update the cluster state.

#### K8's Security Measures

Kubernetes security can be divided into several domains:

- Cluster infrastructure security
- Cluster configuration security
- Application security
- Data security

Each domain includes multiple layers and elements that must be secured and managed appropriately by the developers and administrators.

