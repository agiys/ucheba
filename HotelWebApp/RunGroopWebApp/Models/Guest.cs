using HotelWebApp.Data.Enum;
using RunGroopWebApp.Models;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace HotelWebApp.Models
{
    public class Guest
    {
        [Key]
        public int Id { get; set; }

        public string FirstName { get; set; }

        public string LastName { get; set; }

        public string SurName { get; set; }

        public string PassportData { get; set; }

        public string? PhoneNumber { get; set; }

        public string? Email { get; set; }

        public string? Wishes { get; set; }
        
        public ICollection<Reservation> Reservations { get; set; }
    }
}
