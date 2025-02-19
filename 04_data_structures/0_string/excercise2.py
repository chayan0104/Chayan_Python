
input_data=["/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
"/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
"/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv"
]  

ip_addresses = []

for path in input_data:
    segments = path.split("/")
    if "server" in segments:
        ip = segments[segments.index("server") + 1]  
        ip_addresses.append(ip)

# Print the extracted IP addresses
print(ip_addresses)