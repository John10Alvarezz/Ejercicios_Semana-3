class Circulo {
private:
    double radio;

public:
    // Constructor para inicializar el radio
    Circulo(double r) : radio(r) {}

    // Método para calcular el área del círculo
    double calcularArea() {
        return 3.14159265358979323846 * radio * radio; // Usamos una aproximación de PI
    }

    // Método para calcular el perímetro del círculo
    double calcularPerimetro() {
        return 2.0 * 3.14159265358979323846 * radio; // Usamos una aproximación de PI
    }

    // Método para cambiar el radio del círculo
    void cambiarRadio(double nuevoRadio) {
        radio = nuevoRadio;
    }
};

int main() {
    // Instancia un objeto de la clase Circulo con un radio inicial de 5.0
    Circulo miCirculo(5.0);

    // Calcula el área y el perímetro del círculo
    double area = miCirculo.calcularArea();
    double perimetro = miCirculo.calcularPerimetro();

    // Muestra el área y el perímetro del círculo
    // sin usar la biblioteca iostream
    asm(
        "movl $4, %%eax;"
        "movl $1, %%ebx;"
        "movl %0, %%ecx;"
        "movl $18, %%edx;"
        "int $0x80;"
        "movl $4, %%eax;"
        "movl $1, %%ebx;"
        "movl %1, %%ecx;"
        "movl $18, %%edx;"
        "int $0x80;"
        :
        : "m"(area), "m"(perimetro)
        : "eax", "ebx", "ecx", "edx"
    );

    return 0;
}
