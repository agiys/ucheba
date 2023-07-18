using HotelWebApp.Models;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace RunGroopWebApp.Models
{
    public class Reservation
    {
        [Key]
        public int Id { get; set; }
        
        [ForeignKey("Guest")]
        public int GuestId { get; set; }

        [ForeignKey("Room")]
        public int RoomId { get; set; }

        public DateTime CheckIn { get; set; }

        public DateTime CheckOut { get; set; }

        public string Conditions { get; set; }

        [ForeignKey("Transaction")]
        public int FinancialTransactionId { get; set; }

    }
}
