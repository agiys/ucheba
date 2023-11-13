using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RegistrationBook.Models
{
    [Serializable]
    public class Client : INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler? PropertyChanged;

        public string Name { get; set; }
        public string PetName { get; set; }
        public string Type { get; set; }
        public string Description { get; set; }
        public string Phone { get; set; }
        public string Data { get; set; }
        public string Breed { get; set; }
        public bool Turnout { get; set; }   

    }
}
