#include <iostream>

class rectangulo {
private:
    int longitud;
    int ancho;
public:
    rectangulo(int longitud, int ancho) {
        this->longitud = longitud;
        this->ancho = ancho;
    }
    int calcularArea() {
        return longitud * ancho;
    }
    int calcularPerimetro() {
        return ancho * 2 + longitud * 2;
    }
    void cambiarLongitud(int nueva_longitud) {
        longitud = nueva_longitud;
    }
    void cambiarAncho(int nuevo_ancho) {
        ancho = nuevo_ancho;
    }
};

int main() {
    int valor_longitud = 7;
    int valor_ancho = 5;
    rectangulo mi_rectangulo(valor_longitud, valor_ancho);
    int area = mi_rectangulo.calcularArea();
    std::cout << "El área del rectangulo es: " << area << std::endl;
    int perimetro = mi_rectangulo.calcularPerimetro();
    std::cout << "El perímetro del rectangulo es: " << perimetro << std::endl;
    return 0;
}