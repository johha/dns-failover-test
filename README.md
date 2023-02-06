# DNS Failover Test

This is a docker compose setup to simulate and test a DNS failover.


## Test DNS Failover
### Start Containers
``` bash
$ docker compose up
```

### DNS Failover
```bash
$ curl --connect-timeout 10 local.bbs:5000/v1/ping -v
```