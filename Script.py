import sys
import dns.resolver

def find_subdomains(domain):
    subdomains = []

    # Use the dns.resolver.query function to find subdomains
    try:
        answers = dns.resolver.query(domain, 'NS')
        for rdata in answers:
            subdomains.append(rdata.target.to_text())
    except Exception as e:
        print("Error:", e)
        return []

    return subdomains

# Example usage
domain = input ("enter the address")
subdomains = find_subdomains(domain)
print(f"Subdomains of {domain}: {subdomains}")
