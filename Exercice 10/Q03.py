import subprocess as sp

result = sp.run('dir', shell=True, capture_output=True)

print(result.stdout)

# extraire adresse ip du message depuis popen
process = sp.Popen('ping google.com', shell=True, stdout=sp.PIPE, stderr=sp.PIPE, text=True, encoding='oem')
process.wait()


for ligne in process.stdout:
    for mot in ligne.split():
        if mot.count(".") == 3:
            ip = mot.strip("ÿ:;,")
            print(ip)
