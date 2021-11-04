using System;

namespace FundamentosLenguaje
{
    class Program
    {
        static void Main(string[] args)
        {
            DiaNacimiento();
        }


        static void DiaNacimiento()
        {

            Console.WriteLine("Día");
            string dato = Console.ReadLine();
            int dia = int.Parse(dato);
            Console.WriteLine("Mes");
            dato = Console.ReadLine();
            int mes = int.Parse(dato);
            Console.WriteLine("Año");
            dato = Console.ReadLine();
            int anio = int.Parse(dato);


            if (mes == 1)
            {
                mes = 13;
                anio -= 1;
            }

            if (mes == 2)
            {
                mes = 14;
                anio -= 1;
            }

            int num1 = 0, num2 = 0, num3 = 0, num4 = 0;

            num1 = (((mes + 1) * 3) / 5);
            num2 = (anio / 4);
            num3 = (anio / 100);
            num4 = (anio / 400);

            num1 = dia + (mes * 2) + anio + num1 + num2 - num3 + num4 + 2;
            num2 = (num1 / 7);
            num3 = num1 - (num2 * 7);

            if (num3 == 0)
            {
                Console.WriteLine("Naciste en sábado");
            }
            else if (num3 == 1)
            {
                Console.WriteLine("Naciste en domingo");
            }
            else if (num3 == 2)
            {
                Console.WriteLine("Naciste en lunes");
            }
            else if (num3 == 3)
            {
                Console.WriteLine("Naciste en martes");
            }
            else if (num3 == 4)
            {
                Console.WriteLine("Naciste en miercoles");
            }
            else if (num3 == 5)
            {
                Console.WriteLine("Naciste en jueves");
            }
            else if (num3 == 6)
            {
                Console.WriteLine("Naciste en viernes");
            }

        }

        static void MayorTresNumeros()
        {
            Console.WriteLine("Número 1: ");
            string dato = Console.ReadLine();
            int numero1 = int.Parse(dato);
            Console.WriteLine("Número 2: ");
            dato = Console.ReadLine();
            int numero2 = int.Parse(dato);
            Console.WriteLine("Número 3: ");
            dato = Console.ReadLine();
            int numero3 = int.Parse(dato);
            int mayor = 0, menor = 0, intermedio = 0;
            if (numero1 >= numero2 && numero1 >= numero3)
            {
                mayor = numero1;
            }
            else if (numero2 >= numero1 && numero2 >= numero3)
            {
                mayor = numero2;
            }
            else
            {
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
            Console.WriteLine("Número mayor: " + mayor);
            Console.WriteLine("Número menor: " + menor);
            Console.WriteLine("Intermedio: " + intermedio);
        }

        static void NumeroPositivoNegativo()
        {
            Console.WriteLine("Introduzca un número");
            //RECUPERO EL VALOR EN UNA VARIABLE STRING
            String dato = Console.ReadLine();
            //DECLARAMOS UN int PARA CONVERTIR EL DATO
            int numero = int.Parse(dato);
            //EVALUAMOS CON UNA CONDICION POSITIVO, NEGATIVO O CERO
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