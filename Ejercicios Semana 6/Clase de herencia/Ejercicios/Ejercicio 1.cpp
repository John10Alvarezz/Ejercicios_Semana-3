#include <iostream>
#include <string>

class Producto
{
public:
    std::string nombre;
    std::string precio;
    std::string categoria;

    Producto(std::string nombre, std::string precio, std::string categoria)
    {
        this->nombre = nombre;
        this->precio = precio;
        this->categoria = categoria;
    }

    void mostrar_detalle()
    {
        std::cout << "nombre: " << nombre << std::endl;
        std::cout << "precio: " << precio << std::endl;
        std::cout << "categoria: " << categoria << std::endl;
    }
};

class Electronico : public Producto
{
public:
    int unidades;

    Electronico(std::string nombre, std::string precio, std::string categoria, int unidades)
        : Producto(nombre, precio, categoria)
    {
        this->unidades = unidades;
    }

    void mostrar_detalle()
    {
        std::cout << "Producto Electronico:" << std::endl;
        Producto::mostrar_detalle();
        std::cout << "Unidades disponibles: " << unidades << std::endl;
    }
};

class Alimeticio : public Producto
{
public:
    int paquetes;

    Alimeticio(std::string nombre, std::string precio, std::string categoria, int paquetes)
        : Producto(nombre, precio, categoria)
    {
        this->paquetes = paquetes;
    }

    void mostrar_detalle()
    {
        std::cout << "Producto Alimenticio:" << std::endl;
        Producto::mostrar_detalle();
        std::cout << "N de paquetes: " << paquetes << std::endl;
    }
};

class Vestimenta : public Producto
{
public:
    std::string color;

    Vestimenta(std::string nombre, std::string precio, std::string categoria, std::string color)
        : Producto(nombre, precio, categoria)
    {
        this->color = color;
    }

    void mostrar_detalle()
    {
        std::cout << "Producto de vestir:" << std::endl;
        Producto::mostrar_detalle();
        std::cout << "Color: " << color << std::endl;
    }
};

int main()
{
    Electronico electronico("Lavadora", "$120.000", "Linea Blanca", 5);
    electronico.mostrar_detalle();
    std::cout << std::endl;

    Alimeticio alimenticio("Arroz", "$7.000", "Alimentos", 2);
    alimenticio.mostrar_detalle();
    std::cout << std::endl;

    Vestimenta vestimenta("Pantalones", "$12.000", "Ropa", "Rojo");
    vestimenta.mostrar_detalle();

    return 0;
}
