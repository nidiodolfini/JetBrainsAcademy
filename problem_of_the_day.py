Belov = ["Physics", "Math", "Russian"]
Smith = ["Math", "Geometry", "English"]
Sarada = ["Japanese", "Math", "Physics"]

teste = Belov
teste += Smith
teste += Sarada

print(len(sorted(set(teste))))