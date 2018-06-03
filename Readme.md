# Auto-SSH for Windows security 


# Example of the working environment
![alt text](https://github.com/mohanad86/autossh-python/blob/master/example.png)

### Scenario
If the security monitoring solution fails, system administrator will use the current script to automate the distribution of the SSH public keys for all the machines in the network and will allow the administrator to SSH -t thoroughly the specific machine accompanied by the root permissions. 
System administrator can use the following commands to ensure the security of the system, 
until the monitoring solution will back in busniess. 



### Administrator need to have the following to be able to run the code in the Windows environment

1- Python version 2.7 (https://www.python.org/download/releases/2.7/)

2- Install openssh server and client

3- Install Nmap this is a direct link to download (https://nmap.org/dist/nmap-7.70-setup.exe)



```sh
$ ssh -t hostname top -U [username]
$ ssh -t hostname  ps -u [username]
$ ssh -t hostname watch w
$ ssh -t hostname watch w [username]
$ ssh -t hostname watch who 
$ ssh -t hostname watch who -a
$ ssh -t hostname watch users
$ ssh -t hostname tail -f /var/log/syslog
$ ssh -t hostname htop
```  

### The code is to automate sending the ssh public ID to many machines, and if user need to access the machines it could be easy, cause the code will add all the required information to .ssh/config. 

### The code will work in Windows 10 platform
 
- Send commands direct to other machines using the command
The following commands
```sh
$ ssh -t machine-name (The command here)
```

# If you're interested to see how it works

* [Auto-SSH video](https://www.youtube.com/watch?v=MxuFB4hLGWc&index=6&list=PLKAuFoXV02VoW3cvZZAcDI1qWvuyM1qrF)



# Interesting about the how the ssh works 

* [First ssh tutorial](https://www.youtube.com/watch?v=xhqY3m8xiwQ&list=PLKAuFoXV02VoW3cvZZAcDI1qWvuyM1qrF)

* [Second ssh tutorial](https://www.youtube.com/watch?v=fiv-hAHUMF8&list=PLKAuFoXV02VoW3cvZZAcDI1qWvuyM1qrF&index=2) 

* [Third ssh mange to other machines from Linux overview](https://www.youtube.com/watch?v=8EmnxIOlsUQ&index=3&list=PLKAuFoXV02VoW3cvZZAcDI1qWvuyM1qrF)

* [Fourth how to add many machine using Python from Linux overview](https://www.youtube.com/watch?v=1mU8resSwwg&list=PLKAuFoXV02VoW3cvZZAcDI1qWvuyM1qrF&index=4)

 

    Author: Mohanad Aly 

License
----
Licensed under the Apache License

http://www.apache.org/licenses/LICENSE-2.0
