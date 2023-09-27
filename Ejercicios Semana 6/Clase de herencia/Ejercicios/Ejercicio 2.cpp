#include <iostream>
#include <string>

class Empleado
{
public:
    Empleado(std::string nombre, int edad, std::string salario)
    {
        this->nombre = nombre;
        this->edad = edad;
        this->salario = salario;
    }
    void describir_rol()
    {
        std::cout << "Mi nombre es " << nombre << ", tengo " << edad << " años, mi sueldo es " << salario << std::endl;
    }

private:
    std::string nombre;
    int edad;
    std::string salario;
};

class Gerente : public Empleado
{
public:
    Gerente(std::string nombre, int edad, std::string salario, std::string departamento) : Empleado(nombre, edad, salario)
    {
        this->departamento = departamento;
    }
    void describir_rol()
    {
        Empleado::describir_rol();
        std::cout << "y trabajo en el departamento de " << departamento << std::endl;
    }

private:
    std::string departamento;
};

class Ingeniero : public Empleado
{
public:
    Ingeniero(std::string nombre, int edad, std::string salario, std::string especialidad) : Empleado(nombre, edad, salario)
    {
        this->especialidad = especialidad;
    }
    void describir_rol()
    {
        Empleado::describir_rol();
        std::cout << "y me especializo en el area de " << especialidad << std::endl;
    }

private:
    std::string especialidad;
};

class Asistente : public Empleado
{
public:
    Asistente(std::string nombre, int edad, std::string salario, std::string tarea) : Empleado(nombre, edad, salario)
    {
        this->tarea = tarea;
    }
    void describir_rol()
    {
        Empleado::describir_rol();
        std::cout << "y mi labor es " << tarea << std::endl;
    }

private:
    std::string tarea;
};

int main()
{
    Gerente gerente("Patricio", 40, "$1.100.000", "Ventas");
    gerente.describir_rol();
    std::cout << std::endl;

    Ingeniero ingeniero("Neymar", 29, "$1.500.000", "Informatica");
    ingeniero.describir_rol();
    std::cout << std::endl;

    Asistente asistente("Fabricio", 24, "$600.000", "Agendar visitas");
    asistente.describir_rol();

    return 0;
}
