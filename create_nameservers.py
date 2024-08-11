import requests

def add_dns_record(api_token, zone_id, name, ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    data = {
        "type": "A",
        "name": name,
        "content": ip,
        "ttl": 3600,
        "proxied": False
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Registro A criado com sucesso: {name} -> {ip}")
    else:
        print(f"Falha ao criar o registro A: {response.status_code} - {response.text}")

def main():
    api_token = input("Digite seu token de API do Cloudflare: ")
    zone_id = input("Digite o ID da zona do Cloudflare: ")
    ip = input("Digite o IP da VPS: ")
    domain = input("Digite o domínio (exemplo.com): ")
    
    ns1 = f"dragon.ns.{domain}"
    ns2 = f"mastertech.ns.{domain}"

    add_dns_record(api_token, zone_id, ns1, ip)
    add_dns_record(api_token, zone_id, ns2, ip)

if __name__ == "__main__":
    main()
