print('Hello world');

a = 5;
b = 6;

soma = a + b;
multi = a * b;


print(soma);
print(multi);

print(b > 10);

trybe_course = ["Introdução", "Front-end", "Back-end"];
print(trybe_course);

trybe_course.append("Ciencias da Computação");

trybe_course[0] = "Fundamentos";

print(trybe_course);

info = {
  "personagem": "Margarida",
  "origem": "Pato Donald",
  "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}

info["recorrente"] = "Sim";

print(info);

del info["origem"];

print(info);

alcance = list(range(5))

print(alcance)
