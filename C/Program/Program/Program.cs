using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;
using Program.Models;

namespace Program
{
    enum TipoChar { Letras, Numeros, Simbolos}
    class Program
    {
        static void Main(string[] args)
        {
            Persona person = new Persona();
            person.Nombre = "Sinoshuke";
            person.Apellidos = "Yamamoto";
            //person.Edad = 23;
            //person.Nacionalidad = Paises.Japon;
            person[0] = "Ojos azules";
            person[1] = "Pelo largo";
            person[2] = "Cicatriz";
            person.ConvertirDescripciones();
            Console.WriteLine(person.Nombre + ", " + person.Apellidos + ", " + person.Edad);
            Console.WriteLine(person.Nacionalidad);
            Console.WriteLine(person[1]);
            Console.WriteLine(person.GetNombreCompleto());
            Console.WriteLine(person.GetNombreCompleto(true));
            Console.WriteLine(person.GetNombreCompleto(23));

            Persona person2 = new Persona("Lucas", "Trotacielos");
            Console.WriteLine(person2.GetNombreCompleto());

            Empleado emp = new Empleado();
            emp.Nombre = "Luis";
            emp.Apellidos = "Barcenas";
            Console.WriteLine(emp.GetNombreCompleto());
        }

        static void ListaNombres() {
            String respuesta = " ";
            List<string> nombres = new List<string>();

            while (respuesta != "PARA") {
                Console.WriteLine("Introduce un nombre: (PARA)");
                respuesta=Console.ReadLine();
                nombres.Add(respuesta);
            }

            nombres.Remove("PARA");
            Console.WriteLine("--------------------------------------");
            foreach (string name in nombres) {
                Console.WriteLine(name);
            }
        }

        static void EjemploColecciones() {

            List<int> numeros = new List<int>();
            numeros.Add(34);
            numeros.Add(432);
            foreach (int num in numeros) {
                Console.WriteLine(num);
            }

            List<String> nombres = new List<string>();
            nombres.Add("Padmé");
            nombres.Add("Leia");
            nombres.Add("Luke");
            nombres.Add("Mace");
            //nombres.Remove("Leia");
            nombres.RemoveAt(3);
            foreach (string name in nombres) {
                Console.WriteLine(name);
            }

        }

        static void InvertirTextoStringBuilder(String datos)
        {
            Stopwatch cronos = new Stopwatch();
            cronos.Start();
            StringBuilder texto = new StringBuilder();
            texto.Append(datos);
            for (int i = 0; i < texto.Length; i++)
            {
                char letra = texto[texto.Length - 1];
                texto = texto.Remove(texto.Length - 1, 1);
                texto = texto.Insert(i, letra.ToString());
            }
            cronos.Stop();
            Console.WriteLine(texto);
            Console.Write("Milisegundos: " + cronos.Elapsed.TotalMilliseconds);
            Console.WriteLine("-------------------------------");
        }

        static void InvertirTextoString(String texto) 
        {
            Stopwatch cronos = new Stopwatch();
            cronos.Start();
            for (int i = 0; i < texto.Length; i++) {
                char letra = texto[texto.Length - 1];
                texto = texto.Remove(texto.Length - 1, 1);
                texto = texto.Insert(i, letra.ToString());
            }
            cronos.Stop();
            Console.WriteLine(texto);
            Console.Write("Milisegundos: " + cronos.Elapsed.TotalMilliseconds);
            Console.WriteLine("-------------------------------");
        }

        static void SumarNumerosString() {
            Console.WriteLine("Introduzca un texto");
            string texto = Console.ReadLine();
            int suma = 0;

            for (var i = 0; i < texto.Length; i++) {
                char caracter = texto[i];

                //int numero = (int)caracter;
                int numero = int.Parse(caracter.ToString());

                suma += numero;
            }
            Console.WriteLine(suma);
        }

        static void EjemploChar(TipoChar tipo)
        {
            for (int i = 0; i <= 255; i++)
            {
                char letra = (char)i;
                if (tipo == TipoChar.Simbolos)
                {
                    if (char.IsSymbol(letra))
                    {
                        Console.WriteLine(letra);
                    }
                }
                else if (tipo == TipoChar.Letras)
                {
                    if (char.IsLetter(letra))
                    {
                        Console.WriteLine(letra);
                    }
                }
                else if (tipo == TipoChar.Numeros)
                {
                    if (char.IsNumber(letra))
                    {
                        Console.WriteLine(letra);
                    }
                }
            }
        }

        static void SumarNumeros() {

            Console.WriteLine("Introduzca números: (0 para terminar)");
            string dato=Console.ReadLine();
            int numero = int.Parse(dato);
            int suma = 0;
            while (numero != 0) {
                suma += numero;
                Console.WriteLine("Suma: " + suma);
                Console.WriteLine("Introduzca números: (0 para terminar)");
                dato = Console.ReadLine();
                numero = int.Parse(dato);
            }
            Console.WriteLine("¡Adios!");


        }

        static void NumerosPares()
        {
            Console.WriteLine("Introduzca un inicio: ");
            string dato = Console.ReadLine();
            int inicio = int.Parse(dato);
            Console.WriteLine("Introduzcxa un fin: ");
            dato = Console.ReadLine();
            int fin = int.Parse(dato);

            for (int i = inicio; i <= fin; i++)
            {
                if (i % 2 == 0) {
                    Console.WriteLine(i);
                }
                
            }
        }

        static void ConjeturaCollatz() {
            Console.WriteLine("Introduzca un número");
            string dato = Console.ReadLine();
            int numero = int.Parse(dato);

            while (numero != 1) {

                if (numero % 2 == 0)
                {
                    numero = numero / 2;
                }
                else {
                    numero = numero * 3 + 1;
                }
                Console.WriteLine(numero);
            
            }
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