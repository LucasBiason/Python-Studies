import paramiko

IP = "172.31.38.36"
KEY = "./testespython521.pem"
key = paramiko.RSAKey.from_private_key_file(KEY)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname = IP,
    username = 'ubuntu',
    pkey = key
)

commands = [
    'sudo apt-get update -y',
    'sudo apt-get install -y python3-pip',
    'git clone git@gitlab.com:LucasBiason/pythonstudies.git',
    'cd pythonstudies/python521/',
    'pip3 install -r requirements.txt',
    'sudo python3 app.py &'
]

for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode(), stderr.read().decode())

