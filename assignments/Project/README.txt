Application URL: http://block647068-f9b.blueboxgrid.com:6543

Github URL: https://github.com/yenlinsu/training.python_web/tree/master/assignments/Project


Project Description: Network Deployment Automation System

Front End:
- Automation Process initiation:
  - Form: input site specific information (location, network, etc) - complete
  - Submitted data validation - complete
  - store submitted data into ZODB - not complete yet
- Query site specific data stored in ZODB:
  - Form: input site selection - complete
  - Submitted data validation - complete
  - Display the contents of the objects in a nicely formatted table, based on different query set - not complete yet
- user login/out (not complete yet)

Backend: (out of scope for this project due to the time required to develop this portion)
- IP subnetting (user input an IP supernet and the system generate a list of subnets based on a pre-defined IP subnetting scheme) - not complete yet
    - based on the subnetting result, create a set of objects needed for generating the network device configs
    - take those objects and generate the configs, save them to txt files

Extras down the road: (out of scope for this project)
- learn APIs of other network management system so my deployment system can automate populating data into those network management systems

Note: the "not complete yet" part will be the focus of the spring term class project.



Instructions on how to run my project locally on your laptop:
- packages needed: pyramid_zodbconn, pyramid_tm, deform
