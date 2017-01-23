# multivac-AP
simple python app

based on https://github.com/Unbabel/devops-coding-challenge

### Planning


Before starting building the stack, it is necessary to desing 1 or 2 possible scenarios in terms of infrastructure architecture for a live system:
one solution can be as follow
- An ELB load balancer rotating requests in a round robin fashion way
- 2 AWS EC2 instances on a Public Network with a webserver (i.e. NGINX) configured in two different availability zones within the same region
- 2 or more EC2 application instances in a private network configured within an AutoScaling group (i.e. between 2 and 3) with policies to start/stop instances based on CloundWatch metrics
- a DB tier including both MongoDB and Redis

* Security
there are several points to consider in order to make the whole stack reasonably secure:
** network security

* Scalability
* Logging
* Monitoring
* Automation
