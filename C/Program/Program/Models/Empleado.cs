using System;
using System.Collections.Generic;
using System.Text;

namespace Program.Models
{
    public class Empleado : Persona
    {
        public Empleado()
        {
            this.SalarioMinimo = 900;
        }

        public int Salario { get; set; }

        protected int SalarioMinimo { get; set; }


    }
}
