import mlab
from models.river import River
mlab.connect()

river_inafr = []
for river in River.objects(continent = "Africa" ):
    river_inafr.append(river.name)

print("All river in Africa continent:")
print(*river_inafr, sep = ', ')


river_ame = []

for river in River.objects(continent = "S. America", length__lt = 1000):
    river_ame.append(river.name)


print("All river in S.America continent and less than 1000:")
print(*river_ame, sep = ', ')
