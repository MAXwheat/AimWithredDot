import random
import requests
import base64
import binascii
#CONFIG___\\\
obf_payload_path='E:/AWD_Obf/sample.txt'
host_path='E:/AWD_Obf/host.txt'
relurl_path='E:/AWD_Obf/relpath.txt'
datagen_path='E:/AWD_Obf/postdata.txt'
MAX_ITER=25
#CONFIG___///
obf_payload_set=[]
host_set=[]
relurl_set=[]
datagen_set=[]
file = open(obf_payload_path) 
for line in file.readlines():  
    line=line.strip('\n')  
    obf_payload_set.append(line)
file.close()
print("[+] obf_payload: "+str(len(obf_payload_set))+" "+" || ".join(obf_payload_set))
file = open(host_path) 
for line in file.readlines():  
    line=line.strip('\n')  
    host_set.append(line)
file.close()
print("[+] host: "+str(len(host_set))+" "+" || ".join(host_set))
file = open(relurl_path) 
for line in file.readlines():  
    line=line.strip('\n')  
    relurl_set.append(line)
file.close()
print("[+] relative_url: "+str(len(relurl_set))+" "+" || ".join(relurl_set))
file = open(datagen_path) 
for line in file.readlines():  
    line=line.strip('\n')  
    datagen_set.append(line)
file.close()
print("[+] post_datagen: "+str(len(datagen_set))+" "+" || ".join(datagen_set))
print("------------------------")
iters=0
padding=' '
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.115','Content-Type': 'application/x-www-form-urlencoded'}
get_or_post_set=['GET','POST']
encry_set=['NONE','NONE','BASE64','HEX']
while iters<MAX_ITER:
    iters=iters+1
    encry=encry_set[random.randint(0,3)]
    get_or_post=get_or_post_set[random.randint(0,1)]
    random_host=host_set[random.randint(0,len(host_set)-1)]
    random_relurl=relurl_set[random.randint(0,len(relurl_set)-1)]
    random_payload=obf_payload_set[random.randint(0,len(obf_payload_set)-1)]
    random_datagen=datagen_set[random.randint(0,len(datagen_set)-1)]
    if(encry=='BASE64'):
        random_payload=base64.b64encode(random_payload)
    if(encry=='HEX'):
        random_payload=binascii.b2a_hex(random_payload)
    if get_or_post=='GET':
        print("[-] current_process_info: "+str(iters)+"/"+str(MAX_ITER)+" "+" || ".join((get_or_post,random_host,random_relurl,random_payload,encry)))
        url=random_host+random_relurl+padding+random_payload
        try:
            res=requests.get(url=url,timeout=0.1,headers=headers)
            print("[-] current_process_res: "+str(url)+" "+str(res.status_code))
            print("------------------------")
        except:
            print("[-] current_process_res: "+str(url)+" ERROR!!!")
            print("------------------------")
    if get_or_post=='POST':
        print("[-] current_process_info: "+str(iters)+"/"+str(MAX_ITER)+" "+" || ".join((get_or_post,random_host,random_relurl,random_payload,random_datagen,encry)))
        url=random_host+random_relurl
        post_data=random_datagen+padding+random_payload
        try:
            res=requests.post(url=url,timeout=0.1,headers=headers,data=post_data)
            print("[-] current_process_res: "+str(url)+" DATA: "+post_data+" "+str(res.status_code))
            print("------------------------")
        except:
            print("[-] current_process_res: "+str(url)+" ERROR!!!")
            print("------------------------")