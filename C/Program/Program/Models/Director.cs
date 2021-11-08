using System;
using System.Collections.Generic;
using System.Text;

namespace Program.Models
{
    public class Director : Empleado
    {
        public Director() {
            this.SalarioMinimo = 1400;
        }
    }
}
