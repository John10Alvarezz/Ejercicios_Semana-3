#include <iostream>
#include <cmath>

class Circulo {
private:
    double radio;
public:
    Circulo(double radio) {
        this->radio = radio;
    }
    double calcularArea() {
        return M_PI * pow(this->radio, 2);
    }
    double calcularPerimetro() {
        return 2 * M_PI * this->radio;
    }
    void cambiarRadio(double nuevo_radio) {
        this->radio = nuevo_radio;
    }
};

int main() {
    double radio_inicial = 6;
    Circulo calcular_circulo(radio_inicial);

    double area = calcular_circulo.calcularArea();
    std::cout << "El área del círculo es: " << area << std::endl;

    double perimetro = calcular_circulo.calcularPerimetro();
    std::cout << "El perímetro del círculo es: " << perimetro << std::endl;

    return 0;
}
