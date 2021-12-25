# <img src="https://img.icons8.com/external-wanicon-lineal-color-wanicon/64/000000/external-machine-big-data-wanicon-lineal-color-wanicon.png"/> MACHINE: Kevin Local - Kevin Proof
- IP Address: 192.168.19.151 <br>
- Hint: ✍
  - 
  - 

## Write-up - Kevin Local:

- Scan các port bằng **nmap**, đây là payload nmap mình thường dùng nhất  `nmap -Pn -sV -sC -p- -A -T4 -vv 192.168.19.151 `
Ta có các port sau: 

```
22/tcp   open  ssh      syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     syn-ack nginx 1.18.0 (Ubuntu)
443/tcp  open  ssl/http syn-ack nginx 1.18.0 (Ubuntu)
8080/tcp open  http     syn-ack Apache Tomcat
```



## Leo thang đặc quyền - Kevin Proof:



### Flag:
- Local.txt: 
- Proof.txt: 












