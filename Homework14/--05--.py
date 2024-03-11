key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}

legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

legendary_obtained = False

while not legendary_obtained:
    items = input().lower().split()
    for i in range(0, len(items), 2):
        quantity = int(items[i])
        material = items[i+1]

        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                legendary_obtained = True
                print(f"{legendary_items[material]} obtained!")
                key_materials[material] -= 250
                break
        else:
            if material not in junk_items:
                junk_items[material] = 0
            junk_items[material] += quantity

for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")

for material, quantity in junk_items.items():
    print(f"{material}: {quantity}")
