import dns.resolver

answer = dns.resolver.resolve('trybeans.com', 'TXT', search=True)
records = [str(record) for record in answer]

is_valid = False
for record in records:
    if record.startswith('v:spf') and 'include:sendgrid.net' in record:
        is_valid = True
        break
