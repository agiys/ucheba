using System.Diagnostics;
using System.Security.Cryptography.X509Certificates;
using System.Text;
namespace Lr4
{
    enum type { Автобус, Поезд, Самолет, Такси }

    class Transport
    {
        int price;
        public type type;
        

        public Transport(int price)
        {
            
            this.price = price;
            
            
        }
        

        static void Main(string[] args)
        {
            Transport transport = new Transport(1500);
            transport.type = type.Такси;
            Console.WriteLine(" цена " + transport.price + " вид трнанспорта " + transport.type);

            Console.WriteLine(" введите стоимость для сравнения ");
            string st = Console.ReadLine();
            while (int.TryParse(st, out int stoim))
            {
                if (stoim > transport.price)
                {
                    Console.WriteLine("Проезд на вашем транспорте дороже ");
                    return;
                }
                if (stoim == transport.price)
                {
                    Console.WriteLine("Стоимость равна ");
                    return;
                }
                else
                {
                    Console.WriteLine("Стоимость дешевле ");
                    return;
                }

            }
            

        }
        
    }
        
}

