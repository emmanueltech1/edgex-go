# EIS Message Bus (PUB/SUB) Reference Example 

These example assumes that one has successfully installed and configered the EIS Message Bus libraries for python bindings.

## Get Started
 - Open a terminal and run the following command for the publisher:
```sh
python3 ./mypublisher.py ../../examples/configs/tcp_publisher_no_security.json
```
 - Open another terminal and run the following command for the subscriber:
```sh
python3 ./mysubscriber.py ../../examples/configs/tcp_subscriber_no_security.json 
```
One should now see the IQ data being recieved from the EIS Message Bus Publisher.

This reference example can be used to extend to any particular use case for further development.