using System;
using System.Collections.Generic;
using System.Text;

namespace Program.Models
{   public enum Paises { España, Francia, Alemania, Italia, Japon}
    public class Persona
    {

        public Persona() 
        {
            this.Edad = 20;
            this.Nacionalidad = Paises.España;
        }

        public Persona(string nombre, string apellido) {
            this.Nombre = nombre;
            this.Apellidos = apellido;
        }

        public void ConvertirDescripciones() {

            for (int i = 0; i < this._Descripciones.Length; i++) {
                this._Descripciones[i] = this._Descripciones[i].ToUpper();
            }
        }

        public string GetNombreCompleto() {
            return this.Nombre + " " + this.Apellidos;
        }

        public string GetNombreCompleto(int numero)
        {
            return this.Nombre + " ------------ " + this.Apellidos;
        }

        public string GetNombreCompleto(bool orden) {
            if (orden == true)
            {
                return this.Apellidos + " " + this.Nombre;
            }
            else {
                return this.GetNombreCompleto();
            }
        }

        private string[] _Descripciones = new string[3];
        public string this[int indice]
        {
            get {
                return this._Descripciones[indice];
            }
            set {
                this._Descripciones[indice] = value;
            }
        }
        public Paises Nacionalidad { get; set; }
        public string Nombre { get; set; }
        public String Apellidos { get; set; }
        private int _Edad;
        public int Edad 
        {
            get 
            {
                return this._Edad;
            }
            set {

                if (value < 0)
                {
                    throw new Exception("La edad no puede ser negativa");
                }
                else {
                    this._Edad = value;
                }

                
            }
        }
    }
}
