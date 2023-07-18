using HotelWebApp.Data.Enum;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace RunGroopWebApp.Models
{
    public class Service
    {
        [Key]
        public int Id { get; set; }

        public string Name { get; set; }

        public ServicesCategory ServicesCategory { get; set; }    

        public string? Description { get; set; }

        public decimal Price { get; set; }

        public ICollection<Room> Rooms { get; set; }
    }
}
