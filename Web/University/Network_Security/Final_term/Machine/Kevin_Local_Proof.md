# <img src="https://img.icons8.com/external-wanicon-lineal-color-wanicon/64/000000/external-machine-big-data-wanicon-lineal-color-wanicon.png"/> MACHINE: Kevin Local - Kevin Proof
- IP Address: 192.168.19.151 <br>
- Hint: ✍
  - DNS
  - Dir Tiết Kiệm, Try harder!

## Write-up - Kevin Local:

- Scan các port bằng **nmap**, đây là payload nmap mình thường dùng nhất  `nmap -Pn -sV -sC -p- -A -T4 -vv 192.168.19.151 `<br>
Ta có các port sau: 

```
42/tcp    open  tcpwrapped    syn-ack
53/tcp    open  domain?       syn-ack
80/tcp    open  http          syn-ack Microsoft IIS httpd 10.0
135/tcp   open  msrpc         syn-ack Microsoft Windows RPC
445/tcp   open  microsoft-ds? syn-ack
3306/tcp  open  mysql?        syn-ack
3389/tcp  open  ms-wbt-server syn-ack Microsoft Terminal Services
5357/tcp  open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
5526/tcp  open  unknown       syn-ack
49670/tcp open  msrpc         syn-ack Microsoft Windows RPC
49671/tcp open  msrpc         syn-ack Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```

Hint là DNS. Vì vậy mình nên tập trung vào port 53 và scan xem thử dịch vụ nó đang chạy là gì : `nmap -sV -p 53 192.168.19.151 `
```
PORT   STATE SERVICE VERSION
53/tcp open  domain  Simple DNS Plus
```
Theo trên, server là một Domain Controller sử dụng dịch vụ **Simple DNS Plus**.

## Leo thang đặc quyền - Kevin Proof:



### Flag:
- Local.txt: 
- Proof.txt: 












