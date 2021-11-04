using System;

namespace Program
{
    class Program
    {
        static void Main(string[] args)
        {
            MayorTresNum();
        }


        static void MayorTresNum() {
            Console.WriteLine("Primer número");
            string dato = Console.ReadLine();
            int numero1 = int.Parse(dato);
            Console.WriteLine("Segundo número");
            dato = Console.ReadLine();
            int numero2 = int.Parse(dato);
            Console.WriteLine("Tercer número");
            dato = Console.ReadLine();
            int numero3 = int.Parse(dato);

            int mayor=0, menor=0, intermedio=0;

            if (numero1 >= numero2 && numero1 >= numero3) 
            {
                mayor = numero1;
            } else if (numero2 >= numero1 && numero2 >= numero3) {
                mayor = numero2;
            }
            else {
                mayor = numero3;
            }

            if (numero1 <= numero2 && numero1 <= numero3)
            {
                menor = numero1;
            }
            else if (numero2 <= numero1 && numero2 <= numero3)
            {
                menor = numero2;
            }
            else
            {
                menor = numero3;
            }

            int suma = (numero1 + numero2 + numero3);
            intermedio = suma - mayor - menor;
            Console.WriteLine("Mayor: " + mayor);
            Console.WriteLine("Menor: " + menor);
            Console.WriteLine("Intermedio: " + intermedio);
        }

        static void NumeroPositivoNegativo() {
            Console.WriteLine("Dame número: ");
            string dato = Console.ReadLine();
            int numero = int.Parse(dato);
            if (numero > 0)
            {
                Console.WriteLine("POSITIVO");
            }
            else if (numero == 0)
            {
                Console.WriteLine("CERO");
            }
            else 
            {
                Console.WriteLine("NEGATIVO");
            }

        }
    }
}
