#include <iostream>

class Circulo {
private:
    double radio;
public:
    Circulo(double radio) {
        this->radio = radio;
    }
    double calcularArea() {
        return 3.14159 * radio * radio;
    }
    double calcularPerimetro() {
        return 2 * 3.14159 * radio;
    }
    void cambiarRadio(double nuevo_radio) {
        this->radio = nuevo_radio;
    }
};

int main() {
    double radio_inicial = 6;
    Circulo miCirculo(radio_inicial);

    double area = miCirculo.calcularArea();
    std::cout << "El área del círculo es: " << area << std::endl;

    double perimetro = miCirculo.calcularPerimetro();
    std::cout << "El perímetro del círculo es: " << perimetro << std::endl;

    return 0;
}
