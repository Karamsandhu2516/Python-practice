a = [100,200,300,True]
print(type(a))
print(a)

cloud = list()
print(type(cloud))
cloud.append("AWS")
cloud.append("AZURE")
cloud.append("GCP")
print(cloud)

for i in cloud:
    print(i)

# Dictionary

info ={
    "name" : "Karam",
    "Qualification" : "MCA",
    "City": "waterloo",
    "Favorite" : ["reading", "shopping", "travelling"]
    }

print("I live in", info["City"])

info.update({"surname": "sandhu"})
print(info)

