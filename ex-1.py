result = []

with open('nginx_logs.txt', 'r') as f:
    for line in f:
        remote_addr = line.partition(' - - ')[0]
        request_type = (line.partition('] "')[2]).partition(' /')[0]
        requested_resource = (line.partition('GET ')[2]).partition(' HTTP')[0]
        res = (remote_addr, request_type, requested_resource)
        result.append(res)
    print(result)
