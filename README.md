# multivac-AP
simple python app

based on https://github.com/Unbabel/devops-coding-challenge

### Planning


Before starting building the stack, it is necessary to desing 1 or 2 possible scenarios in terms of infrastructure architecture for a live system:
one solution can be as follow
- An ELB load balancer rotating requests in a round robin fashion way
- 2 AWS EC2 instances on a Public Network with a webserver (i.e. NGINX) configured in two different availability zones within the same region
- 2 or more EC2 application instances in a private network configured within an AutoScaling group (i.e. between 2 and 3) with policies to start/stop instances based on CloundWatch metrics
- a DB tier including both MongoDB and Redis in a single instance (for session persistence), plus one or more read-replicas

* Security
there are several points to consider in order to make the whole stack reasonably secure:

** network security
use security groups (and/or network ACL) to allow traffic only on listening ports; for example for the webservers in the DMZ zone it will be 80,443 from anywhere, and 22 for management purposes, maybe restricted to the public IP or network of the company.
On the other end, the application tier security group (or iptables chains) should be configured only to accept and forward requests from the private network interface of the webservers to the application port 5000 in a stateful way (default for security groups)

** infrastructure security

Each single instance should be regularly patched to avoid common exploits and vulnerabilities. Patches and updates should be applied to the CI plugins as well.

** application security

Some sort of authentication can be applied to the Flask's endpoints as well, at least to the POST and DELETE ones (i.e. http basic auth) even if the data is sent in clear text, the encryption can/should be managed elsewhere, like on the NGINX servers enabling SSL certs.
Plus the app servers should be tested against any possible common SQL injection and XSS techniques.

* Scalability

Given the architecture described above, the most obvious way to scale such architecture horizontally would be done via AutoScaling Groups and Launch Configuration.
Anyway, since the application is deployed inside a Docker container - which could be used even in a production environment - another way to scale can be managed using orchestration tools like Kubernetes, Docker Swarm, Apache Mesos (+Marathon) or furthermore AWS services such ECS. Describing in details which one to use is beyond the scope of this test. Another solution could be using a combination of the above; i.e. a Kubernetes cluster (which in my opinion is the best solution) with Docker images deployed under ECR (container registry service in AWS) to make the image available from anywhere using only their Amazion Resource Name.

* Logging

The application that run inside the container is configured to log on two different files on the host machine (under /var/log/app/ directory), one for the server, the other one for the worker. Further improvement can be configuring a logstash pipeline file to get these files as input, apply common filters/plugin to them and send the output to a kibana dashboard for graphs and statistics.

* Monitoring

The most common and easy way would be to install elsewhere within the same subnet a Nagios/Zabbix/Icinga2 or any other SNMP based monitoring server to launch usual checks on services and health on the instances. But since we are describing an application stack deployed under AWS, even better would be to use CloudWatch and ELB heartbeat on the load balancer.

* Automation

a pretty basic Ansible playbook is already implemented in the solution deployed.
Said that, it can be configured in many different ways to install just piece of software or any other common admin tasks in different machines and different tiers.
For the purpose of the test I just tried to keep it simple/

*** Installation


