using HotelWebApp.Data.Enum;
using Microsoft.AspNetCore.Identity;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace HotelWebApp.Models
{
    public class FinancialTransaction
    {
        [Key]
        public int Id { get; set; }

        public ServicesCategory? ServicesCategory { get; set; }
        
        [ForeignKey("Reservation")]
        public int ReservationId { get; set; }

        public decimal Price { get; set; }

        public DateTime Date { get; set; }
    }
}
