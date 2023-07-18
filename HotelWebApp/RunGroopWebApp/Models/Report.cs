using HotelWebApp.Data.Enum;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace HotelWebApp.Models
{
    public class Report
    {
        [Key]
        public int Id { get; set; }

        public ReportsCategory ReportsCategory { get; set; }

        public string DataReport { get; set; }
        
        [ForeignKey("Administrator")]
        public int AdministratorId { get; set; }

        public DateTime Date { get; set; }
    }
}
