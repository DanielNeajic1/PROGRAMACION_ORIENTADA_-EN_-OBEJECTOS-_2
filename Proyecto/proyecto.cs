using System;

class Program
{
    static void Main()
    {
        // Tipos de datos
        int numero = 100;
        float decimalFlotante = 3.14f;
        double decimalDoble = 3.14159;
        char letra = 'A';
        string saludo = "Hola, mundo";

        // Salida en consola
        Console.WriteLine("Entero: " + numero);
        Console.WriteLine("Flotante: " + decimalFlotante);
        Console.WriteLine("Doble: " + decimalDoble);
        Console.WriteLine("Carácter: " + letra);
        Console.WriteLine("Cadena: " + saludo);

        Console.WriteLine("Presiona cualquier tecla para salir...");
        Console.ReadKey();
    }
}