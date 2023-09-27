#include <iostream>
#include <string>

class Animal
{
public:
    Animal(std::string nombre, int edad)
    {
        this->nombre = nombre;
        this->edad = edad;
    }
    void sonido()
    {
        std::cout << "Nombre: " << nombre << std::endl;
        std::cout << "Edad: " << edad << std::endl;
    }

private:
    std::string nombre;
    int edad;
};

class Perro : public Animal
{
public:
    Perro(std::string nombre, int edad, std::string sonido_perro) : Animal(nombre, edad)
    {
        this->sonido_perro = sonido_perro;
    }
    void sonido()
    {
        Animal::sonido();
        std::cout << "Sonido que emite: " << sonido_perro << std::endl;
    }

private:
    std::string sonido_perro;
};

class Gato : public Animal
{
public:
    Gato(std::string nombre, int edad, std::string sonido_gato) : Animal(nombre, edad)
    {
        this->sonido_gato = sonido_gato;
    }
    void sonido()
    {
        Animal::sonido();
        std::cout << "Sonido que emite: " << sonido_gato << std::endl;
    }

private:
    std::string sonido_gato;
};

class Pajaro : public Animal
{
public:
    Pajaro(std::string nombre, int edad, std::string sonido_pajaro) : Animal(nombre, edad)
    {
        this->sonido_pajaro = sonido_pajaro;
    }
    void sonido()
    {
        Animal::sonido();
        std::cout << "Sonido que emite: " << sonido_pajaro << std::endl;
    }

private:
    std::string sonido_pajaro;
};

int main()
{
    Perro perro("perro", 5, "Guau-Guau");
    perro.sonido();
    std::cout << std::endl;

    Gato gato("gato", 3, "Miau-Miau");
    gato.sonido();
    std::cout << std::endl;

    Pajaro pajaro("pajaro", 2, "Pio-pio");
    pajaro.sonido();

    return 0;
}
