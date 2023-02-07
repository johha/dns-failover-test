# DNS Failover Test

This is a docker compose setup to simulate and test a DNS failover.


## Test DNS Failover
### Start Containers
``` bash
$ docker compose up -d
```

### Setup DNS Forwarding (MacOs)

#### Backup `pf` Config
```bash
sudo cp -p /etc/pf.conf /etc/pf.conf.bak
```

#### Append To Config `/etc/pf.conf `
``` bash
rdr pass inet proto { tcp, udp }  from any to 127.0.0.1 port 53 -> 127.0.0.1 port 8053

```

#### Restart `pf`
```
sudo pfctl -E
```


### Test DNS Failover With `curl`
```bash
$ curl --connect-timeout 10 local.horst:5000/v1/ping -v
```


### Stop Containers
``` bash
$ docker compose down
```