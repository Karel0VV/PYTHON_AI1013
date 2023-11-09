class BuildingError(Exception):
    def __str__(self):
        return "Занадто мало матеріалів для того щоб побудувати будинок"
def check_material(amouth_of_material, limit_value):
    if amouth_of_material > limit_value:
        return "матеріалів недостатньо"
    else:
        raise BuildingError(amouth_of_material)
matterial = 100
print(check_material(matterial, limit_value=300))