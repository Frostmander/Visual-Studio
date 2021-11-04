using System;

namespace Prueba
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.BackgroundColor = ConsoleColor.Green;

            Console.WriteLine("Dame el primer número:");
            string dato = Console.ReadLine();
            int num1 = int.Parse(dato);
            Console.WriteLine("Dame el segundo número");
            dato = Console.ReadLine();
            int num2 = int.Parse(dato);

            int suma = num1 + num2;
            Console.WriteLine("La suma es " + suma);


        }
    }
}
