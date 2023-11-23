using Newtonsoft.Json;
using RegistrationBook.Models;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RegistrationBook.Repository
{
    class AppService : IService
    {
        private readonly string PATH = $"{Environment.CurrentDirectory}\\clients.json";

        public BindingList<Client> GetClients()
        {
            var fileExists = File.Exists(PATH);
            if (!fileExists)
            {
                File.CreateText(PATH).Dispose();
                return new BindingList<Client>();
            }
            using (var reader = File.OpenText(PATH))
            {
                var text = reader.ReadToEnd();
                return JsonConvert.DeserializeObject<BindingList<Client>>(text);
            }
        }

        public void SaveClients(object clientList)
        {
            using (StreamWriter writer = File.CreateText(PATH))
            {
                string output = JsonConvert.SerializeObject(clientList);
                writer.Write(output);
            }
        }

        //private void LoadClients()
        //{
        //    string jsonFilePath = "clientss.json";
        //    List<Client> loadedClients = new List<Client>();

        //    if (File.Exists(jsonFilePath))
        //    {
        //        string json = File.ReadAllText(jsonFilePath);

        //        if (!string.IsNullOrWhiteSpace(json))
        //        {
        //            loadedClients = JsonConvert.DeserializeObject<List<Client>>(json);
        //        }
        //    }

        //    return new BindingList<Client>(loadedClients);
        //}
    }
}
