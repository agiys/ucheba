using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace RunGroopWebApp.Models
{
    public class Room
    {
        [Key]
        public int Id { get; set; }

        public int Number { get; set; }

        public string Type { get; set; }

        public int CountRoom { get; set; }

        public decimal Price { get; set; }

        public string Description { get; set; }

        public bool State { get; set; }
        [ForeignKey("Reservation")]
        public int ReservationId { get; set; }

        public ICollection<Service> Services { get; set; }
    
    }
}
